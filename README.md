# JC Science — PreTeXt

An open, expandable Junior Cycle Science learning resource for Ireland, authored in PreTeXt.

## Read this first

This README is the standing project brief.

Any AI or contributor working on this repository should read it before creating or changing book content.

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

Reference textbooks are working inputs, not project dependencies.

Because this repository is public, do **not** commit copyrighted commercial textbook files unless redistribution rights are confirmed. Keep such files outside the public repository and remove temporary copies when no longer needed.

The project should remain fully understandable and buildable without those books being stored here.

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
- `.github/workflows/pages.yml` — builds and deploys the real PreTeXt HTML to GitHub Pages

This repository is deliberately structured so individual topic chapters can be split into separate source files as the book grows.

## Standing instruction for AI contributors

Before continuing work on this repository:

1. read this README;
2. check the official Junior Cycle Science specification;
3. inspect the existing project structure and recent work;
4. preserve working features unless there is a clear reason to change them;
5. build in small, maintainable increments;
6. keep specification alignment explicit;
7. prefer learning value over imitation of print textbooks;
8. leave the project in a state another contributor can understand and continue.

**Specification-led. Pedagogy-led. Original. Modular. Interactive. Formative by design. Expandable.**
