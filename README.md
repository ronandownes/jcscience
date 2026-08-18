# JC Science — PreTeXt

An open, expandable Junior Cycle Science learning resource for Ireland, authored in PreTeXt.

## Read this first

This README is the standing project brief and the shared continuity document between AI contributors.

Any AI or contributor working on this repository should read it before creating or changing book content.

## AI continuity protocol

The repository itself is the project memory. The user should not have to act as a middleman between different AI systems.

When a significant project decision is made, the AI working on the repository should write the durable part of that decision back into the repository, normally by updating this README or the relevant file under `references/`.

Do **not** dump raw chat transcripts into the README. Preserve the useful project decisions, rationale, constraints and next direction in concise form.

Before continuing substantial work:

1. read this README;
2. read `references/README.md`;
3. read `references/SOURCES.md` when using external material;
4. read `references/QUESTION-DESIGN.md` when creating assessment questions;
5. inspect the current source tree and recent commits;
6. continue from the current state rather than rebuilding decisions from chat history.

If a new decision materially changes the project direction, update the repository documentation before finishing the work session.

## Current working direction

The project is not intended to be a conventional textbook converted to HTML. It is an interactive science learning environment built around the official specification and the affordances of PreTeXt and the web.

Current priorities are:

- specification-led coverage rather than textbook-led coverage;
- strong, original explanatory writing;
- formative assessment embedded throughout learning;
- immediate and useful feedback rather than end-of-chapter marking only;
- extensive retrieval and cumulative practice;
- exam-standard but genuinely original question banks;
- modular architecture that can expand without major rewrites;
- practical work, scientific reasoning and Nature of Science integrated throughout;
- accessibility, scaffolding and appropriate challenge;
- future support for richer interactions, semantic answer checking, simulations, multilingual content and analytics where worthwhile.

The working reference strategy is **hybrid rather than cloud-only**:

- GitHub contains the authored resource, project instructions, reference catalogue, provenance, manifests and retrieval tools;
- stable official documents can normally be referenced by canonical source URL;
- frequently used public documents and examination papers may be cached locally/private for efficient AI and author use;
- commercial textbooks and commercial examination papers are reference material only and should not be published in the public repository unless redistribution rights are confirmed;
- a cloud-only AI should rely on the repository documentation and accessible reference store rather than requiring the user to repeatedly transfer context manually.

## Source of truth

The **official Junior Cycle Science specification is the only curricular source of truth**.

Two existing Junior Cycle Science textbooks may be supplied separately as reference material. They are useful for checking:

- expected student level;
- common examples and practical work;
- vocabulary;
- typical coverage;
- possible omissions;
- alternative explanations of difficult ideas.

They are **not authorities**. Do not copy or inherit their chapter structure, prose, exercises or sequencing as the design of this book.

The resource must be original and designed from first principles around:

1. the official specification;
2. strong science pedagogy;
3. formative assessment;
4. the possibilities of an interactive digital platform.

The curriculum spine follows the NCCA Junior Cycle Science specification: Nature of Science as the unifying strand, with Earth and Space, Chemical World, Physical World, and Biological World developed through Building Blocks, Systems and Interactions, Energy, and Sustainability.

## Reference hierarchy

Not all reference material has equal authority.

Use this order:

1. official Junior Cycle Science specification and Framework for Junior Cycle;
2. official Science assessment guidance and examples of student work;
3. professional, Inspectorate, SSE, teaching, inclusion and laboratory-safety guidance;
4. SEC/sample/past examination papers as an assessment corpus;
5. commercial textbooks and commercial exam papers as non-authoritative working references.

See `references/SOURCES.md` for the maintained source catalogue.

## Examination corpus

Past papers are evidence about **how science has been assessed**, not a substitute for the specification.

The current working corpus includes:

- Junior Certificate Science Higher and Ordinary papers from 2009–2018;
- current/common-level Science papers from the 2019 onward era where available;
- relevant sample papers;
- later expansion to other useful assessment material where appropriate.

The repository contains `tools/fetch_science_papers.py` to automate acquisition of the public Science paper corpus instead of manually scrolling through archive pages and downloading files one by one.

Use papers to identify:

- action verbs;
- cognitive demand;
- data and graph styles;
- experimental reasoning;
- scientific misconceptions;
- stimulus design;
- expected response depth;
- useful assessment patterns.

Then create new project-authored questions from those patterns.

