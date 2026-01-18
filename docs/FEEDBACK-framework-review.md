# Framework Review Feedback (WIP)

**Date**: 2026-01-18  
**Scope**: Review of the current “internet arguments → claims → evaluation” research/analysis framework; focus on process/documentation and data integrity, not substantive claim truth.

## What I Reviewed

- `AGENTS.md` (methodology + templates)
- `WORKFLOWS.md` (operational procedures)
- `PLAN-framework.md` (reorg plan + open questions)
- `claims/registry.yaml` (claim + chain registry structure)
- `reference/sources.yaml` (source registry structure)
- `tracking/predictions.md` (prediction registry structure)
- `analysis/syntheses/neofeudalism-discourse-synthesis.md` (example output)
- Current repo layout (`reference/`, `analysis/`, `inbox/`)

## What’s Working Well

- **Claim-centric architecture** is a strong core abstraction for “argument processing”, and you already model key relations (`supports`, `contradicts`, `depends_on`, `modified_by`, chains).
- **Three-stage method (descriptive → evaluative → dialectical)** is a good default for avoiding “premature critique” and for producing reusable structured artifacts.
- **Evidence hierarchy + confidence calibration** provides a consistent language for uncertainty and should transfer well across domains.
- **Inbox via symlinks** is a pragmatic operational choice (keeps canonical sources stable while tracking WIP state).
- **Templates for chains, scenario matrices, dashboards, and conversational sessions** are well-chosen primitives for internet-argument analysis (where “what would discriminate between scenarios?” matters).

## Main Gaps / Improvements (Process-Level)

### 1) Schema mismatch between docs and actual YAML structures (high priority)

The examples in `AGENTS.md` don’t match the current on-disk schemas:

- `claims/registry.yaml` is keyed as `claims: { CLAIM_ID: {...} }`, but `AGENTS.md` shows a single `claim:` object example.
- `reference/sources.yaml` is keyed as `sources: { SOURCE_ID: {...} }`, but `AGENTS.md` shows a single `source:` object example.
- `claims/registry.yaml` contains a `chains:` index (with `CHAIN-...` metadata), but this isn’t documented as part of the registry schema.

**Recommendation**: add a canonical “Current File Schemas” section (or separate `docs/SCHEMA-*.md`) that exactly mirrors real files, so agents don’t drift.

### 2) Integrity rules vs. current data: source IDs and relationship fields (high priority)

The stated rule “every claim in registry.yaml must have valid `source_ids`” is currently violated if “valid” means “present in `reference/sources.yaml`”.

Examples of `source_ids` currently used as placeholders / uncataloged references:
`deepseek-r1`, `chm-alexnet`, `standard-economics`, `macro-identity`, `historical-pattern`, `reuters-rio-tinto-amazon`, `japan-ai-act`, `eu-ai-act`.

Separately, `supports` / `contradicts` sometimes contain items that do not look like claim IDs (e.g. thesis labels like `equity-escape-thesis`, or what may be source IDs like `acemoglu-restrepo-tasks`).

**Recommendation (choose one and document it clearly)**:

- **Option A (strict)**: require every `source_id` in claims to exist in `reference/sources.yaml` (even if stub entries), and require relationship fields to contain claim IDs only.
- **Option B (typed references)**: allow `source_ids` to include “uncataloged placeholders” but enforce a prefix convention (e.g. `uncat:*`), and introduce separate fields for `related_sources`, `related_theses`, or `notes_links` to avoid mixing types in `contradicts`.

Either way, the rule should be enforceable by a validator.

### 3) Predictions are defined but not synced (high priority)

The framework states: any `[P]` claim should also be registered in `tracking/predictions.md`.  
But `claims/registry.yaml` contains `[P]` claims (e.g. `TECH-2026-002`, `LABOR-2026-002`, `DIST-2026-003`) while `tracking/predictions.md` says “Total Predictions Tracked: 0”.

