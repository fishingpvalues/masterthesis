import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.customization import convert_to_unicode
from titlecase import titlecase
import re
import unicodedata

# Map of some common unicode to LaTeX equivalents (expand as needed)
UNICODE_LATEX_MAP = {
    "ä": '{"a}',
    "ö": '{"o}',
    "ü": '{"u}',
    "ß": "{\ss}",
    "Ä": '{"A}',
    "Ö": '{"O}',
    "Ü": '{"U}',
    "é": "{\\'e}",
    "è": "{\\`e}",
    "ê": "{\\^e}",
    "á": "{\\'a}",
    "à": "{\\`a}",
    "â": "{\\^a}",
    "É": "{\\'E}",
    "È": "{\\`E}",
    "Ê": "{\\^E}",
    "Á": "{\\'A}",
    "À": "{\\`A}",
    "Â": "{\\^A}",
    "ç": "{\\c{c}}",
    "Ç": "{\\c{C}}",
    "ñ": "{\\~n}",
    "Ñ": "{\\~N}",
    "ø": "{\\o}",
    "Ø": "{\\O}",
    "å": "{\\aa}",
    "Å": "{\\AA}",
    "œ": "{\\oe}",
    "Œ": "{\\OE}",
    "æ": "{\\ae}",
    "Æ": "{\\AE}",
    "í": "{\\'i}",
    "ì": "{\\`i}",
    "î": "{\\^i}",
    "Í": "{\\'I}",
    "Ì": "{\\`I}",
    "Î": "{\\^I}",
    "ó": "{\\'o}",
    "ò": "{\\`o}",
    "ô": "{\\^o}",
    "Ó": "{\\'O}",
    "Ò": "{\\`O}",
    "Ô": "{\\^O}",
    "ú": "{\\'u}",
    "ù": "{\\`u}",
    "û": "{\\^u}",
    "Ú": "{\\'U}",
    "Ù": "{\\`U}",
    "Û": "{\\^U}",
    # Add more as needed
}


def escape_non_ascii(text):
    """Replace non-ASCII characters with LaTeX equivalents or escape as unicode."""

    def repl(c):
        if c in UNICODE_LATEX_MAP:
            return UNICODE_LATEX_MAP[c]
        elif ord(c) < 128:
            return c
        else:
            # fallback: unicode code point
            return "{{\\char{}}}".format(ord(c))

    return "".join(repl(c) for c in text)


def split_protected(text):
    """
    Splits text into a list of (is_protected, segment) tuples.
    Protected segments are LaTeX commands, math, or {...}.
    """
    pattern = re.compile(
        r"(\\[a-zA-Z]+\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})"  # LaTeX command
        r"|(\$[^$]*\$|\$\$[^$]*\$\$|\\\([^\)]*\\\)|\\\[[^\]]*\\\])"  # Math
        r"|(\{[^{}]*\})"  # Braces
        r"|(\\[&%$#_{}~^\\])"  # Special LaTeX chars
    )
    result = []
    last = 0
    for m in pattern.finditer(text):
        start, end = m.span()
        if start > last:
            result.append((False, text[last:start]))
        result.append((True, text[start:end]))
        last = end
    if last < len(text):
        result.append((False, text[last:]))
    return result


def safe_titlecase(text):
    """Apply titlecase only to unprotected segments."""
    segments = split_protected(text)
    return "".join(seg if is_prot else titlecase(seg) for is_prot, seg in segments)


def is_title_case(text: str) -> bool:
    """Check if unprotected segments are in title case."""
    segments = split_protected(text)
    for is_prot, seg in segments:
        if not is_prot and seg.strip() and seg != titlecase(seg):
            return False
    return True


def apply_title_case(entry: dict, fields: list[str]) -> None:
    """Apply title case to specified fields while preserving LaTeX formatting."""
    for field in fields:
        if field in entry:
            if is_title_case(entry[field]):
                continue
            entry[field] = safe_titlecase(entry[field])


def process_bibtex_file(input_file: str, output_file: str) -> None:
    try:
        # Make a backup of the original file
        import shutil

        backup_file = output_file + ".bak"
        shutil.copy2(input_file, backup_file)
        print(f"Created backup of original file: {backup_file}")

        # Read the input file
        with open(input_file, "r", encoding="utf-8") as bibfile:
            parser = BibTexParser(common_strings=True)
            parser.customization = convert_to_unicode
            bib_database = bibtexparser.load(bibfile, parser=parser)

        # Process entries
        entry_count = len(bib_database.entries)
        changed_count = 0

        for entry in bib_database.entries:
            for field in ["title", "journal"]:
                if field in entry:
                    original = entry[field]
                    if not is_title_case(original):
                        entry[field] = safe_titlecase(original)
                        changed_count += 1
            # Escape all fields to ASCII/LaTeX
            for field in entry:
                if isinstance(entry[field], str):
                    entry[field] = escape_non_ascii(entry[field])

        # Write the output file carefully
        with open(
            output_file, "w", encoding="ascii", errors="backslashreplace"
        ) as bibfile:
            writer = BibTexWriter()
            # Configure the writer for compatibility
            writer.indent = "  "  # Standard indentation
            writer.comma_first = False  # Put commas at the end of lines
            writer.display_order = (
                "title",
                "author",
                "journal",
                "booktitle",
                "year",
            )  # Prioritize important fields

            bibfile.write(bibtexparser.dumps(bib_database, writer))

        print(
            f"Successfully processed {entry_count} entries ({changed_count} fields modified)"
        )
        print(f"Output written to {output_file}")

    except Exception as e:
        print(f"Error processing BibTeX file: {e}")
        import traceback

        traceback.print_exc()
        print(
            f"If the output file was corrupted, you can restore from the backup: {backup_file}"
        )


if __name__ == "__main__":
    input_file = "ref.bib"
    output_file = "ref_titlecase.bib"

    process_bibtex_file(input_file, output_file)
