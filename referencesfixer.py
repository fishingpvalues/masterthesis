import requests
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

    for entry in bib_database.entries:
        if "doi" not in entry:
            title = entry.get("title", "")
            # Use first author from 'author' field; assumes ' and ' separator
            author = entry.get("author", "").split(" and ")[0]
            doi = fetch_doi(title, author)
            if doi:
                entry["doi"] = doi
                print(f"Updated {entry.get('ID', 'Unknown')}: DOI added -> {doi}")
            else:
                print(f"No DOI found for {entry.get('ID', 'Unknown')}.")

    writer = BibTexWriter()
    with open(out_file, "w", encoding="utf-8") as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file, writer=writer)


if __name__ == "__main__":
    update_bib_file("ref.bib", "references_updated.bib")
