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

Add or update `.agents/notes/<lifecycle>/<class>/yyyy-mm-dd-topic.md` when a change alters behavior, architecture, a shared contract, process/tooling, testing strategy, persistent data, wire/config formats, or another decision likely to be revisited.

Lifecycle:

- `proposed`: substantial future work under review.
- `implemented`: shipped current decision; keep paths and facts current.
- `rejected`: declined proposal retained only while its rationale prevents a plausible mistake.

Classes: `feature`, `bug-fix`, `simplification`, `architecture`, `process`, `testing`. Extend only when the project has a real classification gap.

Every note includes the problem, proposal/decision, genuine alternatives considered, and acceptance criteria/risks or consequences. Do not invent alternatives. Do not append a change log to an implemented note; update current facts in place. A reversal gets a new cross-linked note.

## Handoff

Use a handoff when another agent or person must continue unfinished work. Include exact state, changed files, commands run and results, remaining work, blockers, risky assumptions, and next safe action. Never describe an interrupted command as completed.
