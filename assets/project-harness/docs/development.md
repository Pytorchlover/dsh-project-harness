# Development

This guide owns contributor setup and the daily change workflow for `{{PROJECT_NAME}}`. Product behavior and component contracts belong in their owning documentation.

## Prerequisites

<!-- TODO: Pin supported runtimes, package managers, system dependencies, and required local services. -->

## Setup

```sh
{{INSTALL_COMMAND}}
```

<!-- TODO: Add the first runnable local outcome and non-secret environment setup. -->

## Daily commands

```sh
{{BUILD_COMMAND}}
{{LINT_COMMAND}}
{{TYPECHECK_COMMAND}}
{{TEST_COMMAND}}
```

## Change flow

1. Inspect applicable `AGENTS.md` files, Git state, and the owning implementation and docs.
2. Create an active plan for multi-step, risky, cross-component, or delegated work.
3. Implement the smallest coherent change and update its tests and documentation together.
4. Add or update an Agent Note when the change carries a non-trivial decision.
5. Run focused evidence, inspect the final diff, and use the pre-push workflow before claiming readiness.

## CI and releases

<!-- TODO: Link to workflow files and release/deployment runbooks; do not copy their full command inventories here. -->
