# Canonical File Schemas

> **Purpose**: Define exact file formats for data files. Agents should match these schemas.
> **Last Updated**: 2026-01-18

---

## claims/registry.yaml

The claim registry is a YAML file with three top-level keys: `counters`, `claims`, and `chains`.

```yaml
# Counter tracking for ID allocation
counters:
  LABOR: 2      # Next ID would be LABOR-2026-003
  VALUE: 1
  DIST: 4
  GOV: 7
  TECH: 4
  SOCIAL: 0
  RESOURCE: 2
  TRANS: 0
  META: 0

# Claims dictionary, keyed by claim ID
claims:

  TECH-2026-001:                    # ID format: [DOMAIN]-[YYYY]-[NNN]
    text: "The claim text"          # Required: full claim statement
    type: "[F]"                     # Required: [F]/[T]/[H]/[P]/[A]/[C]/[S]/[X]
    domain: "TECH"                  # Required: matches ID domain
    evidence_level: "E2"            # Required: E1-E6
    confidence: 0.80                # Required: 0.0-1.0

    # Provenance
    source_ids:                     # Required: list of source IDs (must exist in sources.yaml)
      - "epoch-2024-training-costs"
    first_extracted: "2026-01-18"   # Required: ISO date
    extracted_by: "claude"          # Required: who extracted

    # Relationships (all claim IDs only, must exist in registry)
    supports: []                    # Claim IDs this evidence supports
    contradicts: []                 # Claim IDs this contradicts
    depends_on: []                  # Claim IDs this requires to be true
    modified_by: []                 # Claim IDs that qualify/refine this

    # Chain membership
    part_of_chain: ""               # Chain ID if part of argument chain, else ""

    # Versioning
    version: 1                      # Increment on significant updates
    last_updated: "2026-01-18"      # ISO date of last change

    # Optional
    notes: "Any additional context" # Optional freeform notes

# Argument chains dictionary, keyed by chain ID
chains:

  CHAIN-2026-001:                   # ID format: CHAIN-[YYYY]-[NNN]
    name: "Permanent Underclass"    # Required: short name
    thesis: "Full thesis statement" # Required: what the chain argues
    confidence: 0.30                # Required: overall chain confidence (≤ weakest link)
    claims:                         # Required: ordered list of claim IDs in chain
      - "LABOR-2026-002"
      - "LABOR-2026-001"
      - "DIST-2026-003"
    analysis_file: "analysis/syntheses/neofeudalism-discourse-synthesis.md"  # Where chain is analyzed
    weakest_link: "Description of weakest link"  # Which step and why

# Statistics (comment block, manually updated)
# Total claims: 20
# Total chains: 3
# Last updated: 2026-01-18
```

### Claim Types

| Type | Symbol | Use When |
|------|--------|----------|
| Fact | `[F]` | Empirically verified, consensus |
| Theory | `[T]` | Coherent explanatory framework |
| Hypothesis | `[H]` | Testable proposition, awaiting evidence |
| Prediction | `[P]` | Future-oriented with conditions |
| Assumption | `[A]` | Underlying premise |
| Counterfactual | `[C]` | Alternative scenario |
| Speculation | `[S]` | Untestable/unfalsifiable |
| Contradiction | `[X]` | Identified logical inconsistency |

### Evidence Levels

| Level | Weight Range |
|-------|--------------|
| E1 | 0.9-1.0 |
| E2 | 0.6-0.8 |
| E3 | 0.5-0.7 |
| E4 | 0.3-0.5 |
| E5 | 0.2-0.4 |
| E6 | 0.0-0.2 |

### ID Allocation

1. Read current counter for domain
2. Increment counter
3. Assign ID: `[DOMAIN]-[YYYY]-[counter]` (zero-pad to 3 digits)
4. Commit counter + claim atomically

---

## reference/sources.yaml

The source registry is a YAML file with a single top-level key: `sources`.

```yaml
sources:

  hotz-2026-three-minutes:          # ID format: [author]-[year]-[shorttitle]

    # Required fields
    type: "BLOG"                    # PAPER/BOOK/REPORT/ARTICLE/BLOG/SOCIAL/CONVO/KNOWLEDGE
    title: "Full Title of Source"
    author:                         # List of authors/handles
      - "George Hotz"
    year: 2026                      # Publication year
    url: "https://..."              # URL or empty string
    accessed: "2026-01-18"          # When we accessed it

    # Quality assessment
    reliability: 0.5                # 0.0-1.0 source reliability
    bias_notes: "Known biases"      # Freeform bias notes

    # Linkage
    claims_extracted:               # List of claim IDs extracted from this source
      - "GOV-2026-001"
    analysis_file: "analysis/..."   # Path to analysis doc, or "" if none

    # Classification
    topics:                         # Freeform topic tags
      - "neofeudalism"
      - "tech-work"
    domains:                        # Domain tags (match claim domains)
      - "LABOR"
      - "DIST"

    # Optional
    status: "analyzed"              # captured/cataloged/extracted/analyzed (optional)
    doi: ""                         # DOI if applicable

# Statistics (comment block)
# Total sources: 8
# By type: CONVO: 2, BLOG: 2, SOCIAL: 2, REPORT: 2
# Last updated: 2026-01-18
```

