#!/usr/bin/env python3
"""Download the JC/Junior Certificate Science assessment corpus from the
Maynooth University Maths & Stats State Exam Papers archive.

The script deliberately separates *discovery/provenance* from Git tracking:
files are downloaded into references/exams/sec/ for local/private working use.
Whether the binaries themselves are committed is a separate rights/workflow
choice. The canonical source URL is retained in a manifest.

Default target corpus:
- Junior Certificate Science Higher + Ordinary, 2009-2018
- Science paper, 2019-2020
- no 2021 paper (archive has no Science entry)
- Junior Cycle Science, 2022-2026
- Science sample papers from 2018 and 2019 when present on the archive page
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

ARCHIVE_URL = "https://archive.maths.nuim.ie/staff/dmalone/StateExamPapers/"
DEFAULT_OUTPUT = Path("references/exams/sec")
YEAR_MIN = 2009
YEAR_MAX = 2026


def safe_name(url: str) -> str:
    name = Path(urlparse(url).path).name
    return name or "paper.pdf"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def get_html(session: requests.Session) -> BeautifulSoup:
    r = session.get(ARCHIVE_URL, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def find_junior_table(soup: BeautifulSoup):
    for heading in soup.find_all(["h1", "h2", "h3", "h4"]):
        text = heading.get_text(" ", strip=True).lower()
        if "junior" in text and "certificate" in text:
            table = heading.find_next("table")
            if table:
                return table
    raise RuntimeError("Could not locate Junior/Intermediate Certificate table")


def discover_exam_links(soup: BeautifulSoup) -> list[dict]:
    table = find_junior_table(soup)
    records: list[dict] = []

    rows = table.find_all("tr")
    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) < 3:
            continue

        year_text = cells[0].get_text(" ", strip=True)
        match = re.search(r"\b(19|20)\d{2}\b", year_text)
        if not match:
            continue

        year = int(match.group(0))
        if not (YEAR_MIN <= year <= YEAR_MAX):
            continue

        science_cell = cells[2]
        links = science_cell.find_all("a", href=True)
        for a in links:
            href = a["href"]
            label = a.get_text(" ", strip=True) or "Science"
            url = urljoin(ARCHIVE_URL, href)
            if not url.lower().endswith(".pdf"):
                continue
            records.append(
                {
                    "kind": "exam",
                    "year": year,
                    "label": label,
                    "source_url": url,
                    "filename": safe_name(url),
                }
            )

    return records


def discover_samples(soup: BeautifulSoup) -> list[dict]:
    wanted = {
        "ScienceSample-JC-2018.pdf",
        "ScienceSample-JC-2019.pdf",
    }
    records: list[dict] = []
    for a in soup.find_all("a", href=True):
        url = urljoin(ARCHIVE_URL, a["href"])
        name = safe_name(url)
        if name in wanted:
            year_match = re.search(r"(20\d{2})", name)
            records.append(
                {
                    "kind": "sample",
                    "year": int(year_match.group(1)) if year_match else None,
                    "label": "Sample",
                    "source_url": url,
                    "filename": name,
                }
            )
    return records


def download(session: requests.Session, record: dict, output: Path, overwrite: bool) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    target = output / record["filename"]

    if target.exists() and not overwrite:
        result = dict(record)
        result.update(
            {
                "local_path": str(target.as_posix()),
                "sha256": sha256(target),
                "status": "existing",
            }
        )
        return result

    r = session.get(record["source_url"], timeout=60)
    r.raise_for_status()

    content_type = r.headers.get("content-type", "").lower()
    if "pdf" not in content_type and not r.content.startswith(b"%PDF"):
        raise RuntimeError(f"Not a PDF: {record['source_url']}")

    target.write_bytes(r.content)
    result = dict(record)
    result.update(
        {
            "local_path": str(target.as_posix()),
            "sha256": sha256(target),
            "status": "downloaded",
        }
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-samples", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--list-only", action="store_true")
    args = parser.parse_args()

    session = requests.Session()
    session.headers.update(
        {"User-Agent": "jcscience-reference-fetcher/1.0 (+educational-project)"}
    )

    soup = get_html(session)
    records = discover_exam_links(soup)
    if not args.no_samples:
        records.extend(discover_samples(soup))

    # Deduplicate by source URL while preserving order.
    unique = []
    seen = set()
    for rec in records:
        if rec["source_url"] not in seen:
            seen.add(rec["source_url"])
            unique.append(rec)

    print(f"Discovered {len(unique)} Science PDFs")
    for rec in unique:
        print(f"{rec['year']}: {rec['label']:<8} {rec['source_url']}")

    if args.list_only:
        return 0

    completed = []
    for rec in unique:
        try:
            completed.append(download(session, rec, args.output, args.overwrite))
            print(f"OK  {rec['filename']}")
        except Exception as exc:
            failed = dict(rec)
            failed.update({"status": "failed", "error": str(exc)})
            completed.append(failed)
            print(f"ERR {rec['source_url']}: {exc}", file=sys.stderr)

    manifest = {
        "archive": ARCHIVE_URL,
        "purpose": "JC Science assessment-design reference corpus",
        "authority_note": (
            "Past papers are assessment evidence, not the curricular source of truth. "
            "The current Junior Cycle Science specification remains authoritative."
        ),
        "files": completed,
    }
    manifest_path = args.output / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Manifest: {manifest_path}")

    failures = sum(1 for x in completed if x.get("status") == "failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
