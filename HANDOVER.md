# Handover and Coordination

This file is the live coordination point for any AI or contributor working on the JC Science project.

## Read before working

1. Read the root `README.md`.
2. Read `PROJECT-STATUS.md`, `NEXT.md`, `DECISIONS.md` and `WORKLOG.md`.
3. Read all standing files under `references/`, especially `LEARNING-ARCHITECTURE.md`, `CONCEPT-DATA.md`, `LEARNING-DESIGN.md`, `QUESTION-DESIGN.md`, and `SOURCES.md`.
4. Inspect `curriculum/`, the current source tree and recent commits before changing anything.
5. Treat the repository as the project memory and source of truth.

## Multi-AI rule

Different ChatGPT sessions/accounts cannot communicate directly. They coordinate only through the repository.

Before starting substantial work, read this file and the latest repository state. Before stopping, update this file and any relevant standing documentation so another AI can continue without the user having to relay context manually.

Avoid two AIs editing the same files simultaneously. Parallel work is acceptable only when responsibilities are clearly separated by file, chapter, branch or task. If in doubt, work sequentially.

## End-of-session requirement

Every substantial work session must leave the repository fully self-describing:

- commit completed work;
- record durable design decisions;
- update current state;
- state what is complete, what is incomplete and the best next step;
- note external/private reference material used but not stored publicly;
- do not leave important decisions only in chat history.

## Current state — 2026-08-18

The project has moved far beyond the earlier documentation-only state. It now contains a substantial modular PreTeXt textbook source plus build, curriculum, concept-data and assessment infrastructure.

### PreTeXt and deployment

- `project.ptx` is a PreTeXt CLI v2 manifest.
- `source/main.ptx` includes the full current book source.
- `.github/workflows/pages.yml` checks source, installs pinned PreTeXt 2.44.0, builds the web target and deploys `output/web` to GitHub Pages.
- `tools/check_source.py` checks malformed XML, missing includes and duplicate `xml:id` values before the full PreTeXt build.
- A successful end-to-end GitHub Actions build still needs to be observed and any concrete schema/build errors repaired.

### Authored textbook source

Current production chapters include:

- Nature of Science;
- Science, Technology and Society;
- Physical World;
- Measuring the Physical World;
- Chemical World;
- Chemical Patterns, Rates and Energy;
- Biological World;
- Health, Reproduction and Human Biology;
- Earth and Space;
- Cosmos, Carbon and Earth's Energy Future;
- Investigations and Practical Science;
- Practical Science Bank;
- Interactive Diagnostic Checks;
- Retrieval, Mixed Practice and Assessment.

Substantial explanatory sections use the established three-route system:

**Read less → Standard → Go deeper**

These are independent reading-depth routes, not ability labels.

### Specification/framework layer

- `curriculum/learning-outcomes.yml` maps every official Junior Cycle Science outcome to current source and records coverage status/gaps.
- `curriculum/JUNIOR-CYCLE-FRAMEWORK.md` records project implications of outcomes-based Junior Cycle, common-level Science, key skills, Statements of Learning, literacy/numeracy, inclusion and assessment.
- The official specification remains the curricular authority.

### Concept layer

- `data/concepts/core.yml` seeds canonical project-owned concept records with Understand / Exam-ready / Precise wording, units/relationships and misconceptions where appropriate.
- These records are still draft until formally reviewed and wired into generated chapter/glossary views.

### Assessment/practical layer

The current source includes original structured exercises, mixed retrieval, cross-strand application, misconception clinics, exam-style practice and native PreTeXt interactive true/false and multiple-choice questions with feedback.

`source/practicals.ptx` contains a substantial cross-strand bank including density, motion, circuits/resistance, insulation, reflection, conservation of mass, separation, reaction rates, acids/bases, reaction energy, microscopy, photosynthesis, respiration, habitat study, climate-data work and Earth-Sun-Moon modelling.

`tools/fetch_science_papers.py` remains the acquisition tool for the public Maynooth/NUIM Science paper corpus. Past papers are assessment-pattern data, not curricular authority.

### External/private reference material

Commercial reference textbooks are not stored in this public repository. Two roughly 150-page textbook extracts are available in a ChatGPT Library as comparative reference material only; they must not be copied or treated as authorities.

Public official material — specification, Junior Cycle Framework, assessment guidance, examples/sample material and examination resources — should be obtained directly from authoritative public sources as required. The user does not need to manually supply these.

## Best next steps

1. Observe/run the GitHub Pages Action and fix only concrete PreTeXt/schema/build issues until the real web book is green.
2. Refresh `curriculum/learning-outcomes.yml` because many gaps listed in the first mapping have since been filled by new chapters.
3. Complete a systematic specification audit so every outcome has explanation, investigation/formative evidence and assessment coverage.
4. Expand the native diagram/representation layer.
5. Analyse the public examination corpus as structured assessment patterns and create a much larger original metadata-rich question bank.
6. Review canonical concepts and begin rendering definitions/glossary/feedback from one maintained data source.
7. Continue deepening chapters with examples, non-examples, embedded checks, cross-strand links and cumulative retrieval.

Do not redesign the project from scratch. Continue the established specification-led, original, modular, interactive and formative architecture.
