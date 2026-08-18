# Worklog

## 2026-08-18 — PreTeXt production pass

### Completed

- Read the repository project brief and core learning architecture before authoring.
- Added a PreTeXt CLI v2 project manifest.
- Added `source/main.ptx` as a modular book entry point.
- Authored first substantial production chapters:
  - Nature of Science;
  - Physical World;
  - Chemical World;
  - Biological World;
  - Earth and Space;
  - Investigations and Practical Science;
  - Retrieval, Mixed Practice and Assessment.
- Implemented the three-route reading architecture throughout substantial sections: Read less / Standard / Go deeper.
- Added original examples, misconception corrections, investigation reasoning and mixed cross-strand assessment items.
- Corrected the project manifest to the PreTeXt CLI v2 attribute syntax after checking current official PreTeXt documentation.
- Added a GitHub Pages workflow that installs PreTeXt 2.44.0, builds the `web` target, uploads `output/web` and deploys using the current GitHub Pages action pattern.
- Added `PROJECT-STATUS.md`, `NEXT.md`, `DECISIONS.md` and this worklog so another AI can continue without requiring chat relay.

### Important state

The source tree is now materially populated, but this is still a first authored layer rather than a completed final textbook. It needs build verification, exact LO mapping, canonical concept data, diagrams/interactives, more practicals and a much larger metadata-rich assessment bank.

### Next contributor

Start with `PROJECT-STATUS.md` and `NEXT.md`. The immediate technical task is to verify the GitHub Actions build and repair only concrete PreTeXt/schema errors. After that, prioritise exact specification mapping and canonical concept data before multiplying prose blindly.
