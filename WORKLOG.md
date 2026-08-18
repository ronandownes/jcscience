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

### Expansion completed in the same pass

- Checked the current official Curriculum Online Science learning outcomes and built `curriculum/learning-outcomes.yml`, mapping every strand outcome to current source and exposing gaps.
- Used that gap analysis to add major specification-completion chapters:
  - `science-society.ptx` — scientific change, scientists/contributions, media claims, technology and society;
  - `quantitative-physics.ptx` — instruments, area/volume, density, acceleration, force measurement, current/voltage/resistance/power;
  - `chemical-patterns-energy.ptx` — atom ratios, material properties, reaction rate, gases, biochemical rates, exothermic/endothermic reactions and activation energy;
  - `life-health-reproduction.ptx` — health factors, microorganisms, human reproduction, reproductive health, habitat study, ecosystem services and global food;
  - `cosmos-carbon-energy.ptx` — celestial relationships, Big Bang model, planetary comparison, carbon cycle, energy sources, electricity ethics and space exploration.
- Added `source/practicals.ptx`, a large cross-strand practical bank covering physical, chemical, biological and Earth/Space investigations with safety, analysis, evaluation and deeper extensions.
- Added `source/interactive-checks.ptx` using native PreTeXt interactive true/false and multiple-choice markup with misconception-specific feedback.
- Added `data/concepts/core.yml`, seeding the canonical concept architecture with three-level Understand / Exam-ready / Precise wording across the course.
- Added `curriculum/JUNIOR-CYCLE-FRAMEWORK.md` connecting the book design to outcomes-based Junior Cycle, common-level Science, key skills, Statements of Learning, literacy/numeracy, inclusion and assessment.
- Added `tools/check_source.py` and wired it into GitHub Actions before the full PreTeXt build so malformed XML, missing includes and duplicate `xml:id` values fail early.
- Updated `source/main.ptx` so all new chapters, practicals and interactive diagnostics are part of the actual book build.
- Refreshed `PROJECT-STATUS.md` to reflect the expanded repository rather than the earlier skeleton state.

### Important state

The repository has moved from architecture/documentation into a serious first textbook. It now contains broad specification coverage, three reading routes, investigations, practical work, interactive diagnostics, mixed assessment, framework alignment and canonical concept infrastructure.

It is still not a finished publication. The most important next technical step is observing and repairing any concrete PreTeXt schema/build errors from GitHub Actions. After the build is green, the main content priorities are refreshed LO audit, more native diagrams/representations, a much larger exam-pattern-informed question bank, and connecting chapter definitions to canonical concept data.

### Next contributor

Read `PROJECT-STATUS.md` and `NEXT.md` first. Do not redesign from scratch. Preserve the specification-led architecture and the Read less / Standard / Go deeper principle. Update this worklog and status after any substantial session.
