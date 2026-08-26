---
name: project-pre-push-checks
description: Select and run the smallest credible local checks for an outgoing change in this repository before pushing, force-pushing, or claiming readiness for review. Use the repository's actual scripts and CI as sources of truth; do not default to a full suite.
---

# Project pre-push checks

Confirm the Git root, branch, live base, and complete committed/staged/unstaged/untracked scope. Re-evaluate after a merge, rebase, or retarget.

Select evidence by affected surface:

- Logic: focused owning tests; adjacent tests for shared contracts.
- Types/public interfaces: typecheck and consumer/contract tests.
- User-visible output: snapshot, E2E, or real runnable entry path.
- Build/exports/manifests/generated artifacts: build and built-artifact smoke.
- Documentation: owning link, generation, formatting, and example checks.
- External providers: relevant integration test when credentials and authority exist; never print secrets.

CI owns exhaustive platform and integration matrices. Run a full local rehearsal only for repository-wide changes, CI diagnosis, or explicit request. Do not repeat a passing check solely because commit or push follows, and do not weaken filters or thresholds to produce green output.

If a relevant check fails, stop before an ordinary push and fix or report the blocker. Report exact commands and distinguish passed, failed, skipped, unavailable, interrupted, and not-run checks.
