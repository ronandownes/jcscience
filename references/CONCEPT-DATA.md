# Canonical Concept Data Model

This document specifies how important scientific concepts should be stored so the JC Science project has one authoritative project-owned source for definitions, terminology, symbols, units and related learning metadata.

The aim is simple: **write the concept once, review it properly, then reuse it everywhere.**

A chapter, glossary, pop-up, revision card, quiz, audio layer or multilingual view should not quietly invent its own competing definition.

## Terminology

### Canonical

The project’s accepted authoritative version of an object.

“Canonical definition” does not mean an eternal definition imposed by nature. It means the version this project has deliberately accepted after checking the disciplinary meaning, scope, learner level and relevant authoritative references.

### Single source of truth

One maintained source record supplies many uses.

For example, the canonical record for `density` may supply:

- the chapter definition;
- a glossary entry;
- a hover/pop-up definition;
- a revision card;
- feedback in a question;
- a read-aloud version;
- a translated version;
- teacher notes.

If the definition is improved, the source record changes once and dependent views should update from it.

### Front end

What the learner or teacher sees and interacts with: pages, buttons, definitions, diagrams, questions, hints, audio, simulations and controls.

### Back end / source layer

The structured material from which those visible views are built: PreTeXt source, YAML/JSON/XML data, question metadata, concept records and build logic.

The project should permit many front-end presentations without creating many independent back-end copies of the same academic statement.

## Recommended record

The exact storage format can evolve. YAML is readable for humans and machines and is suitable as an initial format.

A concept record should be able to contain fields such as:

```yaml
id: density
status: reviewed
preferred_term: Density
aliases: []
concept_type: quantity

scope:
  stage: junior-cycle
  notes: ""

wording:
  understand: ""
  exam_ready: ""
  precise: ""

notation:
  symbols: []
  relationships: []

units:
  si_unit: ""
  other_units: []

learning:
  prerequisites: []
  related: []
  examples: []
  non_examples: []
  misconceptions: []
  representations: []

assessment:
  expected_uses: []
  common_errors: []

accessibility:
  vocabulary_support: []
  pronunciation: ""
  read_less_notes: ""

curriculum:
  learning_outcomes: []
  strand: ""

provenance:
  sources: []
  review_notes: ""
  last_reviewed: ""
```

Not every concept needs every field.

## Concept types

Use controlled concept types so the resource can distinguish what kind of claim is being made.

Initial controlled values may include:

- `definition-term`
- `quantity`
- `unit`
- `symbol`
- `convention`
- `empirical-law`
- `model`
- `theory`
- `principle`
- `derived-relationship`
- `approximation`
- `observation`
- `inference`
- `hypothesis`
- `process`
- `structure`
- `classification`
- `skill`

This list may expand when a genuine need appears. Do not create near-duplicate types merely because two authors use different labels.

## Status lifecycle

Canonical records should have an explicit review state.

Suggested values:

- `draft` — useful working wording but not yet academically reviewed;
- `reviewed` — checked for scientific accuracy, scope, age-appropriateness and consistency;
- `provisional` — accepted for use but has a known unresolved terminology or curricular issue;
- `deprecated` — retained only for compatibility; another record should now be used.

Student-facing “exam-ready” definitions should normally come from `reviewed` records.

## Three wording layers

### Understand

Designed to establish meaning.

This can be longer than the memorisable version. It should answer the learner’s likely question: “What does this actually mean?”

### Exam-ready

Concise and complete enough for the intended Junior Cycle assessment context.

This is not automatically copied from a marking scheme or textbook. It is project-authored wording calibrated against the curriculum and assessment evidence.

### Precise

States the concept with greater disciplinary precision, including conditions, distinctions, notation or limitations where they matter.

The three layers should not contradict each other. They are views at different explanatory resolutions of the same underlying concept.

## Relationships and derivations

Do not store equations as isolated decorative formulae.

Where possible, record:

- what each symbol means;
- unit constraints;
- whether the relationship is definitional, empirical, model-based or derived;
- conditions under which it applies;
- prerequisite relationships;
- common rearrangements;
- common dimensional/unit errors.

This will later allow the Mathematics, Physics and Applied Mathematics projects to reuse a more formal version of the same architecture.

## Reuse rule

A concept may appear in dozens of places, but the project should avoid dozens of manually maintained definitions.

Preferred pattern:

1. canonical concept record;
2. reusable renderer/include;
3. context-specific display options.

For example, a page might request only:

- preferred term + Understand;
- preferred term + Exam-ready;
- Precise + units;
- a compact glossary view;
- a question-feedback view.

The content remains linked to one source object.

## Context-specific wording

Sometimes the full canonical wording is inappropriate in running prose.

A chapter may use a natural contextual sentence, but if that sentence is serving as the formal definition, it should reference the canonical record rather than creating a competing definition.

If a genuine alternative formulation is needed, record it explicitly as a variant with a reason.

## Provenance

Canonical definitions should record where the disciplinary meaning was checked.

The source list may include:

- curriculum/specification location;
- standards body;
- professional scientific body;
- authoritative nomenclature source;
- reputable university/reference source;
- assessment evidence used only for calibration.

Commercial textbooks can be listed as comparison evidence but should not be the authority for accepting wording.

## Quality review

Before changing a reviewed concept, check the effect on:

- chapters;
- glossary;
- assessment feedback;
- symbols and units;
- related concepts;
- translations;
- audio;
- revision resources;
- later subject reuse.

A definition improvement should propagate. A local patch that creates inconsistency should not.

## Implementation principle

**Many views; one maintained academic object.**

That principle is more important than the first choice of YAML, XML or another format. The representation can change later without changing the academic architecture.