**Changing only a few numbers or lightly paraphrasing an existing question is not the project standard.**

Use the process in `references/QUESTION-DESIGN.md`: source question → abstract assessment blueprint → source put aside → genuinely new question → similarity review → specification check.

User-facing questions should normally be labelled generically, for example **Exam-style practice**, rather than presented as if they were actual SEC or commercial-paper questions.

## Core design principle

Do not ask:

> How would this appear in a printed textbook?

Ask:

> What is the best way for a student to learn this on an interactive platform?

A useful learning sequence is often:

**Prior knowledge → phenomenon/question → explanation → example → student interaction → formative check → feedback → misconception → retrieval → application → extension**

This is a pedagogical model, not a rigid page template.

## Formative assessment by design

Assessment should happen **during learning**, not only at the end of a chapter.

Use interactive checks wherever they improve learning, including:

- multiple-choice diagnostic questions;
- prediction before explanation or reveal;
- immediate feedback;
- clear success feedback, including green success states where appropriate;
- hints and scaffolds before full answers are revealed;
- misconception questions;
- retrieval of previously learned material;
- short application questions;
- graduated difficulty;
- self-checks throughout sections.

Where useful and technically feasible, go beyond standard textbook interactions. For example, a student might type a definition or short explanation into a text box and receive approximate semantic feedback when the response is sufficiently close in meaning to the target answer.

PreTeXt is the core publishing framework, but additional HTML/CSS/JavaScript or other suitable mechanisms may be used where they provide worthwhile learning functionality and remain maintainable.

## Architecture

Keep the book **modular, expandable and easy to refactor**.

Likely major areas include:

- Nature of Science;
- Biological World;
- Chemical World;
- Physical World;
- Earth and Space;
- investigations and practical work;
- retrieval and assessment.

Do not hard-code a structure that prevents later reorganisation.

Prefer reusable components for:

- definitions and vocabulary;
- worked examples;
- investigations;
- diagrams and representations;
- misconceptions;
- formative questions;
- retrieval practice;
- scaffolding and differentiation;
- extension and challenge.

Cross-reference existing explanations rather than duplicating material unnecessarily.

## Writing standard

The prose must be **clear, accurate, concise and genuinely well written**.

Do not merely paraphrase supplied textbooks.

Explain scientific ideas from first principles in language appropriate to Junior Cycle students while preserving scientific accuracy. Use examples, analogies, diagrams and representations because they improve understanding, not because another textbook uses them.

The finished resource should have its **own voice, structure and pedagogy**.

## Reference textbooks

Reference textbooks are working inputs, not project dependencies or curricular authorities.

Because this repository is public, do **not** commit copyrighted commercial textbook files unless redistribution rights are confirmed. Keep such files in a suitable private working reference store if multiple contributors need access.

The project should remain fully understandable and buildable without those books being stored in the public repository.

## Long-term direction

Design now for later expansion. The project may eventually include:

- simulations;
- interactive diagrams;
- video;
- richer question banks;
- cumulative retrieval;
- adaptive or semantic feedback;
- multilingual support;
- teacher resources;
- accessibility features;
- analytics or other formative-assessment tools.

Avoid decisions that unnecessarily box the project in.

## Build

```bash
python -m pip install "pretext==2.44.0"
pretext build web
```

The HTML output is written to `output/web/`.

## Structure

- `project.ptx` — PreTeXt CLI project manifest
- `source/main.ptx` — book source
- `references/README.md` — reference workflow
- `references/SOURCES.md` — reference hierarchy and source catalogue
- `references/QUESTION-DESIGN.md` — assessment-generation policy
- `tools/fetch_science_papers.py` — automated Science exam-corpus downloader
- `.github/workflows/pages.yml` — builds and deploys the real PreTeXt HTML to GitHub Pages

This repository is deliberately structured so individual topic chapters can be split into separate source files as the book grows.

## Standing instruction for AI contributors

Before continuing work on this repository:

1. read the repository documentation first;
2. check the official Junior Cycle Science specification;
3. inspect the existing project structure and recent work;
4. preserve working features unless there is a clear reason to change them;
5. build in small, maintainable increments;
6. keep specification alignment explicit;
7. prefer learning value over imitation of print textbooks;
8. write durable project decisions back into the repository;
9. leave the project in a state another contributor can understand and continue without requiring the user to manually relay context.

**Specification-led. Pedagogy-led. Original. Modular. Interactive. Formative by design. Expandable.**
