# Reference Material

This directory contains the standing reference policy for development of the JC Science PreTeXt resource.

Read these files before using external material or creating substantial book content:

- `LEARNING-ARCHITECTURE.md` — canonical learning architecture, definition policy, reading routes, terminology rigor, single-source concept model and subject-transfer rules.
- `LEARNING-DESIGN.md` — production-content, mastery, formative/exam-mode and CBA/project strategy.
- `SOURCES.md` — authority hierarchy and reference library.
- `QUESTION-DESIGN.md` — how past papers and commercial assessment material may inform genuinely new project questions.

## Core rules

- The official Junior Cycle Science specification remains the only curricular source of truth.
- The academic architecture is defined in `LEARNING-ARCHITECTURE.md`: keep intellectual demand rigorous while varying reading load, representation, scaffolding, pace and challenge.
- Important definitions and concepts should be project-owned canonical objects rather than copied textbook wording. Commercial textbook definitions are comparison material, not authority.
- Distinguish explicitly among definitions, quantities, units, conventions, laws, models, theories, principles, derived relationships, observations, inferences and hypotheses where relevant.
- Keep a single source of truth for important terminology, symbols, units and canonical definitions wherever technically practical, then reuse those objects across chapters, glossaries, revision, feedback and accessibility views.
- Official assessment and professional guidance inform assessment, pedagogy, planning and safety but do not replace the specification.
- Past papers are an **assessment corpus**, not a curriculum.
- Commercial textbooks are reference inputs only: use them to check level, coverage, examples, vocabulary and possible omissions.
- Commercial exam papers may be analysed privately for assessment patterns but should not be superficially rewritten or published without appropriate rights.
- Do not copy textbook prose, exercises, chapter structures, illustrations or distinctive presentation.
- Build the new resource independently from the specification and strong pedagogy.
- Prefer interactive formative assessment and other digital affordances where they improve learning.

## Recommended working model — hybrid, not cloud-only

Keep **provenance and instructions in GitHub**, and keep a **local/private cache of frequently used reference binaries**.

That means:

- GitHub always contains `SOURCES.md`, source URLs, retrieval scripts, provenance and project policy;
- stable official documents may simply be referenced by canonical URL;
- frequently used papers/documents can be downloaded into a working reference cache;
- commercial textbooks and commercial examination papers belong in a private working store unless redistribution rights are confirmed;
- the public PreTeXt repository should remain primarily the authored resource and its reproducible tooling, rather than becoming an uncontrolled PDF archive.

`.gitignore` only controls whether Git tracks a local file. It does **not** prevent a local writer or AI process from reading that file. A cloud-only agent that can see only GitHub will not see an ignored local file; if several cloud agents genuinely need the same restricted reference binaries, use a separate private shared reference store/repository.

## Science examination corpus

A reproducible downloader is tracked at:

`tools/fetch_science_papers.py`

From the repository root, install its small dependencies and run:

```bash
python -m pip install requests beautifulsoup4
python tools/fetch_science_papers.py
```

This discovers and downloads the current target Science corpus from the Maynooth University State Exam Papers archive into:

`references/exams/sec/`

It also creates a `manifest.json` recording the source URL and SHA-256 hash of each downloaded file.

Use:

```bash
python tools/fetch_science_papers.py --list-only
```

to inspect what would be fetched without downloading anything.

## Local source area

The previously inventoried science material is under:

`E:\Projects\Publishing\pdfhub`

The inventory includes `jc01scienceer.pdf`, and science material also appears under:

`E:\Projects\Publishing\sections\rwp`

## Repository/publication rule

The main repository is currently public. Do not commit copyrighted commercial textbook or commercial exam-paper PDFs here unless redistribution rights are confirmed.

If the project requires AI contributors to share commercial reference files, use a **separate private reference store/repository** rather than relying on `.gitignore` or planning to delete the files later. Deleting a tracked file does not by itself remove it from Git history.

Stable official documents can normally remain as canonical source links in `SOURCES.md`; mirror a binary copy only when there is a clear workflow reason and the redistribution position is suitable.
