# Writing AGENTS.md

## Root file

Write standing orders an agent needs in most sessions:

- Project purpose and the architecture document to read before structural changes.
- Repository layout by responsibility, not an exhaustive file listing.
- Canonical install, build, lint, typecheck, test, and documentation commands.
- Security, secrets, generated-file, migration, and shared-system constraints.
- Change workflow: inspect first, preserve unrelated work, update docs with behavior, add/update a decision note for non-trivial decisions, and run relevant evidence.
- Definition of done and links to specialized workflows.

Rules should be testable or decision-changing. Remove generic reminders that an agent already knows. Avoid situational tutorials, historical narrative, and copied API documentation.

## Nested files

Create a nested `AGENTS.md` only when its subtree differs in commands, architecture, generated/source ownership, safety, testing, or documentation. It supplements the root file and should not repeat it.

Useful examples include frontend, infrastructure, database migrations, generated SDKs, vendored code, and documentation trees. Keep each rule self-contained and link to its rationale or procedure.

## Authoring workflow

1. Inspect the code and commands first.
2. Separate repository-wide rules from subtree rules.
3. Search for duplicated guidance before adding text.
4. Name actual commands and paths; mark unknowns instead of inventing them.
5. Convert stable mechanical rules into checks when practical.
6. Validate every link and command.

Do not make `AGENTS.md` a status board. Active work belongs in plans; durable rationale belongs in decision notes.
