---
name: project-code-review
description: Review a change in this repository against its live base, applicable AGENTS.md rules, owning contracts, decision notes, and relevant quality evidence. Use for PR or branch review; do not mutate the change unless the user also asks for fixes.
---

# Project code review

Confirm the Git root, live base, exact head, dirty state, and every applicable `AGENTS.md`. Read the full diff plus enough owning code and documentation to understand intent and contracts.

Prioritize correctness, lifecycle, security, data loss, broken public behavior, and missing required evidence over style. Trace both sides of changed interfaces and the real entry path. Check errors, cancellation, disposal, authorization at the executing operation, state ownership, migrations, rollback, and whether tests fail on the intended regression.

Verify changed behavior, defaults, configuration, persistent/wire fields, and public interfaces update their owning docs. A green automated check does not prove prose accuracy or semantic correctness.

Report each actionable finding with location, impact, and evidence. Separate blockers from suggestions. Omit issues already conclusively enforced by passing checks. If there are no findings, say so and name residual test or review gaps.
