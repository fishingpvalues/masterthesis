import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.customization import convert_to_unicode
from titlecase import titlecase


def is_title_case(text: str) -> bool:
    return text == titlecase(text)


def apply_title_case(entry: dict, fields: list[str]) -> None:
    for field in fields:
        if field in entry:
            entry[field] = (
                titlecase(entry[field])
                if not is_title_case(entry[field])
                else entry[field]
            )


def process_bibtex_file(input_file: str, output_file: str) -> None:
    with open(input_file, "r", encoding="utf-8") as bibfile:
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibfile, parser=parser)

    for entry in bib_database.entries:
        apply_title_case(entry, ["title", "journal"])

    with open(output_file, "w", encoding="utf-8") as bibfile:
        writer = BibTexWriter()
        bibfile.write(bibtexparser.dumps(bib_database, writer))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Apply AP title case to BibTeX title and journal fields."
    )
    parser.add_argument("input", help="Input BibTeX file")
    parser.add_argument("output", help="Output BibTeX file")
    args = parser.parse_args()

    process_bibtex_file(args.input, args.output)
    print(f"Processed {args.input} -> {args.output}")
