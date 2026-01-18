# Implementation: Robustness Fixes

> **Sprint**: 2026-01-19
> **Triggered by**: GPT 5.2 Pro feedback on framework gap analysis improvements
> **Status**: Complete

---

## Summary

After implementing the initial framework gap analysis improvements, we shared the updated framework with GPT 5.2 Pro for review. It identified that while our changes address the major gaps, there are 4 additional minimal fixes needed to prevent common framework failure modes:

1. **Checking easy facts while the thesis escapes untouched**
2. **Mistaking structure + scores for grounded verification**

## GPT 5.2 Pro Feedback (verbatim)

### What's Still Missing or Under-Specified

#### A) Evidence-level rubric creates confusion

> You propose:
> E1=Replicated empirical … E4=Speculative theory … E5=Expert opinion … E6=Pure speculation
>
> Two issues:
> 1. **You're mixing evidence *type* with evidence *strength*.** "Expert opinion" can be stronger than "single case" in some domains and weaker in others. "Speculative theory" is a type, not a strength.
> 2. **The ordering is ambiguous.** Is E5 better than E4? In practice, analysts will diverge.
>
> **Minimal fix:** split into two fields:
> * **Evidence Type:** {Primary doc, Secondary reporting, Quant dataset, Expert commentary, Analyst inference, Source assertion}
> * **Evidence Strength:** {High / Medium / Low} (or 1–5) with a short rubric
>
> If you insist on one scalar "E-level," then redefine it as *strength only* and keep type separate.

#### B) Fact-check table can devolve into checking trivia

> The temptation is to verify easy numbers (oil reserves, manufacturing share) and leave the hard claims ("unified U.S. strategy," "end trade," "elite worldview drives policy") at "unverified."
>
> **Minimal fix:** require that the fact-check table includes:
> * **at least 1 "crux" claim verification attempt**, not just peripheral numerics
> * **at least 1 disconfirming search**

#### C) No explicit adversarial check prompt

> Frameworks naturally bias toward *organizing* what's in the source. You need a systematic counterweight: "try to break it."
>
> **Minimal fix:** add a one-liner requirement in Stage 2:
> > For the top 2–3 claims, perform a quick search for the strongest counterevidence or alternative explanation; record it.
>
> Even if it's 5 minutes, it changes behavior.

#### D) Media/images are a blind spot

> Given how often viral threads use:
> * miscaptioned screenshots,
> * out-of-context charts,
> * fake "leaks,"
> * or memes that silently carry the "evidence,"
>
> …you probably want at least a minimal "media handling" step.
>
> **Minimal fix:** Stage 1 add:
> * **Media artifacts present?** Y/N
> * If yes: describe what they depict and whether they are evidentiary or decorative.
> * If evidentiary: "verify or mark unverified."

### GPT's Recommended "4 Small Requirements"

