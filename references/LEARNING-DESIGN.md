# Learning and Assessment Design Strategy

This document defines how the JC Science project should turn specifications, professional guidance, past papers and other references into an original, high-quality interactive learning resource.

## Outcome standard

The resource should be sufficiently complete and demanding that a diligent, capable student can prepare for the highest level of Junior Cycle Science performance **without needing another textbook to fill curricular or practice gaps**.

No resource can guarantee an examination result. The design goal is to remove avoidable resource limitations: missing specification coverage, weak explanations, insufficient practice, poor feedback, shallow retrieval, lack of unfamiliar-context questions, or inadequate support for scientific investigation and project work.

## Do not build pages from screenshots

Production content should be native wherever reasonably possible.

Avoid workflows based on repeated cutting, pasting, screenshots, JPEGs or PNGs of textbook/exam content. These are acceptable as temporary reference material during analysis, but they should not become the authored book.

Prefer:

- native PreTeXt text and mathematics;
- native tables;
- structured question source;
- accessible HTML controls;
- reproducible vector diagrams where practical;
- project-created figures and datasets;
- reusable assets rather than page screenshots.

Benefits include responsive layout, accessibility, searchability, translation, restyling, print output, question reuse, automated feedback and easier future editing.

## Reference-ingest workflow

Keep frequently used source documents in a local/private reference cache, with GitHub holding the catalogue, provenance and tooling.

For each useful source:

1. record source/title/date/status in the reference catalogue or manifest;
2. extract the information needed for analysis;
3. identify curriculum, pedagogy or assessment patterns;
4. convert those patterns into structured project knowledge;
5. author new content natively;
6. keep source material separate from production content.

The purpose is not to typeset an old paper into PreTeXt. It is to make old papers computationally useful as an assessment corpus.

## Question architecture

Every substantial question should be capable of carrying internal metadata such as:

- learning outcome(s);
- strand / element;
- concept;
- action verb;
- question type;
- difficulty;
- cognitive demand;
- prerequisite knowledge;
- misconception targeted;
- representation: text / graph / table / diagram / calculation / investigation;
- expected response form;
- mark-equivalent or expected response depth;
- provenance category;
- accessibility notes;
- feedback / hint path.

This enables the same underlying bank to support teaching, retrieval, end-of-section practice, mixed revision and exam-mode assessments.

## Mastery ladder

Do not treat success as memorising definitions followed by one end-of-chapter exercise.

For each important learning outcome, aim to provide progression through several demands:

1. **Recognise / recall** — terminology, facts, representations.
2. **Explain** — articulate the scientific idea accurately.
3. **Apply** — use it in a familiar context.
4. **Interpret** — work with tables, graphs, diagrams, observations or evidence.
5. **Investigate** — variables, fair testing, measurement, reliability, evaluation and scientific method.
6. **Transfer** — solve a new or unfamiliar-context problem.
7. **Connect** — combine learning across topics/strands and Nature of Science.

Not every outcome needs identical numbers of questions at every stage, but the overall book should deliberately develop this progression.

## Formative mode and exam mode

The same resource should support two deliberately different experiences.

### Learning / formative mode

Use:

- immediate feedback;
- green success states where appropriate;
- hints;
- scaffolds;
- worked reasoning after attempts;
- misconception-specific feedback;
- multiple attempts;
- retrieval prompts;
- short semantic/free-text checks where technically reliable.

The student should learn **while answering**.

### Exam mode

Later practice should progressively remove support:

- no immediate answer reveal;
- no hints unless requested after completion;
- mixed topics and strands;
- unfamiliar contexts;
- realistic response depth;
- timed or untimed options;
- marking guidance / model response available after submission;
- cumulative practice rather than chapter-isolated practice only.

The student should eventually be able to perform without the scaffolds that helped build the learning.

## Exam corpus strategy

Past SEC, sample and other assessment material should be treated as a dataset of assessment patterns.

Do **not** spend large amounts of authoring time recreating old paper typography or page layout.

Instead extract:

- what concept was assessed;
- how the question was framed;
- the command verb;
- the representation used;
- the reasoning required;
- likely distractors/misconceptions;
- how subparts increased in demand;
- what a strong response needed to contain.

Then generate and review original questions from that blueprint.

See `QUESTION-DESIGN.md` for the originality and similarity policy.

## Diagrams and figures

Do not automatically crop figures from old papers.

Use this priority order:

1. project-created native/vector diagram;
2. openly licensed or public-domain figure with recorded attribution where suitable;
3. newly generated or redrawn schematic based on the scientific concept, not the distinctive appearance of a source figure;
4. raster image only when it is genuinely the best representation (for example a photograph or microscopic image).

A diagram should remain legible on phone, desktop and print output and should include appropriate alternative text or equivalent description.

## CBA and project-based learning layer

The project should not assume that every learner will receive equally strong classroom scaffolding for open-ended investigation or project work.

Build explicit support into the resource so that scientific inquiry becomes teachable and learnable rather than an instruction to simply 'do a project'.

Develop reusable student supports for:

- choosing/refining a research question;
- distinguishing investigable from non-investigable questions;
- background research and source quality;
- hypothesis/prediction where appropriate;
- independent/dependent/control variables;
- planning a fair and safe investigation;
- measurement and data collection;
- tables, graphs and suitable representations;
- patterns, anomalies and uncertainty;
- drawing evidence-based conclusions;
- evaluating limitations and improvements;
- distinguishing evidence from assertion;
- citing sources and avoiding plagiarism;
- reflection on the process;
- communicating findings clearly.

Include worked and partially worked examples, checkpoints and exemplars. Gradually fade support so the student develops independence.

The goal is to reduce dependence on variable levels of teacher expertise while still supporting, rather than replacing, good classroom teaching.

## CBA/project workflow concept

A future interactive project workspace could guide a student through:

**Question → research → plan → safety → method → evidence → analyse → conclude → evaluate → communicate → reflect**

At each stage the system can provide prompts and formative checks without writing the project for the student.

This can later be extended with teacher-facing guidance, exemplars, rubrics/checklists, milestone views and links back to the exact science concepts needed for the student's investigation.

## Quality-control gate

Before a substantial section is considered complete, check:

- specification coverage is explicit;
- explanations are scientifically accurate and age-appropriate;
- vocabulary is taught rather than assumed;
- required practical/investigative thinking is represented;
- formative checks occur during learning;
- misconceptions are anticipated;
- retrieval reaches back beyond the current subsection;
- students get application and unfamiliar-context practice;
- exam-style questions are original and current-specification aligned;
- answers/feedback explain why, not merely what;
- diagrams are legible and accessible;
- content works digitally and remains printable where print is valuable;
- no production content depends on an inaccessible commercial reference file.

## Strategic principle

**Use documents and papers as data. Build the learning experience natively.**

The project should eventually know far more about each question and learning outcome than a conventional printed textbook can encode, allowing better feedback, retrieval, adaptation, revision and project support without sacrificing rigorous scientific content.
