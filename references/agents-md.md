# Writing AGENTS.md

## Root file

Write standing orders an agent needs in most sessions:

- Project purpose and the architecture document to read before structural changes.
- Repository layout by responsibility, not an exhaustive file listing.
- Canonical install, build, lint, typecheck, test, and documentation commands.
- Security, secrets, generated-file, migration, and shared-system constraints.
- Change workflow: inspect first, preserve unrelated work, update docs with behavior, add/update a decision note for non-trivial decisions, and run relevant evidence.
- Confirmed lessons and recurring failure classes, each stated as a rule that links its evidence.
- Definition of done, links to specialized workflows, and a short statement of how this file itself is edited.

Group the rules under short named headings so a reader can find the owning group. Rules should be testable or decision-changing. Remove generic reminders that an agent already knows. Avoid situational tutorials, historical narrative, and copied API documentation.

## Rules and confirmed lessons

Distill an experience once it is confirmed; never keep a chronological log of incidents.

- A confirmed, broadly applicable lesson becomes one short actionable rule in the owning `AGENTS.md` or module document, with a link to its evidence. State the trigger and the required action so a reader can tell whether the rule applies.
- A failure class that has recurred across components, and would be costly to rediscover, gets one defect-class document such as `docs/failure-modes.md`, linked from the root file in a single line. Write each entry as the rule that prevents recurrence with its symptom and evidence link; keep chronology out. Create the document with the first confirmed class, never as an empty scaffold.
- A one-off incident, an unsuccessful experiment, or an unproven hypothesis stays in its report or active plan. Recurrence alone does not prove a general rule.
- Retire or rewrite a rule that no longer matches the repository; do not keep a deprecated list.

## Nested files

Create a nested `AGENTS.md` only when its subtree differs in commands, architecture, generated/source ownership, safety, testing, or documentation. It supplements the root file and should not repeat it.

Useful examples include frontend, infrastructure, database migrations, generated SDKs, vendored code, and documentation trees. Keep each rule self-contained and link to its rationale or procedure.

## Authoring workflow

1. Inspect the code and commands first.
2. Separate repository-wide rules from subtree rules.
3. Search for duplicated guidance before adding text.
4. Name actual commands and paths; mark unknowns instead of inventing them.
5. Convert stable mechanical rules into checks when practical.
6. Promote confirmed lessons into rules and leave incident narrative in its report.
7. Validate every link and command.

Do not make `AGENTS.md` a status board. Active work belongs in plans; durable rationale belongs in decision notes.
