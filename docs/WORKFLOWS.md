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
| Improve the framework itself | [9. Framework Improvement](#9-framework-improvement) |

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
     - Include Verified? and Falsifiable By columns in Key Claims table
     - Note Media Artifacts (Y/N) in metadata
   - Stage 2: Evaluation (must include):
     - Key Factual Claims Verified (≥1 crux claim, not just peripheral facts)
     - Disconfirming Evidence Search (top 2-3 claims)
     - Internal Tensions / Self-Contradictions
     - Persuasion Techniques
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

6. **Update Current Research list (if applicable)**:
   - If this analysis represents a *new* topic or materially advances an existing one, add it to `README.md` under **Current Research → Analyses**
   - If claim totals/domains changed, update the counts in `README.md` under **Claims Registered**

7. **Remove from inbox**:
   ```bash
   rm inbox/to-analyze/[filename]
   ```

8. **Commit all together**:
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

6. **Update README.md**:
   - Add entry to Analyses table
   - Update claim/source counts if changed

7. **Commit**:
   ```bash
   git add analysis/syntheses/[topic]-synthesis.md
   git add claims/registry.yaml reference/sources.yaml README.md
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

## 9. Framework Improvement

**When**: The framework itself needs updating—new template sections, workflow changes, methodology refinements.

### Triggers

- External feedback (e.g., GPT/Claude review of outputs)
- Meta-analysis reveals gaps (comparing framework vs raw analysis)
- Repeated friction in existing workflows
- New source types require new handling
- Validation script needs enhancement

### Determine Scope

| Scope | Criteria | Approach |
|-------|----------|----------|
| **Minor** | Single field addition, typo fix, clarification | Direct edit → commit |
| **Major** | New template sections, workflow changes, multiple files | IMPLEMENTATION doc |
| **Meta-analysis** | Testing framework efficacy | Create `analysis/meta/` doc first |

### Path A: Minor Fixes

1. **Edit directly** in CLAUDE.md/AGENTS.md or WORKFLOWS.md
2. **Run validation**: `python scripts/validate.py`
3. **Commit**:
   ```bash
   git add [files]
   git commit -m "docs: [describe fix]"
   git push
   ```

### Path B: Major Changes (IMPLEMENTATION doc)

1. **Create implementation doc**:
   ```bash
   touch docs/IMPLEMENTATION-[change-name].md
   ```

2. **Document the change** using this structure:
   ```markdown
   # Implementation: [Change Name]

   > **Sprint**: [YYYY-MM-DD]
   > **Triggered by**: [What prompted this?]
   > **Status**: In Progress

   ## Summary
   [What's changing and why]

   ## Punchlist
   - [ ] Item 1
   - [ ] Item 2

   ## Worklog
   | Time | Action | Status |
   |------|--------|--------|

   ## Template Diffs
   [Show before/after for template changes]

   ## Success Criteria
   - [ ] Criterion 1
   - [ ] Criterion 2
   ```

3. **Work through punchlist**, updating worklog as items complete

4. **Update CLAUDE.md/AGENTS.md** with new template sections

5. **Update WORKFLOWS.md** if procedures changed

6. **Run validation and commit**:
   ```bash
   python scripts/validate.py
   git add docs/IMPLEMENTATION-[name].md AGENTS.md docs/WORKFLOWS.md
   git commit -m "feat: implement [change-name]"
   git push
   ```

7. **Mark implementation doc as complete** (Status: Complete, check success criteria)

### Path C: Meta-Analysis (Framework Testing)

Use this when you want to test whether the framework is working well.

1. **Select a source** analyzed both with and without framework (or analyze same source twice)

2. **Create meta-analysis doc**:
   ```bash
   touch analysis/meta/[topic]-[test-type].md
   ```

3. **Compare outputs** systematically:
   - What did framework catch that raw missed?
   - What did raw catch that framework missed?
   - Where do confidence levels diverge?

4. **Extract META claims** about framework efficacy:
   - Assign IDs: `META-[YYYY]-[NNN]`
   - Add to `claims/registry.yaml`

5. **Identify gaps** → feeds into Path B if significant

6. **Update sources.yaml** with meta-analysis source entry

7. **Commit**:
   ```bash
   git add analysis/meta/[file] claims/registry.yaml reference/sources.yaml
   git commit -m "feat: meta-analysis [topic]"
   git push
   ```

### Path D: External Feedback Integration

When someone (human or AI) reviews framework outputs and provides feedback:

1. **Capture feedback** in a transcript or note
   - Add to `reference/transcripts/` if substantive

2. **Triage feedback items**:
   - Actionable vs nice-to-have
   - Minor fix vs major change

3. **For actionable items**:
   - Minor → Path A
   - Major → Path B (include verbatim feedback in IMPLEMENTATION doc)

4. **Register as source** if feedback is substantive:
   ```yaml
   [reviewer]-[date]-[topic]:
     type: "CONVO"
     # ... standard fields
   ```

### Examples

**Minor fix**: "Add a column to the claims table"
→ Direct edit to CLAUDE.md, commit

**Major change**: "Add fact-checking, rhetoric analysis, and internal tensions sections"
→ Create `IMPLEMENTATION-gap-analysis-improvement.md`, work through punchlist

**Meta-analysis**: "Compare framework output to raw GPT analysis of same source"
→ Create `analysis/meta/framework-efficacy-[source].md`, extract META claims

**External feedback**: "GPT 5.2 Pro suggests 4 robustness fixes"
→ Create `IMPLEMENTATION-robustness-fixes.md` with verbatim feedback, implement

### Output

- Updated CLAUDE.md/AGENTS.md (templates, methodology)
- Updated WORKFLOWS.md (procedures)
- IMPLEMENTATION doc (for major changes)
- META claims in registry (for meta-analyses)

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
- [ ] **README.md updated if new analysis added** (Analyses table, claim counts)
- [ ] Changes committed and pushed
- [ ] AGENTS.md updated if process improved

---

## Housekeeping: README Updates

When adding new analyses, update `README.md`:

1. **Analyses table**: Add row with document link, status, summary
2. **Claims count**: Update "X claims across Y domains"
3. **Sources count**: Update transcript count if applicable
4. **Repo structure**: Add new directories to tree if created

This ensures the project overview stays current.

---

*Last Updated: 2026-01-19*
