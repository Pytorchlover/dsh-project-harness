# Change documentation

Use two records because execution state and durable rationale age differently.

## Execution plan

Create `.agents/plans/active/yyyy-mm-dd-topic.md` for multi-step, cross-component, risky, or delegated work. Record:

- Objective, non-goals, assumptions, affected areas, and acceptance criteria.
- Work items with owners, dependencies, and advisory write scopes.
- Validation commands and rollback or migration requirements.
- Current decisions, blockers, and handoff state.

Update the plan as work changes. On completion, summarize the delivered outcome and move it to `completed/`, or delete it when it has no durable value. A completed plan is evidence of execution, not the authority for current behavior.

## Decision note

Add or update `.agents/notes/<lifecycle>/<class>/yyyy-mm-dd-topic.md` for durable choices likely to be revisited, such as a new default, architecture, shared contract, process, testing strategy or persistent format. A change touching these areas does not automatically require a separate note; use the proportionality guidance below.

Lifecycle:

- `proposed`: substantial future work under review.
- `implemented`: shipped current decision; keep paths and facts current.
- `rejected`: declined proposal retained only while its rationale prevents a plausible mistake.

Classes: `feature`, `bug-fix`, `simplification`, `architecture`, `process`, `testing`. Extend only when the project has a real classification gap.

Every note includes the problem, proposal/decision, genuine alternatives considered, and acceptance criteria/risks or consequences. Do not invent alternatives. Do not append a change log to an implemented note; update current facts in place. A reversal gets a new cross-linked note.

## Handoff

Use a handoff when another agent or person must continue unfinished work. Include exact state, changed files, commands run and results, remaining work, blockers, risky assumptions, and next safe action. Never describe an interrupted command as completed.

## Proportionality

Use a decision note for a durable choice worth revisiting. Parameter sweeps and exploratory runs can share one experiment report; small internal fixes can explain rationale in the change. Do not create a note per commit. Confirmed lessons belong in the owning rules or module docs, with evidence linked; recurring cross-module failure classes belong in the project's defect-class failure-mode document. No separate memory hierarchy is required.
