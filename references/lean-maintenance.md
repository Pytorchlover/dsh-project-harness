# Proportionate documentation and migration

Start with root AGENTS.md, architecture and development docs. Add a contract,
experiment report or subsystem guide only when it owns information that would
otherwise be hard to find. Existing equivalent documents take precedence over
these suggested names. A short root navigation section is usually sufficient;
there is no mandatory full-file index, timestamp header or code inventory.

## Lessons and decisions

- Put a confirmed, broadly applicable lesson into AGENTS.md as a short actionable
  rule. Module-specific lessons belong in the owning module documentation or
  scoped AGENTS.md. Link to evidence instead of copying incident history.
- When the same failure class recurs across modules, keep one defect-class document
  of rules — symptom, rule, evidence link — and link it from the root AGENTS.md in
  a single line. Order it by defect class, never by date, and create it with the
  first confirmed class rather than as an empty scaffold.
- Keep a one-off incident, unsuccessful experiment or uncertain hypothesis in its
  experiment report or active plan. Recurrence alone does not prove a general rule.
- Do not create a separate memory taxonomy by default. Add a searchable knowledge
  base only when actual retrieval needs justify its ongoing maintenance.
- Parameter sweeps and exploratory runs can share one experiment report. Create a
  decision note for a durable choice worth revisiting, such as changing a default,
  compatibility contract, quality criterion or architecture. A small internal fix
  may record its rationale in the change itself; do not demand a note per commit.
- Plans track multi-step execution. Owners and dependency graphs matter when work
  is partitioned; a single-owner task does not need a ceremonial task DAG.

## Migrating an existing harness

1. Inspect current rules, facts, plans, experiments, failure-mode or incident lists
   and local skills; identify the maintained home of each fact before moving anything.
2. Preserve operating constraints, active state and historical evidence. Merge
   short overlapping guides; retire empty categories and redundant indexes.
3. Move useful records with their links updated. Do not silently delete unresolved
   work, incident evidence or user-authored knowledge. Keep the migration as a
   reviewable commit so its previous structure is recoverable.
4. Install the chosen skill in a project or user location explicitly within scope.
   Remove obsolete workflow copies only after updating their consumers. Tool
   adapters are pointers, not parallel rule bodies; add them only where used.
5. Check changed document links and manually verify commands, defaults and current
   status against code. Report preserved, merged, removed and deferred items.

No algorithm, dependency or production environment changes are implied by a
harness migration. Do not run an initializer in overwrite mode to perform it.

## Executable evidence

Run `python3 <skill-dir>/scripts/check_docs.py <repo-root> [paths ...]` on affected
Markdown files or directories. Default scope is tracked root Markdown, docs/,
.agents/notes/ and .agents/plans/. Explicit paths also cover newly created files.
Use real Markdown links for source references; there is no source-directory whitelist.
Root-relative links resolve from the repository root. External URLs, code blocks,
template documents and fragment-only links are skipped. Local destination paths
are checked, but anchors, arbitrary HTML, all Markdown grammar, unlinked files,
prose freshness, symbols and command correctness are not verified.

Choose checks according to the change. Do not require an all-doc scan on every
unrelated code edit, and never describe a link check as proof of semantic sync.
