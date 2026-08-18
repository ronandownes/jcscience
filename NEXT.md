# Next Work

This file is the shared queue for any AI or human contributor. Take coherent non-conflicting batches, commit them, then update this file.

## Priority 1 — make the current book build cleanly

- Run the GitHub Pages workflow or local `pretext build web`.
- Fix any PreTeXt/schema/include errors without changing the established learning architecture.
- Confirm the generated site uses the actual PreTeXt book output rather than a raw/static placeholder.
- Record the successful build commit in `WORKLOG.md`.

## Priority 2 — exact specification map

Create a machine-readable curriculum map connecting every official Junior Cycle Science learning outcome to:

- strand;
- element;
- concept IDs;
- primary book section(s);
- supporting sections;
- investigations;
- formative checks;
- retrieval items;
- exam-style practice.

Use the official specification as the authority. Identify any uncovered or underdeveloped outcomes and create content for them.

## Priority 3 — canonical concept library

Implement the data model in `references/CONCEPT-DATA.md`, initially using YAML or another maintainable machine-readable format.

Start with high-frequency concepts such as:

- observation / inference / hypothesis;
- independent / dependent / control variable;
- reliability / validity;
- speed / force / mass / weight / pressure / energy;
- current / potential difference;
- element / atom / compound / mixture / solution;
- physical change / chemical reaction / conservation of mass;
- acid / base / pH;
- cell / tissue / organ / system;
- respiration / photosynthesis;
- gene / chromosome / variation / natural selection;
- ecosystem / biodiversity;
- weather / climate / greenhouse effect;
- plate / earthquake / rock cycle / orbit / light-year.

Each should support Understand, Exam-ready and Precise wording plus misconceptions and curriculum links.

## Priority 4 — deepen every strand

The existing chapter prose is the first conceptual layer. Expand each section with:

- phenomenon or question opener;
- prerequisite retrieval;
- examples and non-examples;
- native diagrams;
- practical/investigation link;
- embedded formative checks;
- misconception clinic;
- application;
- cross-strand connection;
- original exam-style question;
- later retrieval hook.

Do not inflate prose for its own sake. Coverage should become deeper through representations, examples, evidence and reasoning.

## Priority 5 — exam corpus

Use `tools/fetch_science_papers.py` and official/public sources to establish the examination corpus. Analyse patterns rather than reproducing papers.

Build structured metadata for:

- action verb;
- concept;
- learning outcome;
- representation;
- response depth;
- data handling;
- practical reasoning;
- misconception;
- cognitive demand.

Then author large numbers of genuinely new questions following `references/QUESTION-DESIGN.md`.

## Priority 6 — practical science bank

Build topic-specific practicals and investigations across all strands. Each practical should include, as appropriate:

- question/purpose;
- equipment;
- safety/risk controls;
- variables;
- method;
- data table scaffold;
- expected pattern without pretending all classrooms get identical results;
- analysis questions;
- evaluation prompts;
- extension/adaptation;
- links to Nature of Science.

## Priority 7 — interactive layer

After the basic build is stable, implement reusable interactive components for:

- reveal/hide three reading routes;
- formative multiple-choice checks;
- hints before solutions;
- success/misconception feedback;
- definition views;
- cumulative retrieval;
- text-entry checks where technically robust;
- diagrams/simulations where they add learning value.

Keep graceful fallback for print and accessibility.

## Priority 8 — polish and audit

- specification completeness audit;
- scientific accuracy audit;
- terminology consistency audit;
- accessibility audit;
- question originality/similarity review;
- cross-reference audit;
- mobile/desktop/print testing;
- final navigation and visual design.

## Parallel-work rule

Two contributors may work simultaneously only when their file territories are clearly separated. Do not independently edit the same chapter or core manifest without coordination through the repo.
