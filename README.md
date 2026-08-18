# JC Science — PreTeXt

An open, expandable Junior Cycle Science book for Ireland, authored in PreTeXt.

The curriculum spine follows the NCCA Junior Cycle Science specification: Nature of Science as the unifying strand, with Earth and Space, Chemical World, Physical World, and Biological World developed through Building Blocks, Systems and Interactions, Energy, and Sustainability.

## Build

```bash
python -m pip install "pretext==2.44.0"
pretext build web
```

The HTML output is written to `output/web/`.

## Structure

- `project.ptx` — PreTeXt CLI project manifest
- `source/main.ptx` — book source
- `.github/workflows/pages.yml` — builds and deploys the real PreTeXt HTML to GitHub Pages

This repository is deliberately structured so individual topic chapters can be split into separate source files as the book grows.