> If you do **only four extra things**, do these:
> 1. **Split evidence into Type + Strength** (or clarify E-level so it's unambiguous).
> 2. **Require at least one crux-claim verification attempt** per source.
> 3. **Require one disconfirming search** for top claims.
> 4. **Add a media/images handling checkbox** (Y/N + quick disposition).

### GPT's "Definition of Done" for High-Value Sources

> A high-value source analysis is "done" when:
> * Top 3 claims each have:
>   * an anchor (supporting baseline),
>   * an alternative explanation,
>   * and a disconfirming indicator.
> * At least one internal tension (or explicitly "none found after scan").
> * Rhetoric section has at least 3 techniques + their epistemic effect.
> * Confidence scores include a 1–2 sentence justification tied to evidence strength and alternatives.

---

## Our Implementation Plan

### Fix 1: Clarify Evidence Levels (Type vs Strength)

**Decision**: Keep single E-level scale but redefine as **strength-only**. Add separate `Evidence Type` guidance.

**Rationale**: Splitting into two columns adds complexity to every claim table. Instead, clarify that E-levels measure *strength of support for the claim*, and provide type as context.

**Changes**:
- Update Evidence Hierarchy table description to emphasize "strength of support"
- Add Evidence Type guidance (optional annotation)
- Update rubric in template header

### Fix 2: Crux-Claim Verification Requirement

**Changes**:
- Add note to Key Factual Claims Verified section requiring ≥1 crux claim attempt
- Add "Crux?" column to fact-check table

### Fix 3: Disconfirming Evidence Search

**Changes**:
- Add new "Disconfirming Evidence Search" section to Stage 2
- Simple table: Claim | Counterevidence Found | Alternative Explanation | Search Performed

### Fix 4: Media Artifacts Handling

**Changes**:
- Add `Media Artifacts: Y/N` to Metadata section
- Add conditional guidance for evidentiary vs decorative media

---

## Punchlist

### CLAUDE.md Updates

- [x] **1.1** Clarify Evidence Hierarchy as strength-focused; add type guidance
- [x] **1.2** Update template header rubric with clarified E-levels
- [x] **1.3** Add "Crux?" column and requirement note to Fact-Check table
- [x] **1.4** Add "Disconfirming Evidence Search" section to Stage 2
- [x] **1.5** Add "Media Artifacts" field to Metadata section

### WORKFLOWS.md Updates

- [x] **2.1** Add disconfirming search to Stage 2 requirements
- [x] **2.2** Note crux-claim and media handling requirements

### Validation

- [x] **3.1** Run `python scripts/validate.py`
- [x] **3.2** Commit and push

---

## Worklog

### 2026-01-19

**Session start**: Implementing robustness fixes from GPT 5.2 Pro feedback

| Time | Action | Status |
|------|--------|--------|
| - | Created this implementation doc | Done |
| - | Item 1.1: Clarify Evidence Hierarchy | Done |
| - | Item 1.2: Update template rubric | Done |
| - | Item 1.3: Crux-claim requirement | Done |
| - | Item 1.4: Disconfirming Evidence Search | Done |
| - | Item 1.5: Media Artifacts field | Done |
| - | Item 2.1-2.2: Workflow updates | Done |
| - | Item 3.1-3.2: Validation and commit | Done |

**Session complete**: All items implemented.

---

## Template Diffs

### 1.1 Evidence Hierarchy Clarification

**Before** (description):
> Use this hierarchy when evaluating claims:

**After**:
> Use this hierarchy to rate **strength of evidential support** for claims. E-levels measure how well-supported a claim is, not the type of evidence.
>
> **Evidence Types** (for context, not scoring): Primary document, Secondary reporting, Quantitative dataset, Expert commentary, Analyst inference, Source assertion

### 1.2 Template Header Rubric

**Before**:
```markdown
> **Evidence Levels**: E1=Replicated empirical | E2=Single study/case | E3=Grounded theory | E4=Speculative theory | E5=Expert opinion | E6=Pure speculation
```

**After**:
```markdown
> **Evidence Strength (E-level)**: E1=Strong empirical (replicated) | E2=Moderate empirical (single study) | E3=Strong theoretical (grounded) | E4=Weak theoretical (speculative) | E5=Opinion/forecast | E6=Unsupported assertion
```

### 1.3 Fact-Check Table with Crux Requirement

**Before**:
```markdown
### Key Factual Claims Verified
| Claim (paraphrased) | Source Says | Actual | External Source | Status |
|---------------------|-------------|--------|-----------------|--------|
| [e.g., "China makes 50% of stuff"] | [assertion] | [verified] | [URL/ref] | ✓ / ✗ / ? |
```

**After**:
```markdown
### Key Factual Claims Verified

> **Requirement**: Must include ≥1 **crux claim** (central to thesis), not just peripheral numerics.

| Claim (paraphrased) | Crux? | Source Says | Actual | External Source | Status |
|---------------------|-------|-------------|--------|-----------------|--------|
| [e.g., "China makes 50% of stuff"] | N | [assertion] | [verified] | [URL/ref] | ✓ / ✗ / ? |
| [e.g., "Elite consensus on X policy"] | **Y** | [assertion] | [verified or ?] | [URL/ref] | ✓ / ✗ / ? |
```

### 1.4 Disconfirming Evidence Search Section

**New section in Stage 2** (after Fact-Check table):
```markdown
### Disconfirming Evidence Search

> For top 2-3 claims, actively search for counterevidence or alternative explanations.

| Claim | Counterevidence Found | Alternative Explanation | Search Notes |
|-------|----------------------|------------------------|--------------|
| [top claim 1] | [what contradicts it] | [other way to explain] | [what you searched] |
| [top claim 2] | [what contradicts it] | [other way to explain] | [what you searched] |
```

### 1.5 Media Artifacts Field

**Add to Metadata section**:
```markdown
- **Media Artifacts**: [Y/N] — If Y: [describe what they depict, whether evidentiary or decorative, verified status]
```

---

## Success Criteria

- [x] Evidence Hierarchy clarified as strength-focused
- [x] Fact-check table requires crux claim attempt
- [x] Disconfirming Evidence Search section added
- [x] Media Artifacts field added to metadata
- [x] WORKFLOWS.md updated
- [x] Validation passes
- [ ] Next source analysis uses updated template

---

## Notes

- This is the second use of the IMPLEMENTATION doc pattern
- These fixes specifically target "framework theater" failure modes
- GPT also suggested rhetorical taxonomy and confidence justification format - deferred for now

---

*Created: 2026-01-19*
*Last Updated: 2026-01-19*
