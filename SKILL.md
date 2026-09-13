---
name: dsh-project-harness
description: "Initialize or improve a repository's agent harness: layered AGENTS.md instructions, team collaboration, change plans and decision notes, project-local workflow skills, review, and proportionate quality checks. Use for new-project bootstrap or for auditing an existing repo's agent-development workflow; do not overwrite established project rules without explicit approval."
---

# DSH Project Harness

Build an agent-ready repository using the transferable parts of DeepSeek Harness's development system. Adapt the system to the target project instead of copying DSH package names, commands, or release rules.

## Start from the live repository

1. Resolve the actual Git root and read every `AGENTS.md` that applies to the target path.
2. Inspect the worktree, manifests, scripts, CI, documentation, and existing contribution or decision records.
3. Preserve user changes. Initialization creates missing files by default; merge with existing files instead of replacing them.
4. State which conventions are source-confirmed and which are proposed adaptations.

For the system's layers and boundaries, read [references/harness-architecture.md](references/harness-architecture.md).

## Choose the operation

- **Initialize a new or lightly documented repository:** read [references/initialization.md](references/initialization.md), run `scripts/init_project_harness.py`, then tailor every generated command and rule against the real project.
- **Write or revise `AGENTS.md`:** read [references/agents-md.md](references/agents-md.md). Keep root instructions short and durable; put subtree-only rules in nested files.
- **Plan or document a project change:** read [references/change-docs.md](references/change-docs.md). Keep execution state separate from durable rationale.
- **Coordinate multiple agents or people:** read [references/collaboration.md](references/collaboration.md). Treat task ownership and write scopes as coordination hints, not filesystem locks.
- **Review, verify, or hand off work:** read [references/quality-workflow.md](references/quality-workflow.md). Select evidence from the affected surface; do not claim checks that were not run.

- **Simplify or migrate an existing harness:** read [references/lean-maintenance.md](references/lean-maintenance.md). Preserve useful facts and evidence; remove redundant structure.

## Operating invariants

- One fact has one maintained home; other documents link to it.
- Standing rules live in `AGENTS.md`; procedures live in skills or development docs; rationale and rejected alternatives live in decision notes; transient execution state lives in plans and handoffs.
- Update affected documentation when behavior changes; add decision notes for durable choices worth revisiting, not every experiment or internal edit. See the proportionality rules in [references/lean-maintenance.md](references/lean-maintenance.md).
- The lead agent owns integration: inspect the final diff, reconcile overlaps, run relevant checks, and wait for required delegated work before answering.
- Parallel work must be partitioned by outcome and file scope. Shared checkout writes remain visible immediately, so Bash, formatters, and generators require explicit coordination.
- Default initialization never overwrites existing files. Use `--overwrite` only with explicit approval; the script writes backups first.
- Mechanically checkable rules should become executable checks when the project can support them. CI owns exhaustive matrices; local work runs the narrowest credible regression evidence.

## Completion

Before handing off an initialized harness:

1. Remove or resolve all generated `TODO` markers that can be learned from the repository.
2. Confirm links and commands point to real files and scripts.
3. Run the initializer's dry run again and the skill validator.
4. In a temporary repository, verify that default initialization is idempotent and overwrite mode creates backups.
5. Report created, merged, skipped, and intentionally deferred pieces separately.
