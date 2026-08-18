# Learning Architecture

This document defines the reusable academic and pedagogical architecture for the JC Science resource. It is intended to transfer to later subject projects such as Mathematics, Applied Mathematics, Physics and Computer Science.

The project should not behave like a printed textbook placed on a screen. It should behave like a structured learning system in which the scientific content is rigorous, the language is age-appropriate, the supports are optional, and the student can move between representations, levels of explanation, practice and challenge without being labelled.

## Core principle

**Keep the intellectual destination rigorous; vary the route to it.**

Do not classify students by fixed ability level. Do not create a permanent “easy”, “ordinary” or “advanced” version of the learner.

Instead, allow independent variation in:

- reading load;
- explanation depth;
- vocabulary support;
- representation;
- scaffolding;
- pace;
- practice volume;
- cognitive demand;
- degree of independence;
- assessment support.

A student may need low reading load and high scientific challenge at the same time. These are separate dimensions.

## Reading routes

Where worthwhile, substantial explanatory content should support three reading routes.

### Read less

Reduce unnecessary linguistic load while preserving the scientific idea and required conditions.

Use:

- shorter paragraphs;
- one main idea at a time;
- explicit sentence structure;
- key vocabulary introduced before it becomes a barrier;
- diagrams and representations that carry genuine explanatory work;
- examples and non-examples;
- optional audio/read-aloud;
- expandable detail rather than compulsory continuous prose.

“Read less” must never mean “learn less science”.

### Standard

Provide the normal complete explanation expected of a high-quality Junior Cycle science resource.

The prose should be clear, economical, accurate and coherent. Avoid unnecessary density, decorative complexity and textbook filler.

### Go deeper

Extend the same concept through greater precision, mechanisms, qualifications, connections, unfamiliar applications, quantitative reasoning, historical context where useful, and links to later study.

Depth should increase intellectual demand rather than merely adding more words.

## Definition architecture

Definitions are canonical academic objects, not decorative highlighted sentences.

Do not copy a definition from a commercial textbook merely because it appears in a coloured box. A textbook definition may be incomplete, vague, circular, over-specific, scientifically weak or pedagogically poor.

For important terms, create a project-owned canonical definition after checking the underlying science against authoritative sources.

Where useful, expose three views of the same concept:

### Understand

A student-friendly explanation that establishes meaning and distinguishes the idea from nearby concepts.

It may be longer than the exam-ready form if extra words make the meaning clearer.

### Exam-ready

A concise formulation containing the scientific elements a student must be able to communicate accurately in assessment.

It should be memorable without becoming scientifically false through over-compression.

### Precise

A more rigorous formulation including necessary conditions, qualifications, symbols, units, conventions or distinctions where appropriate.

The precise version is not automatically intended for rote memorisation. Its purpose is to show what the concept actually means and where simplified classroom language has limits.

A learner using “Read less” must still be able to choose the precise definition.

## What counts as a definition

Teach students that not every important scientific statement is the same kind of statement.

The project should identify, where relevant, whether an item is a:

- **definition** — fixes the meaning of a term within the course or discipline;
- **primitive or assumed term** — used without a full reduction to earlier terms at the present level;
- **quantity** — a measurable property with an agreed meaning;
- **unit** — an agreed standard used to express a quantity;
- **symbol** — notation representing a quantity, object or relationship;
- **convention** — an agreed choice of representation or sign that could have been chosen differently;
- **empirical law** — a compact description of a regularity supported by observation or experiment;
- **model** — a representation used to explain, predict or reason about a system;
- **theory** — a well-supported explanatory framework;
- **principle** — a broad scientific rule or organising statement;
- **derived relationship** — follows from definitions, models, laws or previously established relationships;
- **approximation** — a deliberately simplified relationship valid under stated conditions;
- **observation** — what is measured or noticed;
- **inference** — an interpretation drawn from evidence;
- **hypothesis** — a proposed, testable explanatory or predictive statement in a given investigation context.

Do not force all science into the structure of formal mathematics. Science contains empirical knowledge, model-dependent knowledge and conventions as well as definitions and deductions. The academic discipline comes from being explicit about which kind of claim is being made.

## Definition quality gate

Before accepting a canonical definition, ask:

1. What exactly is being defined?
2. Is the definition circular?
3. Does it accidentally include things that should be excluded?
4. Does it accidentally exclude valid cases?
5. Are necessary conditions missing?
6. Is a convention being presented as a fact of nature?
7. Is a model being presented as literal reality?
8. Is the wording more complex than the idea requires?
9. Is the wording simpler only because scientific precision has been removed?
10. Could the student use this definition consistently in explanation, problem solving and assessment?