### Source Types

| Type | Use For |
|------|---------|
| `PAPER` | Academic/research papers |
| `BOOK` | Books, long-form published |
| `REPORT` | Institutional reports (think tanks, govt, orgs) |
| `ARTICLE` | News/magazine articles |
| `BLOG` | Blog posts |
| `SOCIAL` | Twitter threads, social media posts |
| `CONVO` | AI-assisted analysis transcripts |
| `KNOWLEDGE` | Standard/background knowledge (stub entries) |
| `UNCATALOGUED` | Placeholder for sources not yet fully catalogued |

### Source Lifecycle

| Status | Meaning |
|--------|---------|
| `captured` | Raw source saved, not in sources.yaml |
| `cataloged` | Entry in sources.yaml, not analyzed |
| `extracted` | Claims extracted, no full analysis |
| `analyzed` | Full analysis document exists |

---

## tracking/predictions.md

Predictions are tracked in a Markdown file with structured sections.

```markdown
# Prediction Registry

## Status Summary

| Status | Count | Description |
|--------|-------|-------------|
| `[P+]` Confirmed | 0 | Prediction occurred as specified |
| `[P~]` Partially Confirmed | 0 | Core thesis correct, details differ |
| `[P→]` On Track | 0 | Intermediate indicators align |
| `[P?]` Uncertain | 0 | Insufficient data |
| `[P←]` Off Track | 0 | Intermediate indicators diverge |
| `[P!]` Partially Refuted | 0 | Core thesis problematic |
| `[P-]` Refuted | 0 | Prediction clearly failed |
| `[P∅]` Unfalsifiable | 0 | No possible evidence could refute |

**Total Predictions Tracked**: N

---

## Predictions by Domain

### DOMAIN - Description

### [Prediction Title]
- **Claim ID**: DOMAIN-YYYY-NNN       # Must match registry
- **Source**: source-id               # Must exist in sources.yaml
- **Date Made**: YYYY-MM-DD           # When prediction was made
- **Target Date**: YYYY-MM-DD         # When prediction should resolve (or range/condition)
- **Claim**: Full prediction text
- **Falsification Criteria**: What would prove this wrong
- **Verification Criteria**: What would prove this right
- **Status**: [P?]                    # Current status symbol
- **Confidence**: 0.X                 # Current confidence
- **Last Evaluated**: YYYY-MM-DD
- **Related Claims**: [CLAIM-ID-1, CLAIM-ID-2]
- **Evidence Updates**:
  - YYYY-MM-DD: Description of update and impact

---

## Recent Updates

| Date | Prediction ID | Old Status | New Status | Reason |
|------|---------------|------------|------------|--------|

---

## Upcoming Evaluation Triggers

- [ ] Event that should trigger re-evaluation

---

*Last Updated: YYYY-MM-DD*
```

### Prediction Status Symbols

| Symbol | Meaning | Use When |
|--------|---------|----------|
| `[P+]` | Confirmed | Prediction occurred as specified |
| `[P~]` | Partially Confirmed | Core thesis correct, details differ |
| `[P→]` | On Track | Intermediate indicators align |
| `[P?]` | Uncertain | Insufficient data to evaluate |
| `[P←]` | Off Track | Intermediate indicators diverge |
| `[P!]` | Partially Refuted | Core thesis problematic, some elements valid |
| `[P-]` | Refuted | Prediction clearly failed |
| `[P∅]` | Unfalsifiable | No possible evidence could refute |

---

## Validation Rules

These rules should be enforced (manually or by validator):

1. **Claim source_ids**: Every ID in a claim's `source_ids` must exist in `sources.yaml`
2. **Claim relationships**: `supports`, `contradicts`, `depends_on`, `modified_by` must only contain claim IDs that exist in registry
3. **Prediction sync**: Every claim with `type: "[P]"` must have entry in `predictions.md`
4. **Source back-links**: Every source's `claims_extracted` should list claims that reference it
5. **Chain claims**: Every claim ID in a chain's `claims` list must exist in registry
6. **Counter consistency**: Domain counters should be ≥ highest existing ID number for that domain

---

*Schema Version: 1.0*
