# JC Science Project Status

_Last updated: 2026-08-18_

## Current state

The repository now contains a working modular PreTeXt source architecture rather than documentation only.

### Build infrastructure

- `project.ptx` — PreTeXt CLI v2 manifest for the `web` target.
- `source/main.ptx` — book entry point.
- `.github/workflows/pages.yml` — builds the book with PreTeXt 2.44.0 and deploys `output/web` through GitHub Pages.
- GitHub Pages must use **GitHub Actions** as its publishing source for deployment to succeed.

### Book source now present

- `source/nature-of-science.ptx`
- `source/physical-world.ptx`
- `source/chemical-world.ptx`
- `source/biological-world.ptx`
- `source/earth-space.ptx`
- `source/investigations.ptx`
- `source/retrieval-assessment.ptx`

The first production pass establishes broad curricular coverage and implements the project's three reading routes throughout substantial sections:

- **Read less** — reduced reading load without reduced scientific destination;
- **Standard** — complete Junior Cycle explanation;
- **Go deeper** — greater precision, mechanism, qualification and transfer.

The chapters are intentionally original and specification-led. They are not transcriptions or structural imitations of commercial textbooks.

## Important limitation of the current pass

This is a substantial first authored layer, **not yet the finished textbook**.

The present source establishes the conceptual spine and prose architecture. It still needs:

- exact learning-outcome mapping for every section;
- canonical concept records feeding definitions and glossary views;
- substantially more examples and non-examples;
- diagrams, photographs and interactive representations;
- practical protocols tied to individual topics;
- more formative questions inside sections rather than mostly at the mixed-practice layer;
- misconception-specific feedback;
- cumulative retrieval schedules;
- large original exam-style question bank informed by the past-paper corpus;
- assessment metadata;
- explicit CBA/project pathways and exemplars;
- accessibility/audio hooks;
- richer navigation and styling once the core build is stable;
- final factual and curricular audit against current official documentation.

## Build verification

The GitHub workflow has been added, but each contributor must distinguish **source written** from **build verified**. If the workflow reports a PreTeXt/schema error, repair the smallest relevant source/build issue and preserve the architecture rather than redesigning the project.

## Source hierarchy

The official Junior Cycle Science specification remains the curricular authority. The Junior Cycle Framework, official assessment guidance, SEC material and other public official resources provide context and assessment evidence.

Commercial textbooks may be used privately as comparison/reference material for expected learner level, vocabulary, examples, practical coverage and omission checks. They are not curricular authorities and must not be copied into the public book.

## Continuity rule

Before substantial work, read:

1. root `README.md`;
2. `PROJECT-STATUS.md`;
3. `NEXT.md`;
4. all files under `references/` relevant to the task;
5. recent commits and current source tree.

At the end of substantial work, update this status if the state changed materially and append a concise entry to `WORKLOG.md`.
