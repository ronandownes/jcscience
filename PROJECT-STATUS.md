# JC Science Project Status

_Last updated: 2026-08-18_

## Current state

The repository now contains a substantial modular PreTeXt book, curriculum maps, a canonical concept starter library, practical work, native interactive diagnostics and automated build/deployment infrastructure.

### Build infrastructure

- `project.ptx` — PreTeXt CLI v2 manifest for the `web` target.
- `source/main.ptx` — modular book entry point.
- `tools/check_source.py` — catches malformed XML, missing includes and duplicate `xml:id` values before the full build.
- `.github/workflows/pages.yml` — runs source checks, installs PreTeXt 2.44.0, builds `output/web`, uploads the Pages artifact and deploys it.
- GitHub Pages must use **GitHub Actions** as its publishing source.

### Production book source now present

Core strands and learning architecture:

- `source/nature-of-science.ptx`
- `source/science-society.ptx`
- `source/physical-world.ptx`
- `source/quantitative-physics.ptx`
- `source/chemical-world.ptx`
- `source/chemical-patterns-energy.ptx`
- `source/biological-world.ptx`
- `source/life-health-reproduction.ptx`
- `source/earth-space.ptx`
- `source/cosmos-carbon-energy.ptx`
- `source/investigations.ptx`
- `source/practicals.ptx`
- `source/interactive-checks.ptx`
- `source/retrieval-assessment.ptx`

The authored layer now goes beyond a strand skeleton. It includes substantial treatment of core physical quantities, electricity, reaction rates and energy, atom ratios, human health and reproduction, microorganisms, habitat study, ecosystem services, global food, Big Bang evidence, planetary comparison, carbon cycling, energy systems, space exploration, science-in-society, a cross-strand practical bank and misconception-targeted interactive checks.

### Three reading routes

Substantial sections deliberately implement:

- **Read less** — reduced linguistic load without reducing the scientific destination;
- **Standard** — complete Junior Cycle explanation;
- **Go deeper** — increased precision, mechanism, qualification, connection and transfer.

These are reading routes, not ability labels.

### Curriculum and framework layer

- `curriculum/learning-outcomes.yml` — project-authored paraphrase/map of the official Junior Cycle Science outcomes, with primary section links and explicit gap/status notes.
- `curriculum/JUNIOR-CYCLE-FRAMEWORK.md` — records implications of outcomes-based Junior Cycle design, common-level Science, key skills, Statements of Learning, literacy/numeracy, inclusion and assessment environment.

The map was checked against current Curriculum Online material on 2026-08-18. It exposed first-pass gaps, and a substantial number of those gaps were then addressed in the new production chapters listed above. The map itself should now be refreshed so statuses reflect the new content.

### Canonical concept layer

- `data/concepts/core.yml` — starter canonical concept library with project-owned Understand / Exam-ready / Precise wording for high-frequency concepts across Nature of Science, physics, chemistry, biology and Earth/Space.

Records remain `draft` until subjected to the concept-quality review process and checked against authoritative disciplinary sources where precision matters.

### Assessment and interaction

The book currently contains:

- structured exercises with solutions;
- mixed retrieval and cross-strand application;
- misconception clinics;
- original exam-style practice;
- native PreTeXt true/false and multiple-choice interactive diagnostic questions with specific feedback;
- an existing public-exam-corpus acquisition tool at `tools/fetch_science_papers.py`.

The question bank is still far smaller than the intended final resource. Past papers should be analysed as assessment-pattern data before large-scale generation of further exam-style material.

### Practical science

`source/practicals.ptx` currently includes cross-strand practical treatments for density, ramp motion, circuits/resistance, thermal insulation, reflection, conservation of mass, mixture separation, reaction rate, acids/bases and pH, reaction energy, microscopy/cells, photosynthesis, respiration, habitat study, climate datasets, and Earth-Sun-Moon modelling.

These are written as investigations with reasoning, safety and evaluation rather than recipe-only instructions.

## What remains before this is a finished textbook

This is now a serious first book, but it is **not yet a finished publication**. Major remaining work includes:

- verify the full PreTeXt schema/build through GitHub Actions and repair any concrete errors;
- refresh the learning-outcome map after the latest chapters and confirm every official outcome has complete treatment;
- review canonical concept records and connect chapter definitions to the data source rather than maintaining duplicated prose indefinitely;
- create many more native diagrams, data tables and representations;
- build a much larger metadata-rich formative/retrieval/exam-style question bank from assessment-pattern analysis;
- add more worked examples and non-examples inside conceptual sections;
- build cumulative spaced retrieval pathways;
- develop CBA/project exemplars and staged project workflows;
- add accessibility/audio hooks and test keyboard/screen-reader behaviour of interactive material;
- improve publication styling/navigation only after the core build is stable;
- perform final scientific-accuracy, terminology, specification-completeness and originality audits.

## Build verification rule

Distinguish **source written** from **build verified**. The GitHub workflow is in place but the current session has not observed a completed successful Actions run through the connector. If a build reports a PreTeXt/schema error, repair the smallest relevant source/build issue and preserve the established architecture rather than redesigning the project.

## Source hierarchy

The official Junior Cycle Science specification remains the curricular authority. The Junior Cycle Framework, official Science assessment guidance, examples of student work, SEC material and other public official resources provide context and assessment evidence.

Commercial textbooks are private comparison/reference material only for level, examples, vocabulary, practical coverage and omission checks. They are not curricular authorities and their text, distinctive diagrams or questions must not be copied into this public resource.

## Continuity rule

Before substantial work, read:

1. root `README.md`;
2. `PROJECT-STATUS.md`;
3. `NEXT.md`;
4. relevant material under `references/`;
5. `curriculum/` when changing coverage;
6. recent commits and current source tree.

At the end of substantial work, update this status if the state changed materially and append a concise entry to `WORKLOG.md`.
