import requests
import time
from typing import Optional
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter


def fetch_doi(title: str, author: str) -> Optional[str]:
    """Query CrossRef API to fetch DOI using title and first author."""
    url = "https://api.crossref.org/works"
    params = {"query.bibliographic": title, "query.author": author, "rows": 1}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        items = data.get("message", {}).get("items", [])
        if items:
            return items[0].get("DOI")
    return None


def update_bib_file(in_file: str, out_file: str) -> None:
    """Load .bib file, update entries missing a DOI, and write to new file."""
    with open(in_file, "r", encoding="utf-8") as bibtex_file:
        parser = BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    # Keep track of processing statistics
    entries_processed = 0
    dois_added = 0
    software_entries = 0

    for entry in bib_database.entries:
        entries_processed += 1

        # Skip DOI lookup for software entries
        if (
            entry.get("type", "").lower() == "software"
            or entry.get("howpublished", "").lower().startswith("software")
            or "software" in entry.get("note", "").lower()
        ):
            software_entries += 1
            print(
                f"Skipping DOI lookup for software entry: {entry.get('ID', 'Unknown')}"
            )
            continue

        # Try to add DOI only if it's missing
        if "doi" not in entry:
            title = entry.get("title", "")
            # Use first author from 'author' field; assumes ' and ' separator
            author = (
                entry.get("author", "").split(" and ")[0] if "author" in entry else ""
            )

            if title and author:  # Only attempt lookup if we have enough data
                doi = fetch_doi(title, author)
                if doi:
                    entry["doi"] = doi
                    dois_added += 1
                    print(f"Updated {entry.get('ID', 'Unknown')}: DOI added -> {doi}")
                else:
                    print(
                        f"No DOI found for {entry.get('ID', 'Unknown')}, but entry preserved."
                    )
                # Be kind to the API
                time.sleep(1)
            else:
                print(
                    f"Insufficient data for DOI lookup for {entry.get('ID', 'Unknown')}, but entry preserved."
                )

    writer = BibTexWriter()
    with open(out_file, "w", encoding="utf-8") as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file, writer=writer)

    print(f"\nSummary:")
    print(f"Entries processed: {entries_processed}")
    print(f"Software entries identified: {software_entries}")
    print(f"DOIs added: {dois_added}")
    print(f"Updated file saved to {out_file}")


if __name__ == "__main__":
    update_bib_file("ref.bib", "references_updated.bib")
