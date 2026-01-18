# Implementation: Framework Gap Analysis Improvements

> **Sprint**: 2026-01-19
> **Triggered by**: [Meta-Analysis: Framework Efficacy Test](../analysis/meta/framework-efficacy-greenland-test.md)
> **Status**: Complete

---

## Summary

Based on comparing framework-guided vs raw analysis of the Greenland Endgame source, we identified 5 gaps in the Source Analysis Template. This document tracks implementation of fixes.

## Gap Analysis (from META claims)

| Gap | Claim ID | Impact | Fix |
|-----|----------|--------|-----|
| Under-prompts for fact-checking | META-2026-003 | High | Add Fact-Check Table |
| Missing rhetorical analysis | META-2026-004 | Medium | Add Persuasion Techniques section |
| Missing internal tension detection | META-2026-007 | Medium | Add Internal Tensions field |
| No evidence anchors in claim tables | META-2026-008 | High | Extend Key Claims table |
| Evidence levels not legible | (GPT noted) | Low | Add rubric to template header |

---

## Punchlist

### Source Analysis Template Updates (CLAUDE.md)

- [x] **1.1** Add Evidence Level rubric after Metadata block
- [x] **1.2** Extend Key Claims table with Verified? and Falsifiable By columns
- [x] **1.3** Add "Key Factual Claims Verified" section to Stage 2
- [x] **1.4** Add "Internal Tensions / Self-Contradictions" section to Stage 2
- [x] **1.5** Add "Persuasion Techniques" section to Stage 2

### Meta-Framework Updates (CLAUDE.md)

- [x] **2.1** Add guidance that major framework improvements should create IMPLEMENTATION docs

### Workflow Updates (WORKFLOWS.md)

- [x] **3.1** Add new Stage 2 sections to analysis checklist
- [x] **3.2** Note that fact-checking is now expected

### Validation

- [x] **4.1** Run `python scripts/validate.py`
- [x] **4.2** Commit and push

---

## Worklog

### 2026-01-19

**Session start**: Implementing framework improvements from meta-analysis

| Time | Action | Status |
|------|--------|--------|
| - | Created this implementation doc | Done |
| - | Item 1.1: Evidence Level rubric | Done |
| - | Item 1.2: Extended Key Claims table (Verified?, Falsifiable By) | Done |
| - | Item 1.3: Fact-Check Table | Done |
| - | Item 1.4: Internal Tensions section | Done |
| - | Item 1.5: Persuasion Techniques section | Done |
| - | Item 2.1: Meta-framework guidance (IMPLEMENTATION docs) | Done |
| - | Item 3.1-3.2: Workflow updates | Done |
| - | Item 4.1-4.2: Validation and commit | Done |

**Session complete**: All items implemented.

---

## Template Diffs

### 1.1 Evidence Level Rubric

**Add after Metadata block:**
```markdown
> **Evidence Levels**: E1=Replicated empirical | E2=Single study/case | E3=Grounded theory | E4=Speculative theory | E5=Expert opinion | E6=Pure speculation
```

### 1.2 Extended Key Claims Table

**Before:**
```markdown
| # | Claim | Claim ID | Type | Domain | Evidence Level | Confidence |
```

**After:**
```markdown
| # | Claim | Claim ID | Type | Domain | Evid | Conf | Verified? | Falsifiable By |
```

### 1.3 Fact-Check Table

**New section in Stage 2:**
```markdown
### Key Factual Claims Verified

| Claim (paraphrased) | Source Says | Actual | Source | Status |
|---------------------|-------------|--------|--------|--------|
| [claim] | [assertion] | [verified value] | [URL/ref] | ✓/✗/? |
```

### 1.4 Internal Tensions Section

**New section in Stage 2:**
```markdown
### Internal Tensions / Self-Contradictions

| Tension | Parts in Conflict | Implication |
|---------|-------------------|-------------|
| [description] | [A] vs [B] | [what it means] |
```

### 1.5 Persuasion Techniques Section

**New section in Stage 2:**
```markdown
### Persuasion Techniques

| Technique | Example | Effect on Reader |
|-----------|---------|------------------|
| [e.g., Composition fallacy] | [quote] | [how it biases] |
```

---

## Success Criteria

- [x] All 5 new sections present in CLAUDE.md Source Analysis Template
- [x] WORKFLOWS.md updated with new checklist items
- [x] Meta-framework guidance added for implementation docs
- [x] Validation passes
- [ ] Next source analysis uses updated template

---

## Notes

- This is the first use of the IMPLEMENTATION doc pattern
- Future major framework changes should follow this structure
- Keep worklog updated as items complete

---

*Created: 2026-01-19*
*Last Updated: 2026-01-19*
