# Prediction Registry

This document tracks predictions extracted from analyzed sources.

See [AGENTS.md](../AGENTS.md#prediction-tracking-rubric) for status symbols and methodology.

---

## Status Summary

| Status | Count | Description |
|--------|-------|-------------|
| `[P+]` Confirmed | 0 | Prediction occurred as specified |
| `[P~]` Partially Confirmed | 0 | Core thesis correct, details differ |
| `[P→]` On Track | 1 | Intermediate indicators align |
| `[P?]` Uncertain | 2 | Insufficient data |
| `[P←]` Off Track | 0 | Intermediate indicators diverge |
| `[P!]` Partially Refuted | 0 | Core thesis problematic |
| `[P-]` Refuted | 0 | Prediction clearly failed |
| `[P∅]` Unfalsifiable | 0 | No possible evidence could refute |

**Total Predictions Tracked**: 3

---

## Predictions by Domain

### TECH - Technology Trajectories

#### $1B+ Training Runs by 2027
- **Claim ID**: TECH-2026-002
- **Source**: epoch-2024-training-costs
- **Date Made**: 2024
- **Target Date**: ~2027
- **Claim**: Largest AI training runs could exceed $1B by approximately 2027
- **Falsification Criteria**: No training run exceeds $500M by end of 2027; trend clearly decelerating
- **Verification Criteria**: Credible reports of $1B+ training runs by major labs
- **Status**: `[P→]`
- **Confidence**: 0.65
- **Last Evaluated**: 2026-01-18
- **Related Claims**: [TECH-2026-001, DIST-2026-001]
- **Evidence Updates**:
  - 2026-01-18: Initial registration. Trend appears on track based on 2-3x annual cost growth.

---

### LABOR - Employment & Automation

#### Full Automation by 2035-2045
- **Claim ID**: LABOR-2026-002
- **Source**: teortaxes-2026-thread
- **Date Made**: 2026-01-17
- **Target Date**: 2035-2045
- **Claim**: Full automation of human labor by 2035-2045
- **Falsification Criteria**: >20% of economic output still requires human labor in 2045; clear new task creation outpacing automation
- **Verification Criteria**: <5% of economic output requires human labor; most industries fully automated
- **Status**: `[P?]`
- **Confidence**: 0.35
- **Last Evaluated**: 2026-01-18
- **Related Claims**: [TECH-2026-003, DIST-2026-003]
- **Evidence Updates**:
  - 2026-01-18: Initial registration. Timeline speculative; "full" undefined. Acemoglu-Restrepo task recomposition framework suggests this may overstate displacement.

---

### DIST - Distribution & Ownership

#### Permanent Underclass by Default
- **Claim ID**: DIST-2026-003
- **Source**: teortaxes-2026-thread
- **Date Made**: 2026-01-17
- **Target Date**: Post-automation (conditional on LABOR-2026-002)
- **Claim**: Post-labor economy leads to permanent underclass by default (absent redistribution)
- **Falsification Criteria**: Post-labor transition occurs with broad-based prosperity; effective redistribution mechanisms emerge naturally
- **Verification Criteria**: Significant labor displacement + wealth concentration + no effective redistribution = permanent underclass formation
- **Status**: `[P?]`
- **Confidence**: 0.30
- **Last Evaluated**: 2026-01-18
- **Related Claims**: [LABOR-2026-002, VALUE-2026-001, GOV-2026-004]
- **Evidence Updates**:
  - 2026-01-18: Initial registration. This is a conditional prediction dependent on LABOR-2026-002. Low confidence because it assumes no redistribution mechanism, which is a political choice not an economic necessity.

---

### VALUE - Value Theory & Pricing

*No predictions registered yet*

---

### GOV - Governance & Policy

*No predictions registered yet*

Note: GOV-2026-002 ("Elites will choose genocide over UBI") is classified as `[S]` Speculation, not `[P]` Prediction, due to unfalsifiability and extreme premises. It is tracked in claims registry but not here.

---

### TRANS - Transition Dynamics

*No predictions registered yet*

---

## Predictions by Source

| Source ID | Predictions | Avg Confidence |
|-----------|-------------|----------------|
| epoch-2024-training-costs | 1 | 0.65 |
| teortaxes-2026-thread | 2 | 0.325 |

---

## Recent Updates

| Date | Prediction ID | Old Status | New Status | Reason |
|------|---------------|------------|------------|--------|
| 2026-01-18 | TECH-2026-002 | - | `[P→]` | Initial registration |
| 2026-01-18 | LABOR-2026-002 | - | `[P?]` | Initial registration |
| 2026-01-18 | DIST-2026-003 | - | `[P?]` | Initial registration |

---

## Upcoming Evaluation Triggers

Events that should trigger re-evaluation of predictions:

- [ ] Major lab announces training run budget (for TECH-2026-002)
- [ ] Significant automation deployment news (for LABOR-2026-002)
- [ ] Major UBI/redistribution policy announcements (for DIST-2026-003)
- [ ] Quarterly review: 2026-Q2

---

*Last Updated: 2026-01-18*