If the answer is weak, rewrite the definition from first principles rather than inheriting source wording.

## Single source of truth for concepts

Important concepts should exist once as canonical structured data wherever technically practical.

A canonical concept record may contain:

- stable concept ID;
- preferred term;
- aliases and common alternative terms;
- concept type (definition, quantity, model, law, convention, etc.);
- Understand wording;
- Exam-ready wording;
- Precise wording;
- symbols;
- SI or other relevant units;
- prerequisites;
- related concepts;
- examples;
- non-examples;
- common misconceptions;
- representations;
- pronunciation/audio metadata;
- accessibility notes;
- specification links;
- assessment notes;
- provenance / authoritative references.

Front-end pages, glossaries, revision cards, quizzes, teacher notes, multilingual layers and later subject books should pull from that source rather than silently maintaining conflicting copies.

If wording must differ for a particular context, the variation should reference the canonical concept and have an explicit reason.

## Explanations are not definitions

A definition should not be expected to do all teaching.

For each major concept distinguish:

**What it is → Why it matters → How it behaves → How we know → How to recognise/use it → What it is not.**

A short definition can be rigorous while the explanatory teaching around it is rich and accessible.

## Multiple representations

Use multiple representations when they reveal structure, not as decoration.

Depending on the concept, the learner may move among:

- plain language;
- technical language;
- photograph;
- diagram;
- labelled schematic;
- animation;
- simulation;
- table;
- graph;
- symbolic relationship;
- numerical example;
- physical demonstration;
- concrete model;
- student-built physical model.

The resource should explicitly connect representations. Recognition of several pictures is not enough; the learning often lies in moving between them.

## Physical modelling

Digital delivery does not imply digital-only learning.

Where real objects are pedagogically superior, instruct the learner to use them: laboratory apparatus, cubes, counters, cards, string, elastic bands, magnets, measuring devices, household objects or construction materials.

A digital simulation can supplement a physical model but should not automatically replace it.

The learning sequence may deliberately move:

**physical/concrete → visual/diagrammatic → verbal → numerical/symbolic**

when that sequence supports understanding.

## Learning sequence

A useful adaptable sequence is:

**Activate → See/experience → Explain → Model → Guided attempt → Check → Adapt → Independent attempt → Apply → Reason → Transfer → Retrieve later.**

This reflects the project’s teaching principles:

- establish prior knowledge;
- make the learning intention clear;
- explain and model explicitly when needed;
- scaffold access without removing the thinking;
- use formative assessment during learning;
- respond to evidence;
- fade support;
- consolidate and retrieve over time;
- increase depth and transfer.

This is a design grammar, not a rigid template that every page must visibly follow.

## Support architecture

Supports should be optional and fadeable.

Possible supports include:

- vocabulary pre-teach;
- read-aloud;
- chunked instructions;
- visual cue;
- worked example;
- partly completed example;
- sentence stem;
- prompt hierarchy;
- hint;
- alternate representation;
- prerequisite refresher;
- model answer after an attempt;
- error-specific feedback.

The system should avoid making the most supported view the permanent identity of the learner.

## Challenge architecture

Challenge means greater depth, reasoning and transfer, not simply more questions.

Increase challenge through:

- explaining why;
- comparing models or methods;
- identifying assumptions;
- designing an investigation;
- evaluating evidence;
- unfamiliar contexts;
- connecting topics;
- generalising patterns;
- quantitative analysis;
- critiquing claims;
- resolving apparent contradictions;
- explaining limits of a model or approximation.

## Learning to learn science

The book should explicitly teach students how the learning system works.

Students should understand ideas such as:

- understanding is not the same as recognising a sentence;
- a definition fixes meaning but does not replace explanation;
- retrieval strengthens access to previously learned knowledge;
- worked examples are temporary supports, not substitutes for independent work;
- errors and misconceptions are evidence about what to do next;
- diagrams, words, equations and physical models are different representations of related ideas;
- revision means revisiting and strengthening learning, not merely rereading;
- reviewing an investigation does not require inventing a mistake;
- changing a method after examining evidence is part of scientific work;
- asking for a scaffold is a learning decision, not an ability label;
- useful support should reduce as independence grows.

Occasional student-facing “How learning works here” notes can make this explicit without turning every chapter into a pedagogy lecture.

## Project and investigation progression

From first year onward, build the habits needed for CBAs and later senior-cycle additional assessment.

Use a recurring progression:

