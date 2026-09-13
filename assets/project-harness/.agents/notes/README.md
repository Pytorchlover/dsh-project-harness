# Agent Notes

Agent Notes preserve durable project decisions: why a change was needed, what was chosen, which real alternatives lost, and the resulting consequences or risks. They do not replace current architecture, API, or development documentation.

## Path

Use `{lifecycle}/{class}/yyyy-mm-dd-topic.md`.

Lifecycle:

- `proposed/`: substantial future work under review.
- `implemented/`: shipped decisions, kept current with where and how the decision exists.
- `rejected/`: declined proposals retained only while their rationale prevents a plausible mistake.

Classes: `feature`, `bug-fix`, `simplification`, `architecture`, `process`, and `testing`.

## When required

Add or update a note when a change alters behavior, architecture, a shared contract, process/tooling, testing strategy, persistent data, wire/config formats, or another decision likely to be revisited. Purely mechanical or local behavior-preserving edits are exempt. Update the existing owning note instead of creating a duplicate.

## Format

Proposed notes contain `Problem`, `Proposal`, `Alternatives considered`, `Acceptance criteria`, and `Risks`. Implemented notes contain `Problem`, `Decision`, `Alternatives considered`, and `Consequences`, written as current shipped state. Record only real alternatives; do not invent ceremony.

A reversal gets a new cross-linked note. Update paths, names, defaults, and mechanisms in an implemented note when the same decision moves; do not append a change log.

## Proportionality

Use a decision note for a durable choice worth revisiting. Parameter sweeps and exploratory runs can share one experiment report; small internal fixes can explain rationale in the change. Do not create a note per commit. Confirmed lessons belong in the owning rules or module docs, with evidence linked; no separate memory hierarchy is required.
