# Team collaboration

## Lead responsibilities

The lead owns decomposition, authority boundaries, dependency order, final integration, and the user-facing result. Delegation does not transfer responsibility for the final diff or checks.

Create parallel tasks only when they have independently useful outcomes and bounded write scopes. Give each teammate the objective, relevant context, non-goals, permitted mutations, acceptance evidence, and expected handoff format.

## Task graph

Represent work as a DAG when dependencies matter. A task records:

- Stable id and outcome.
- Owner and status.
- Dependencies.
- Advisory write scopes.
- Acceptance evidence.

An owner claims one ready task at a time when practical. Update task state with compare-and-set discipline: re-read shared state before overwriting a changed task record.

## Shared checkout rules

- All members can observe writes immediately.
- Write scopes reduce collisions but do not authorize writes and are not locks.
- Avoid overlapping source edits. If overlap is unavoidable, serialize the work or designate one integrator.
- Formatters, generators, dependency installers, and broad scripts can touch files outside the apparent scope; announce and coordinate them.
- On stale-file or patch rejection, re-read and rebase the intended edit. Do not erase another member's changes.

## Communication

Use quiet status messages for information and waking follow-ups for new work that must be acted on. Treat an accepted or queued message as delivered work; do not blindly resend. After any wait or timeout, re-read authoritative task and repository state.

The lead waits for all required tasks, inspects the combined diff, resolves ownership gaps, and runs integration evidence before finalizing.
