# Repository initialization

## Preflight

Resolve the Git root, then inspect:

- `git status --short --branch`, remotes, default branch, and ignored files.
- Language/package manifests and the actual package manager lockfile.
- Existing `AGENTS.md`, `CLAUDE.md`, contribution docs, ADR/RFC folders, issue templates, and local skills.
- Build, lint, typecheck, test, documentation, and CI commands from manifests and workflows.
- Monorepo boundaries and directories whose ownership differs enough to need nested instructions.

Do not initialize into the current shell directory merely because it is the workspace root; prove the target.

## Generate the baseline

Run:

```sh
python3 <skill-dir>/scripts/init_project_harness.py <repo-root> --project-name '<name>' --dry-run
python3 <skill-dir>/scripts/init_project_harness.py <repo-root> --project-name '<name>'
```

The script creates only missing files. If a destination exists, it reports `SKIP`. To intentionally replace generated or obsolete harness files, obtain approval and run `--overwrite`; existing files are copied to `.agents/harness-backups/<timestamp>/` before replacement.

## Tailor the baseline

Replace inferred or unresolved command placeholders with commands that execute successfully in the target. Remove irrelevant sections. Add nested `AGENTS.md` only where a directory has materially different constraints; do not mirror the repository tree mechanically.

For an existing mature repository, prefer a gap audit and focused additions. A new documentation system is not automatically better than an established ADR, RFC, or contribution workflow.

## Acceptance

- Root instructions name the actual project, layout, commands, safety boundaries, and definition of done.
- Architecture and development docs link to sources of truth instead of copying inventories.
- Decision-note and execution-plan lifecycles are understandable without this skill.
- Local review and pre-push skills discover commands from the repository and do not claim a universal suite.
- A second default initializer run creates nothing and changes nothing.
