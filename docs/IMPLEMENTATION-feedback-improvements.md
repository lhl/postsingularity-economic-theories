# Implementation: Framework Feedback Improvements

> **Source**: [FEEDBACK-framework-review.md](FEEDBACK-framework-review.md)
> **Started**: 2026-01-18
> **Status**: HIGH-PRIORITY COMPLETE (6/8 items done, 2 deferred)

---

## Punchlist

| # | Issue | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 1 | Schema mismatch between docs and YAML | High | `[x]` DONE | Created SCHEMA.md |
| 2 | Integrity violations - placeholder source_ids | High | `[x]` DONE | Added 9 stub sources |
| 3 | Integrity violations - non-claim-IDs in relationships | High | `[x]` DONE | Cleared, moved to notes |
| 4 | Predictions not synced to predictions.md | High | `[x]` DONE | Added 3 [P] claims |
| 5 | Claim ID allocation policy undefined | High | `[x]` DONE | Documented in D6 |
| 6 | Source lifecycle states underspecified | Medium | `[x]` DONE | Added status field in schema |
| 7 | Internet argument capture template missing | Medium | `[ ]` DEFER | Add template later |
| 8 | Operationalization for non-predictions | Medium | `[ ]` DEFER | Add field later |

---

## Decision Log

Decisions made to resolve open questions from feedback review.

### D1: How to handle "standard knowledge" sources

**Question**: Do we treat "standard econ / macro identity / historical pattern" as sources (with stub entries), or as internal knowledge categories?

**Decision**: Create stub source entries with `type: "KNOWLEDGE"`

**Rationale**:
- Keeps source_ids validation simple (everything in sources.yaml)
- Makes explicit what "standard knowledge" we're relying on
- Can add citations later if we want to ground them

**Date**: 2026-01-18

---

### D2: Prediction ID scheme

**Question**: Are predictions (a) regular domain claim IDs with `type: "[P]"`, or (b) a separate `P-...` ID namespace?

**Decision**: Regular domain claim IDs with `type: "[P]"`

**Rationale**:
- Predictions are claims in a domain (TECH, LABOR, etc.)
- Separate namespace adds complexity without clear benefit
- The `[P]` type tag is sufficient to identify them
- predictions.md references them by their domain ID

**Date**: 2026-01-18

---

### D3: Strict vs typed references policy

**Question**: Should we require all source_ids to exist in sources.yaml, or allow typed placeholders?

**Decision**: Strict - all source_ids must exist in sources.yaml

**Rationale**:
- Simpler validation rule
- Forces us to be explicit about what we're citing
- Stub entries with `type: "KNOWLEDGE"` or `type: "UNCATALOGUED"` handle edge cases
- Avoids proliferation of ad-hoc placeholder conventions

**Date**: 2026-01-18

---

### D4: Relationship field types

**Question**: Should `supports`, `contradicts`, etc. only contain claim IDs, or can they reference sources/theses?

**Decision**: Claim IDs only in relationship fields

**Rationale**:
- Cleaner data model
- If a thesis needs to be referenced, it should become a claim with an ID
- Source relationships go in `source_ids`
- Keeps validation simple

**Action Required**:
- Create claims for thesis labels currently in relationship fields
- Update existing claims to use proper claim IDs

**Date**: 2026-01-18

---

### D5: Synthesis as analysis for sources

**Question**: Should a synthesis that covers multiple primary sources count as "analysis" for each source?

**Decision**: Yes for `[DRAFT]` rigor level; per-source analysis required for `[CANONICAL]`

**Rationale**:
- Synthesis is a valid form of analysis
- But for highest rigor, each source deserves dedicated attention
- `analysis_file` can point to synthesis for now
- Can create per-source analyses later to upgrade to CANONICAL

**Date**: 2026-01-18

---

### D6: Claim ID allocation policy

**Question**: How do agents allocate claim IDs without collisions?

**Decision**: Single-agent increment with commit atomicity

**Policy**:
1. Read current counter from `claims/registry.yaml`
2. Increment counter and assign ID
3. Add claim with new ID
4. Commit counter + claim together atomically
5. If merge conflict on counter, re-read and re-number

**Rationale**:
- Simple for current single-agent workflow
- Commit atomicity prevents most conflicts
- Can add scripting later if multi-agent becomes common

**Date**: 2026-01-18

---

## Worklog

### 2026-01-18: Initial setup

- Created this implementation tracking document
- Logged decisions D1-D6
- Next: Create SCHEMA.md, add stub sources, sync predictions

---

### 2026-01-18: Schema documentation (DONE)

- [x] Create docs/SCHEMA.md
- [x] Document claims/registry.yaml format
- [x] Document reference/sources.yaml format
- [x] Document tracking/predictions.md format
- [x] Add validation rules section

---

### 2026-01-18: Stub sources (DONE)

Sources added as stubs:
- [x] `deepseek-r1` - type: PAPER
- [x] `chm-alexnet` - type: ARTICLE
- [x] `standard-economics` - type: KNOWLEDGE
- [x] `macro-identity` - type: KNOWLEDGE
- [x] `historical-pattern` - type: KNOWLEDGE
- [x] `reuters-rio-tinto-amazon` - type: ARTICLE
- [x] `japan-ai-guidelines-2025` - type: REPORT (renamed from japan-ai-act)
- [x] `eu-ai-act` - type: REPORT
- [x] `acemoglu-restrepo-2019-tasks` - type: PAPER

---

### 2026-01-18: Relationship field cleanup (DONE)

Claims fixed:
- [x] `TECH-2026-004`: Cleared `contradicts`, added notes explaining contradiction with cognitive monopoly thesis
- [x] `GOV-2026-001`: Cleared `contradicts`, notes already explained equity escape thesis contradiction
- [x] `LABOR-2026-002`: Cleared `contradicts`, updated notes to reference Acemoglu-Restrepo (2019)
- [x] `GOV-2026-007`: Fixed source_id from `japan-ai-act` to `japan-ai-guidelines-2025`

---

### 2026-01-18: Prediction sync (DONE)

[P] claims added to predictions.md:
- [x] `TECH-2026-002`: "Largest training runs could exceed $1B by ~2027" - Status: [P→]
- [x] `LABOR-2026-002`: "Full automation of human labor by 2035-2045" - Status: [P?]
- [x] `DIST-2026-003`: "Post-labor → permanent underclass is 'default' outcome" - Status: [P?]
- [x] `GOV-2026-002`: Kept as [S] Speculation, not prediction - noted in predictions.md

---

*Last Updated: 2026-01-18*
