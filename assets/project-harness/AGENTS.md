# AGENTS.md

`{{PROJECT_NAME}}` is described in [docs/architecture.md](docs/architecture.md). Read that document before changing component ownership or cross-module contracts; use [docs/development.md](docs/development.md) for setup and daily workflow.

## Repository layout

<!-- TODO: Replace with a short responsibility-oriented map of real top-level directories. -->

## Commands

```sh
{{INSTALL_COMMAND}}
{{BUILD_COMMAND}}
{{LINT_COMMAND}}
{{TYPECHECK_COMMAND}}
{{TEST_COMMAND}}
```

Run the narrowest credible checks for the affected behavior. CI owns the exhaustive platform and integration matrix unless this repository states otherwise.

## Rules and confirmed failure modes

<!-- TODO: Add project rules as they become confirmed, grouped under short headings that name the owning group. Keep each rule to one to three lines and link the document that owns its detail. Delete generic reminders an agent already knows. -->

Confirmed reusable lessons become short rules here or in the owning module documentation; keep incident details in their original report.

<!-- TODO: When a failure class recurs across components and would be costly to rediscover, add one entry per class — symptom, rule, evidence link — or move the list to docs/failure-modes.md and link that file in one line. Order entries by defect class, never by date. Delete this placeholder while the list is empty. Do not create a memory hierarchy or full-file index without a concrete need. -->

## Change workflow

- Resolve the actual Git root and inspect the worktree before editing. Preserve unrelated and uncommitted user changes.
- Keep one maintained home for each fact. Standing rules belong here, execution state in `.agents/plans/`, rationale in `.agents/notes/`, and situational procedures in `.agents/skills/`.
- Update affected documentation. Record durable decisions worth revisiting in Agent Notes; routine experiments belong in their experiment report, and small internal fixes can explain rationale in the change.
- Multi-step, risky, cross-component, or delegated work uses an active change plan with acceptance criteria, owners, dependencies, and validation.
- Never commit credentials. Treat generated files, migrations, release operations, shared infrastructure, and destructive commands according to their owning instructions.

## Collaboration

The lead agent owns decomposition, final integration, the final diff, and verification. Partition parallel tasks by outcome and advisory write scope; write scopes reduce conflicts but are not locks. Coordinate formatters, generators, dependency operations, and broad scripts because they can modify files outside the apparent scope.

## Definition of done

- Requested behavior is implemented at the real entry path.
- Tests and documentation match the changed contract.
- Relevant checks ran and their exact results are reported.
- The final diff contains no unintended files, secrets, stale generated output, or unresolved placeholders.

Use [.agents/skills/project-code-review/SKILL.md](.agents/skills/project-code-review/SKILL.md) for reviews and [.agents/skills/project-pre-push-checks/SKILL.md](.agents/skills/project-pre-push-checks/SKILL.md) before claiming a branch is ready to push or review.

## Editing these instructions

Keep this file to rules an agent needs in almost every session, grouped under short headings. Put procedures in [docs/development.md](docs/development.md) or project-local skills, durable rationale in [.agents/notes/](.agents/notes/README.md), current execution state in [.agents/plans/](.agents/plans/README.md), and subtree-only constraints in a nested `AGENTS.md`. Retire or rewrite a rule that no longer matches the repository instead of annotating it as deprecated.
