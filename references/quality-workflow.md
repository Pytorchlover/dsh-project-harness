# Review, verification, and handoff

## Inspect the complete change

Confirm the Git root, branch, base, dirty state, and untracked files. Review committed, staged, unstaged, and relevant generated output. Re-establish the base after merges or rebases.

## Select evidence by affected surface

- Logic change: focused owning tests; add adjacent tests when a shared contract changes.
- Types or public interfaces: typecheck plus consumer or contract tests.
- User/model-visible output: snapshot, E2E, or runnable example at the real entry path.
- Build, exports, manifests, workers, or generated artifacts: build and built-artifact smoke.
- Documentation: link, generation, formatting, and example checks owned by the project.
- Provider or integration behavior: real integration test when credentials and authority are available; never print secrets.

Do not run a full suite by reflex. Use it for repository-wide changes, CI diagnosis, or explicit requests. Never weaken filters or thresholds merely to produce green output.

## Semantic review

Trace both sides of changed contracts. Check lifecycle, cancellation, disposal, error reporting, security boundaries, migration and rollback, authority enforcement at the executing operation, and whether retained state has one authoritative owner. Verify tests would fail on the intended regression.

Documentation must match behavior, defaults, errors, configuration, persistent/wire fields, and public interfaces. Automated checks do not prove prose accuracy.

## Reporting

Report exact commands and results. Separate passed, failed, skipped, unavailable, and not-run checks. A push, merge, deployment, or interrupted process is not successful until its observable acceptance check passes.

Handoffs name the exact next action and preserve uncertainty. Final responses summarize outcome, material files, validation, and remaining risks without requiring the reader to reconstruct earlier status messages.
