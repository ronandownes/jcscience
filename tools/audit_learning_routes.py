#!/usr/bin/env python3
"""Audit the three-route learning architecture in production PreTeXt source.

The project does not require every tiny utility section to have three routes, but
substantial explanatory sections should normally contain Read less, Standard and
Go deeper subsections. This script reports exceptions so they are deliberate.
"""
from __future__ import annotations

from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
REQUIRED = {"Read less", "Standard", "Go deeper"}
EXEMPT_FILES = {"main.ptx"}


def norm(text: str | None) -> str:
    return " ".join((text or "").split())


def main() -> int:
    checked = 0
    complete = 0
    exceptions: list[str] = []

    for path in sorted(SOURCE.glob("*.ptx")):
        if path.name in EXEMPT_FILES:
            continue
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError:
            continue  # malformed XML is handled by check_source.py

        for section in root.findall(".//section"):
            title_el = section.find("title")
            section_title = norm("".join(title_el.itertext())) if title_el is not None else "(untitled)"
            subsection_titles = set()
            for subsection in section.findall("subsection"):
                st = subsection.find("title")
                if st is not None:
                    subsection_titles.add(norm("".join(st.itertext())))

            # Treat a section with any of the route titles as intentionally routed.
            if subsection_titles & REQUIRED:
                checked += 1
                missing = sorted(REQUIRED - subsection_titles)
                if missing:
                    exceptions.append(
                        f"{path.relative_to(ROOT)} :: {section_title} :: missing {', '.join(missing)}"
                    )
                else:
                    complete += 1

    print(f"Three-route sections complete: {complete}/{checked}")
    if exceptions:
        print("Incomplete routed sections:")
        for item in exceptions:
            print(f" - {item}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
