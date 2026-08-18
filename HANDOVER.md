# Handover and Coordination

This file is the live coordination point for any AI or contributor working on the JC Science project.

## Read before working

1. Read the root `README.md`.
2. Read all standing files under `references/`, especially `LEARNING-ARCHITECTURE.md`, `CONCEPT-DATA.md`, `LEARNING-DESIGN.md`, `QUESTION-DESIGN.md`, and `SOURCES.md`.
3. Inspect the current repository tree and recent commits before changing anything.
4. Treat the repository as the project memory and source of truth.

## Multi-AI rule

Different ChatGPT sessions/accounts cannot communicate directly. They coordinate only through the repository.

Before starting substantial work, read this file and the latest repository state. Before stopping, update this file and any relevant standing documentation so another AI can continue without the user having to relay context manually.

Avoid two AIs editing the same files simultaneously. Parallel work is acceptable only when responsibilities are clearly separated by file, chapter, branch, or task. If in doubt, work sequentially.

## End-of-session requirement

Every substantial work session must leave the repository fully self-describing:

- commit completed work;
- record any durable design decisions in the appropriate standing document;
- update the current state below;
- state what is complete, what is incomplete, and the best next step;
- note any external/private reference material that was used but is not stored in the repo;
- do not leave important decisions only in chat history.

## Current state

The project architecture and reference policy are documented. The repository contains the project brief, learning architecture, concept-data policy, learning/assessment design, question-design policy, source hierarchy, and the Science-paper acquisition script.

Commercial reference textbooks are not stored in this public repository. Two 150-page textbook extracts are available in one ChatGPT account's Library as comparative reference material only; they are not curricular or definitional authorities.

The NUIM/Maynooth State Exam Papers archive is documented in `references/SOURCES.md`. Current-era papers, the 2009–2018 Higher/Ordinary corpus, and selectively useful older questions are treated as assessment evidence, always filtered against the current specification.

## Next direction

Before large-scale chapter authoring, establish or verify a minimal compiling PreTeXt project skeleton and ensure the root README accurately reflects the files that actually exist. Then begin specification-led production content using the documented learning architecture and canonical concept system.

If compute is constrained, complete a coherent batch of work and leave a precise continuation note here. If compute is not constrained, continue as far as useful while preserving modularity and updating the repository continuously.