Also, prediction ID conventions are inconsistent:
- Templates show `P-DOMAIN-YYYY-NNN` or `P-LABOR-...`
- Actual prediction claims currently use domain IDs like `LABOR-2026-002` with `type: "[P]"`

**Recommendation**:
- Decide whether predictions are **(a)** regular domain claim IDs with `type: "[P]"`, or **(b)** a separate `P-...` ID namespace.
- Document the rule and update templates accordingly.
- Add a process step (and ideally a validator check): “Every claim with `type: "[P]"` must have a matching entry in `tracking/predictions.md`.”

### 4) Claim ID allocation needs a concurrency-safe workflow (high priority)

`claims/registry.yaml` includes `counters:` per domain, but the workflow doesn’t define:
- how an agent “claims” the next ID,
- how to avoid collisions across multiple agents,
- what to do if a claim is deleted/merged.

**Recommendation**:
- Specify a simple policy (e.g. “reserve IDs in one commit”, or “one agent at a time increments counters”, or “use a script that edits counters + inserts claim atomically”).
- If multi-agent parallelism is a goal, seriously consider a small helper script to allocate IDs deterministically and reduce merge conflicts.

### 5) Source lifecycle states are underspecified (medium priority)

Right now, sources can be:
- cataloged but not analyzed (`analysis_file: ""`)
- “cited for evidence” without a dedicated analysis file
- analyzed via synthesis rather than per-source analysis (many sources point to the same synthesis file)

This is all valid, but it needs explicit semantics so integrity rules remain meaningful.

**Recommendation**:
- Add a `status` (or similar) to source records: `captured` | `cataloged` | `extracted` | `analyzed` | `superseded`.
- Consider changing `analysis_file` → `analysis_files` (list) so one source can be referenced by multiple analyses without ambiguity.

### 6) “Internet argument capture” could be more reproducible (medium priority)

Internet arguments are brittle (edits/deletions/context loss). The workflow would benefit from explicitly capturing:
- a stable URL and/or archive link (where possible),
- quoted excerpts with enough surrounding context,
- author identity/handle + date/time,
- a “claim boundary” (what exactly is being asserted).

**Recommendation**:
- Add a lightweight “Argument Capture” template (even for tweets/threads) that standardizes quoting and provenance before extraction.

### 7) Operationalization and falsification criteria for non-prediction claims (medium priority)

You already have falsification/verification criteria in the prediction template, but many internet-argument claims are **quasi-empirical** without being framed as predictions.

**Recommendation**:
- Add an optional field/section for claims: “Operationalization / What would change my mind?” especially for `[H]`, `[T]`, and some `[F]` (where scope is contested).

## Suggested Minimal Next Steps (Process-Only)

1. **Write down canonical schemas** for `claims/registry.yaml`, `reference/sources.yaml`, and `tracking/predictions.md` (matching real files).
2. **Decide and document**: prediction ID scheme; strict vs typed reference policy; relationship field type rules.
3. **Add a validator** (even a simple script) that checks:
   - claim `source_ids` exist in `reference/sources.yaml` (or follow the placeholder convention),
   - every `[P]` claim is present in `tracking/predictions.md`,
   - `claims_extracted` back-links exist,
   - relationships only reference claim IDs (if adopting strict typing).
4. **Define claim ID allocation** (human policy or script) to avoid merge pain as more agents contribute.

## Open Questions to Resolve (Decision Log Candidates)

- Do we treat “standard econ / macro identity / historical pattern” as **sources** (with stub entries), or as **internal knowledge categories** (and if so, how do we represent them)?
- Are “thesis labels” (e.g. “equity escape thesis”) first-class claims that should get claim IDs, or should they live only in analysis narrative text?
- Should a synthesis that covers multiple primary sources count as “analysis” for each source, or do we still require per-source analysis files for `[REVIEWED]` / `[CANONICAL]`?