**Question → Research → Plan → Safety → Investigate → Record → Analyse → Conclude → Review/refine → Communicate → Reflect.**

Teach the transferable skills continuously rather than introducing project literacy suddenly when a formal CBA begins.

Keep current administrative CBA rules separate from permanent project skills so changing regulations do not obsolete core learning content.

## Review and refinement

Teach students that review is an evidential process.

A review may lead to a change, but it may also justify retaining the original decision.

Valid outcomes include:

- repeat a measurement;
- change a range or interval;
- improve control of a variable;
- choose a better graph;
- rewrite an ambiguous question;
- retain the original method because evidence supports it;
- identify a limitation that cannot reasonably be removed;
- distinguish random variation from a systematic problem.

Never force students to invent a defect merely to satisfy a reflection box.

## Formative, practice and exam modes

The same underlying content and question bank should support different modes.

### Learn

- immediate feedback;
- hints;
- optional scaffolds;
- representation changes;
- misconception feedback;
- multiple attempts;
- worked reasoning after an attempt.

### Practice

- fewer automatic supports;
- retrieval and spacing;
- mixed examples;
- increasing independence;
- feedback after commitment.

### Exam

- no automatic hints or answer reveals;
- mixed and unfamiliar contexts;
- realistic response demands;
- timed or untimed options where useful;
- marking guidance only after completion.

Support should therefore be built to fade by design.

## Language policy

Use age-appropriate language without becoming academically vague.

Prefer:

- short, direct sentences where they improve clarity;
- technical words when the technical word is the concept students need;
- explicit teaching of those words rather than avoiding them;
- consistent terminology across chapters;
- a clear distinction between everyday and scientific meanings;
- controlled use of synonyms when synonymy could confuse a novice;
- examples and non-examples for boundary cases.

Avoid:

- unnecessary jargon;
- anthropomorphic explanations that become misconceptions;
- definitions built from undefined equally difficult words when a clearer route exists;
- “sort of”, “basically” and other softeners inside canonical statements unless the uncertainty is scientifically real;
- presenting mnemonics or shortcuts as explanations;
- inconsistent renaming of the same concept for variety.

## Source policy for definitions and concepts

Commercial textbooks are comparison material, not definitional authorities.

Wikipedia may be useful as a navigation or checking aid but should not be treated as the canonical authority merely because it is convenient.

For important scientific concepts, prefer triangulation from suitable authoritative sources such as:

- official curriculum/specification documents for required scope and terminology;
- established scientific bodies and standards organisations;
- SI/BIPM material for quantities and units;
- IUPAC for chemistry terminology where age-appropriate;
- reputable scientific reference works and university-level sources where necessary to resolve precision;
- accepted disciplinary conventions.

Then write the project’s own age-appropriate canonical wording.

Record provenance for claims where future review may matter.

## Consistency rule

Once a canonical term or definition is accepted, use it consistently across the resource unless there is a documented pedagogical reason to vary it.

A later improvement should update the canonical source and propagate, rather than creating a second unofficial wording elsewhere.

Consistency is especially important for:

- definitions;
- symbols;
- units;
- graph conventions;
- variable language;
- investigation terminology;
- command verbs;
- safety terminology;
- assessment vocabulary.

## Transfer to other subjects

This architecture is deliberately subject-transferable.

A later Mathematics or Applied Mathematics project should inherit the same high-level rules while using a more formal distinction among:

- primitive terms;
- definitions;
- axioms/assumptions where relevant;
- theorems;
- derived results;
- conventions;
- examples and counterexamples.

Science will retain its own epistemic structure: empirical evidence, models, theories, laws, measurement uncertainty and revision in light of evidence.

The shared principle is the same:

**be explicit about what kind of knowledge claim is being made, define what can be defined consistently, and never trade rigor for superficial simplicity.**

## Implementation direction

As the PreTeXt project grows, prefer machine-readable canonical concept data rather than duplicated prose blocks.

The exact implementation may evolve, but the architecture should make it possible for one concept record to feed:

- chapter explanations;
- pop-up definitions;
- glossary entries;
- revision cards;
- question feedback;
- accessibility views;
- audio;
- multilingual versions;
- teacher notes;
- later subject resources.

The front end may present the same underlying content in many ways. The source should remain as close as practical to one authoritative object.

## Standing design test

For every significant piece of content, ask:

> Is this scientifically rigorous, understandable at the learner’s stage, consistent with the project’s canonical concepts, accessible without lowering the intellectual demand, and structured so that support can eventually fade?

If not, revise it before adding more material.