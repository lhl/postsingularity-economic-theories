# Operational Workflows

> Quick reference for common operations in this research framework.
> For methodology and templates, see [AGENTS.md](AGENTS.md).

---

## Quick Reference: Which Workflow?

| I want to... | Use workflow |
|--------------|--------------|
| Add a new source I found | [1. New Source Submission](#1-new-source-submission) |
| Do a full analysis of a source | [2. Full Source Analysis](#2-full-source-analysis) |
| Just extract key claims quickly | [3. Quick Claim Extraction](#3-quick-claim-extraction) |
| Record a prediction to track | [4. Prediction Registration](#4-prediction-registration) |
| Update claims with new evidence | [5. Evidence Update](#5-evidence-update) |
| Check/update prediction status | [6. Prediction Evaluation](#6-prediction-evaluation) |
| Combine multiple sources into synthesis | [7. Synthesis Creation](#7-synthesis-creation) |
| Something changed, need to re-analyze | [8. Re-Analysis Trigger](#8-re-analysis-trigger) |

---

## 1. New Source Submission

**When**: You've found a new source (article, paper, thread, video, etc.) relevant to the research.

### Quick Path (just capture it)

```bash
# 1. Add raw source to reference folder
cp /path/to/source.pdf reference/primary/[author]-[year]-[shorttitle].pdf
# OR for a URL, create a markdown file with the URL and key excerpts

# 2. Create inbox symlink for later processing
cd inbox/to-catalog
ln -s ../../reference/primary/[author]-[year]-[shorttitle].pdf .
```

### Full Path (capture and catalog)

1. **Determine source ID**: `[author-lastname]-[year]-[short-title]`
   - Examples: `hotz-2026-three-minutes`, `epoch-2024-training-costs`

2. **Add raw source to `reference/`**:
   - Papers: `reference/primary/papers/`
   - Blog posts: `reference/primary/blogs/`
   - Twitter/social: `reference/primary/social/`
   - AI transcripts: `reference/transcripts/`

3. **Add entry to `reference/sources.yaml`**:
   ```yaml
   source-id:
     type: "BLOG"  # PAPER/BOOK/REPORT/ARTICLE/BLOG/SOCIAL/CONVO
     title: "Full Title"
     author: ["Author Name"]
     year: 2026
     url: "https://..."
     accessed: "2026-01-18"
     reliability: 0.5  # Initial estimate
     bias_notes: "Any known biases"
     claims_extracted: []  # Empty until analyzed
     analysis_file: ""  # Empty until analyzed
     topics: ["topic1", "topic2"]
     domains: ["TECH", "LABOR"]  # Relevant domains
   ```

4. **Create inbox symlink for analysis**:
   ```bash
   cd inbox/to-analyze
   ln -s ../../reference/primary/[filename] .
   ```

5. **Commit**:
   ```bash
   git add reference/sources.yaml reference/primary/[file]
   git commit -m "docs: add source [source-id]"
   git push
   ```

### Output
- Raw source file in `reference/`
- Entry in `sources.yaml`
- Symlink in `inbox/to-analyze/`

---

## 2. Full Source Analysis

**When**: You want to do a complete 3-stage analysis of a source.

**Prerequisites**: Source is cataloged in `sources.yaml`

### Steps

1. **Create analysis file**:
   ```bash
   touch analysis/sources/[source-id]-analysis.md
   ```

2. **Use Source Analysis Template** (from AGENTS.md):
   - Stage 1: Descriptive Summary
   - Stage 2: Evaluation
   - Stage 3: Dialectical Analysis

3. **Extract claims** as you analyze:
   - Assign IDs: `[DOMAIN]-[YYYY]-[NNN]`
   - Add to `claims/registry.yaml`
   - For predictions `[P]`, also add to `tracking/predictions.md`

4. **Update sources.yaml**:
   ```yaml
   source-id:
     claims_extracted:
       - "TECH-2026-001"
       - "LABOR-2026-002"
     analysis_file: "analysis/sources/source-id-analysis.md"
   ```

5. **Identify chains**: If claims form logical chain A→B→C, document in analysis

6. **Remove from inbox**:
   ```bash
   rm inbox/to-analyze/[filename]
   ```

7. **Commit all together**:
   ```bash
   git add analysis/sources/[source-id]-analysis.md
   git add claims/registry.yaml
   git add reference/sources.yaml
   git add tracking/predictions.md  # if predictions added
   git commit -m "feat: analyze [source-id] - extract N claims"
   git push
   ```

### Output
- Complete analysis in `analysis/sources/`
- Claims in registry with back-links
- Predictions registered if applicable
- Source updated with `claims_extracted` and `analysis_file`

---

## 3. Quick Claim Extraction

**When**: You want to capture key claims without full 3-stage analysis.

**Use case**: Rapidly processing multiple sources, or source is simple/low-priority.

### Steps

1. **Read source**, identify key claims

2. **For each significant claim**:
   - Assign ID: `[DOMAIN]-[YYYY]-[NNN]`
   - Determine type: `[F]`act, `[T]`heory, `[H]`ypothesis, `[P]`rediction, etc.
   - Estimate evidence level (E1-E6) and confidence (0.0-1.0)

3. **Add to `claims/registry.yaml`**:
   ```yaml
   TECH-2026-005:
     text: "Claim text here"
     type: "[T]"
     domain: "TECH"
     evidence_level: "E4"
     confidence: 0.5
     source_ids: ["source-id"]
     first_extracted: "2026-01-18"
     extracted_by: "claude"
     supports: []
     contradicts: []
     depends_on: []
     modified_by: []
     part_of_chain: ""
     version: 1
     last_updated: "2026-01-18"
   ```

4. **Update source's `claims_extracted`** in `sources.yaml`

5. **If any `[P]` predictions**, add to `tracking/predictions.md`

6. **Commit**:
   ```bash
   git add claims/registry.yaml reference/sources.yaml
   git commit -m "feat: extract claims from [source-id]"
   git push
   ```

### Output
- Claims in registry
- Source back-linked
- No full analysis document (can be created later)

---

## 4. Prediction Registration

**When**: You identify a prediction claim that should be tracked over time.

### Steps

1. **Ensure claim exists in registry** with type `[P]`

2. **Add to `tracking/predictions.md`** under appropriate domain:
   ```markdown
   ### [Prediction Title]
   - **Claim ID**: LABOR-2026-002
   - **Source**: teortaxes-2026-thread
   - **Date Made**: 2026-01-17
   - **Target Date**: 2035-2045
   - **Claim**: Full automation of human labor by 2035-2045
   - **Falsification Criteria**: >20% of economic output still requires human labor in 2045
   - **Verification Criteria**: <5% of economic output requires human labor
   - **Status**: [P?]
   - **Confidence**: 0.35
   - **Last Evaluated**: 2026-01-18
   - **Related Claims**: [TECH-2026-003, DIST-2026-003]
   - **Evidence Updates**:
     - 2026-01-18: Initial registration, timeline speculative
   ```

3. **Update statistics** in predictions.md header

4. **Commit**:
   ```bash
   git add tracking/predictions.md
   git commit -m "feat: register prediction [claim-id]"
   git push
   ```

---

## 5. Evidence Update

**When**: New information affects existing claims.

### Steps

1. **Identify affected claims** by ID

2. **For each affected claim** in `claims/registry.yaml`:
   - Update `confidence` if warranted
   - Add new source to `source_ids` if applicable
   - Update `supports` or `contradicts` relationships
   - Increment `version`
   - Update `last_updated`
   - Add note to `update_history` if significant

3. **If claim is a prediction**, update in `tracking/predictions.md`:
   - Add entry to Evidence Updates
   - Update Status if warranted
   - Update Last Evaluated date

4. **If evidence triggers re-analysis**, see [8. Re-Analysis Trigger](#8-re-analysis-trigger)

5. **Commit**:
   ```bash
   git add claims/registry.yaml tracking/predictions.md
   git commit -m "fix: update [claim-id] with new evidence from [source]"
   git push
   ```

---

## 6. Prediction Evaluation

**When**: Scheduled check on predictions, or specific event triggers re-evaluation.

**Suggested frequency**: Monthly for active predictions, quarterly for long-horizon

### Steps

1. **Review `tracking/predictions.md`**

2. **For each prediction**:
   - Check for new evidence since last evaluation
   - Compare current state to falsification/verification criteria
   - Update status symbol if warranted:
     - `[P+]` Confirmed
     - `[P~]` Partially Confirmed
     - `[P→]` On Track
     - `[P?]` Uncertain
     - `[P←]` Off Track
     - `[P!]` Partially Refuted
     - `[P-]` Refuted
     - `[P∅]` Unfalsifiable

3. **Add entry to Evidence Updates** with reasoning

4. **Update confidence** if changed

5. **Update Related Claims** if prediction status affects other claims

6. **Log in Recent Updates table**

7. **Commit**:
   ```bash
   git add tracking/predictions.md claims/registry.yaml
   git commit -m "docs: monthly prediction evaluation [YYYY-MM]"
   git push
   ```

---

## 7. Synthesis Creation

**When**: Multiple sources/claims warrant combined analysis.

### Steps

1. **Identify sources/claims to synthesize**

2. **Create synthesis document**:
   ```bash
   touch analysis/syntheses/[topic]-synthesis.md
   ```

3. **Use synthesis structure**:
   - Overview (what's being synthesized)
   - Extracted claims table (from all sources)
   - Argument chains identified
   - Points of agreement
   - Points of conflict / contradictions
   - Scenario matrix (if applicable)
   - Key findings
   - Open questions

4. **Cross-reference**:
   - Link back to source analyses
   - Link back to claim IDs
   - Update sources.yaml `analysis_file` fields if appropriate

5. **Register any new claims** generated by synthesis

6. **Commit**:
   ```bash
   git add analysis/syntheses/[topic]-synthesis.md
   git add claims/registry.yaml reference/sources.yaml
   git commit -m "feat: create [topic] synthesis"
   git push
   ```

---

## 8. Re-Analysis Trigger

**When**: Existing analysis needs revisiting due to new information.

### Triggers
- New evidence significantly changes confidence in key claims
- Prediction status changes
- Contradiction discovered between sources
- New source subsumes or invalidates previous analysis
- Framework methodology updated

### Steps

1. **Document trigger** in the analysis file or a note

2. **Determine scope**:
   - Minor update: Just update claims/confidence
   - Major update: Re-do relevant sections of analysis
   - Full re-analysis: Start fresh with new framework

3. **For minor updates**:
   - Update affected sections in analysis doc
   - Update claims in registry
   - Add changelog entry to analysis doc

4. **For major updates**:
   - Create new version or clearly mark updated sections
   - Re-evaluate all claims from source
   - Update claim versions in registry

5. **Update any affected**:
   - Predictions
   - Dashboards
   - Comparison matrices
   - Syntheses that reference this source

6. **Commit with clear message**:
   ```bash
   git commit -m "refactor: re-analyze [source-id] due to [trigger]"
   git push
   ```

---

## Inbox Management

The `inbox/` folder uses symlinks to track work status without moving files.

### Structure
```
inbox/
├── to-catalog/     # New sources not yet in sources.yaml
├── to-analyze/     # Cataloged sources awaiting analysis
├── in-progress/    # Currently being worked on
└── needs-update/   # Existing analyses flagged for re-evaluation
```

### Commands

**Add to inbox**:
```bash
ln -s ../../reference/primary/[file] inbox/to-analyze/
```

**Move between states**:
```bash
mv inbox/to-analyze/[file] inbox/in-progress/
```

**Complete (remove from inbox)**:
```bash
rm inbox/in-progress/[file]
```

**Flag for update**:
```bash
ln -s ../../analysis/sources/[file] inbox/needs-update/
```

---

## Commit Conventions

| Type | Use for |
|------|---------|
| `feat:` | New analysis, new claims, new predictions |
| `fix:` | Corrections, evidence updates |
| `docs:` | Framework docs, README, process changes |
| `refactor:` | Re-analysis, restructuring |

**No bylines** - keep commit messages clean and descriptive.

---

## Session Checklist

At end of work session:

- [ ] All new claims have IDs and are in registry
- [ ] All sources have `claims_extracted` updated
- [ ] All `[P]` predictions are in predictions.md
- [ ] Run `python scripts/validate.py` and fix any errors
- [ ] Inbox reflects current state
- [ ] Changes committed and pushed
- [ ] AGENTS.md updated if process improved

---

*Last Updated: 2026-01-18*
