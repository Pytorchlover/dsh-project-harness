# Harness architecture

This skill adapts the repository-development system observed in DeepSeek Harness at `b150a551b8` (`dsh-v0.1.1-rc.2`). The source may evolve; the target repository's live state always wins.

## Five layers

1. **Standing instructions:** root `AGENTS.md` contains rules needed in almost every task, including lessons promoted from confirmed incidents. Nested `AGENTS.md` files add only subtree-specific constraints.
2. **Current-state documentation:** architecture, development, subsystem, package, and user documents each own a distinct type of fact.
3. **Decision records:** Agent Notes retain motivation, the selected decision, real rejected alternatives, consequences, and verification obligations.
4. **Workflow skills:** review, pre-push, release, documentation, or other situational procedures load only when needed.
5. **Executable evidence:** focused tests and checks prove affected behavior locally; CI provides exhaustive coverage and platform matrices.

Team coordination overlays these layers. A lead partitions work, teammates own bounded tasks, a shared task graph records dependencies, and the lead remains responsible for final integration and evidence.

## Ownership map

| Information | Maintained home |
|---|---|
| Rules needed in every task | Root `AGENTS.md` |
| Rules for one directory tree | Nested `AGENTS.md` |
| System composition and ownership | `docs/architecture.md` |
| Setup, daily commands, contribution flow | `docs/development.md` |
| Public package or module contract | Owning README or API docs |
| Why a non-trivial decision won | `.agents/notes/<lifecycle>/<class>/...` |
| Current implementation checklist | `.agents/plans/active/...` |
| Reusable situational procedure | `.agents/skills/<workflow>/SKILL.md` |
| Incident chronology and evidence | Postmortem/incident document |
| Recurring failure classes stated as rules | Defect-class failure-mode document linked from root `AGENTS.md` |
| Review result or teammate transfer | Handoff document or task message |

Do not duplicate the same rule across tiers. Put a short link at the point of use.

## What is deliberately not copied from DSH

- DSH package topology, Cordis plugin conventions, TypeScript-only rules, bilingual documentation gates, release policy, and fixed commands.
- DSH's experimental runtime implementation details for durable mailboxes and session logs.
- Absolute coverage targets or documentation budgets without project evidence.

The reusable decisions are the separation of concerns, durable rationale, scoped instructions, explicit ownership, advisory write scopes, final-lead integration, and evidence proportional to the change.
