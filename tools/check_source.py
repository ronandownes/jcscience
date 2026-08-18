#!/usr/bin/env python3
"""Fast structural checks for the JC Science PreTeXt source tree.

This does not replace PreTeXt schema validation. It catches common authoring mistakes
before the full build: malformed XML, missing xi:includes and duplicate xml:id values.
"""
from __future__ import annotations

from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
XML_NS = "http://www.w3.org/XML/1998/namespace"
XI_NS = "http://www.w3.org/2001/XInclude"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    files = sorted(SOURCE.glob("*.ptx"))
    if not files:
        fail("No .ptx source files found")
        return 1

    errors = 0
    ids: dict[str, Path] = {}

    for path in files:
        try:
            tree = ET.parse(path)
        except ET.ParseError as exc:
            fail(f"Malformed XML in {path.relative_to(ROOT)}: {exc}")
            errors += 1
            continue

        root = tree.getroot()
        for elem in root.iter():
            xml_id = elem.attrib.get(f"{{{XML_NS}}}id")
            if xml_id:
                if xml_id in ids:
                    fail(
                        f"Duplicate xml:id '{xml_id}' in {path.relative_to(ROOT)} "
                        f"and {ids[xml_id].relative_to(ROOT)}"
                    )
                    errors += 1
                else:
                    ids[xml_id] = path

            if elem.tag == f"{{{XI_NS}}}include":
                href = elem.attrib.get("href")
                if not href:
                    fail(f"xi:include without href in {path.relative_to(ROOT)}")
                    errors += 1
                    continue
                target = (path.parent / href).resolve()
                if not target.exists():
                    fail(
                        f"Missing include '{href}' referenced from "
                        f"{path.relative_to(ROOT)}"
                    )
                    errors += 1

    if errors:
        print(f"Source checks failed with {errors} error(s).", file=sys.stderr)
        return 1

    print(f"Checked {len(files)} PreTeXt source files; {len(ids)} unique xml:id values.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
