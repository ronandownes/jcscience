# Project Decisions

This file records durable implementation decisions that should survive chat boundaries.

## 2026-08-18 — repository as shared project memory

The GitHub repository is the communication layer between AI contributors. Significant work must leave the repo understandable and resumable without the user manually relaying context.

Read the root README, status/next files and relevant `references/` material before substantial changes. Record durable decisions here or in the more specific reference document.

## 2026-08-18 — specification-led, not textbook-led

The official Junior Cycle Science specification is the curricular authority. The Junior Cycle Framework, official Science assessment material and SEC papers provide context and assessment evidence.

Commercial textbooks are comparison/reference inputs only. They may inform checks for expected learner level, common examples, practical coverage, vocabulary and possible omissions, but the project must not copy their prose, questions, distinctive diagrams or chapter architecture.

## 2026-08-18 — three reading routes

Substantial explanatory sections should support three routes where they genuinely add value:

- **Read less** — reduce linguistic load while preserving the scientific destination;
- **Standard** — complete high-quality Junior Cycle explanation;
- **Go deeper** — increase precision, mechanism, qualification, connection and transfer.

These are reading routes, not student ability labels. A learner may combine low reading load with high challenge.

## 2026-08-18 — modular strand source files

The initial PreTeXt book uses separate source files for:

- Nature of Science;
- Physical World;
- Chemical World;
- Biological World;
- Earth and Space;
- Investigations and Practical Science;
- Retrieval, Mixed Practice and Assessment.

This is a maintainability choice, not a commitment that the final learner navigation must mirror printed strand silos. Cross-strand pathways and later reorganisation remain possible.

## 2026-08-18 — native production content

Production content should be native PreTeXt/HTML/data wherever practical. Reference PDFs, screenshots and papers are inputs for analysis, not page assets to be reproduced.

Prefer project-created diagrams, structured questions, accessible tables and reusable concept data.

## 2026-08-18 — canonical concept architecture

Important definitions and concepts should eventually be stored as maintained structured objects following `references/CONCEPT-DATA.md` so chapters, glossary, feedback, revision cards, audio and later subject projects do not drift into competing definitions.

## 2026-08-18 — assessment corpus as patterns

Past-paper material is an assessment dataset. Extract concepts, action verbs, representations, reasoning demands and misconceptions, then create genuinely new questions. Do not generate near-copies by changing names or numbers.

## 2026-08-18 — PreTeXt build and deployment

Use PreTeXt CLI 2.44.0 for the current reproducible build. The `web` target builds `source/main.ptx` into `output/web`. GitHub Pages deployment uses a custom GitHub Actions workflow and the repository Pages source should be set to GitHub Actions.

This version pin may be deliberately upgraded later after a tested migration.
