# Post-Singularity Economic Theories Research Framework

## Project Purpose

This repository is dedicated to rigorous, systematic analysis of economic theories related to technological singularity, post-scarcity economics, AI-driven economic transformation, and related futurist economic paradigms.

The goal is to move beyond speculation toward structured evaluation: cataloging claims, assessing evidence, tracking predictions, and synthesizing across theoretical frameworks.

---

## Meta-Framework Notes

> **This framework is itself under active development.** As we analyze more sources and encounter new argument structures, we iterate on these tools. The goal is to build a general-purpose analytical engine for rigorous idea validation/invalidation.

### Design Principles
- **File-based first**: All data stored in markdown with embedded metadata for human readability
- **DB-ready**: Metadata formats chosen to enable future migration to structured database
- **Claim-centric**: Individual claims are the atomic unit; everything else (sources, theories, predictions) references claims
- **Relationship-aware**: Track how claims support, contradict, modify, or depend on each other
- **Temporally-aware**: Track when claims were made, evaluated, and updated

### Versioning
When making significant framework changes, increment version and document:
- What changed
- Why it changed
- Migration notes for existing analyses

### Continuous Improvement
**Update this AGENTS.md aggressively** as we refine our process. This document should always reflect current best practices. When you discover a better way to do something, document it here immediately.

### Git Practices
- Commit frequently as work progresses
- Push to remote regularly
- **No bylines or co-author footers in commit messages** - keep them clean and descriptive
- Use conventional commit style when appropriate (feat:, fix:, docs:, refactor:)

---

## Analytical Methodology

All analysis follows a **three-stage process**:

### Stage 1: Descriptive Analysis
- Summarize the source/theory neutrally
- Extract key claims, predictions, and assumptions
- Identify the theoretical lineage (what traditions/thinkers it builds on)
- Note scope and domain (what does this theory attempt to explain?)

### Stage 2: Evaluative Analysis
- Assess internal coherence and logical consistency
- Evaluate evidence quality and empirical grounding
- Identify unstated assumptions and dependencies
- Rate confidence levels using the Evidence Hierarchy (below)
- Flag unfalsifiable claims

### Stage 3: Dialectical Analysis
- Steelman the strongest version of the argument
- Identify strongest counterarguments and counterfactuals
- Map relationships to other theories (supports, contradicts, extends, subsumes)
- Synthesize: where does this fit in the broader theoretical landscape?
- Update theory relationship maps as new sources are analyzed

### Analysis Rigor Levels

Not all analysis needs full rigor. Tag analyses with:

| Level | Tag | Description |
|-------|-----|-------------|
| Exploratory | `[SPITBALL]` | Quick takes, brainstorming, hypothesis generation |
| Working | `[DRAFT]` | Structured but not fully verified |
| Reviewed | `[REVIEWED]` | Full 3-stage analysis, cross-referenced |
| Canonical | `[CANONICAL]` | Authoritative synthesis, periodically updated |

---

## Evidence Hierarchy

Use this hierarchy when evaluating claims:

| Level | Category | Description | Weight |
|-------|----------|-------------|--------|
| E1 | Empirical-Strong | Replicated studies, historical data, verified measurements | 0.9-1.0 |
| E2 | Empirical-Moderate | Single studies, case studies, natural experiments | 0.6-0.8 |
| E3 | Theoretical-Grounded | Logical derivation from well-established principles | 0.5-0.7 |
| E4 | Theoretical-Speculative | Plausible reasoning, extrapolation from trends | 0.3-0.5 |
| E5 | Expert Opinion | Credentialed speculation, informed forecasts | 0.2-0.4 |
| E6 | Pure Speculation | Unfounded claims, sci-fi scenarios, wishful thinking | 0.0-0.2 |

---

## Claim Classification Taxonomy

### By Epistemic Status

| Status | Symbol | Definition |
|--------|--------|------------|
| Fact | `[F]` | Empirically verified, consensus reality |
| Theory | `[T]` | Coherent explanatory framework with some support |
| Hypothesis | `[H]` | Testable proposition, awaiting evidence |
| Prediction | `[P]` | Future-oriented claim with specified conditions |
| Assumption | `[A]` | Unstated or stated premise underlying other claims |
| Counterfactual | `[C]` | Alternative scenario for comparative analysis |
| Speculation | `[S]` | Untestable or unfalsifiable claim |
| Contradiction | `[X]` | Identified logical inconsistency between claims |

### By Domain

- `LABOR` - Employment, automation, human work
- `VALUE` - Value theory, pricing, exchange
- `DIST` - Distribution, inequality, ownership
- `GOV` - Governance, policy, regulation
- `TECH` - Technology trajectories, capabilities
- `SOCIAL` - Social structures, culture, behavior
- `RESOURCE` - Scarcity, abundance, allocation
- `TRANS` - Transition dynamics, pathways
- `META` - Claims about the framework/analysis itself

---

## Claim Registry System

### Claim ID Format

All claims get unique IDs: `[DOMAIN]-[YYYY]-[NNN]`

Example: `TECH-2026-001` = First technology claim registered in 2026

### Claim Record Structure

```yaml
# Claim metadata (embed in markdown or separate YAML)
claim:
  id: "TECH-2026-001"
  text: "Frontier AI training costs grow 2-3x annually"
  type: "[F]"  # Fact/Theory/Hypothesis/Prediction/etc.
  domain: "TECH"
  evidence_level: "E2"
  confidence: 0.75

  # Provenance
  source_ids: ["epoch-2024-training-costs"]
  first_extracted: "2026-01-18"
  extracted_by: "claude"

  # Relationships
  supports: []           # claim IDs this supports
  contradicts: []        # claim IDs this contradicts
  depends_on: []         # claim IDs this requires to be true
  modified_by: []        # claim IDs that qualify/refine this
  part_of_chain: ""      # argument chain ID if applicable

  # Versioning
  version: 1
  last_updated: "2026-01-18"
  update_history: []
```

### Claim Relationship Types

| Relationship | Symbol | Meaning |
|--------------|--------|---------|
| Supports | `→+` | Evidence/logic strengthens target claim |
| Contradicts | `→✗` | Evidence/logic weakens target claim |
| Depends On | `→?` | This claim requires target to be true |
| Modifies | `→~` | Qualifies, refines, or conditions target |
| Subsumes | `→⊃` | This claim includes/generalizes target |
| Part Of | `∈` | Member of a larger argument chain |

---

## Argument Chain Notation

Many arguments are **chains**: A → B → C → Conclusion. Chains fail if any link fails.

### Chain Format

```markdown
## Chain: [CHAIN-ID] [Name]

**Thesis**: [Final conclusion]
**Confidence**: [Overall confidence, usually ≤ weakest link]

### Links

1. **[A]** [First premise/claim]
   - Evidence: [E-level]
   - Confidence: [0.0-1.0]
   - Status: `SOLID` | `CONTESTED` | `WEAK` | `BROKEN`

   ↓ [relationship: implies/requires/suggests]

2. **[B]** [Second claim]
   - Evidence: [E-level]
   - Confidence: [0.0-1.0]
   - Status: `SOLID` | `CONTESTED` | `WEAK` | `BROKEN`

   ↓ [relationship]

3. **[C]** [Conclusion]
   - Evidence: [E-level]
   - Confidence: [0.0-1.0]
   - Status: `SOLID` | `CONTESTED` | `WEAK` | `BROKEN`

### Chain Analysis
- **Weakest Link**: [Which step?]
- **Why Weak**: [Explanation]
- **If Link Breaks**: [What happens to conclusion?]
- **Alternative Paths**: [Can conclusion be reached differently?]
```

### Example: Neofeudalism Chain

```markdown
## Chain: CHAIN-2026-001 "Permanent Underclass"

**Thesis**: Post-labor economy leads to permanent underclass by default
**Confidence**: 0.35 (chain has multiple weak links)

### Links

1. **[A]** AI progress continues on current trajectory → full automation by 2035-2045
   - Evidence: E4 (extrapolation from trends)
   - Confidence: 0.5
   - Status: `CONTESTED` - timeline uncertain, "full" undefined

   ↓ implies

2. **[B]** Full automation → labor becomes economically irrelevant
   - Evidence: E4
   - Confidence: 0.4
   - Status: `WEAK` - ignores task recomposition, new task creation

   ↓ implies

3. **[C]** Labor irrelevant → no consumer purchasing power
   - Evidence: E3
   - Confidence: 0.3
   - Status: `WEAK` - assumes no redistribution mechanism

   ↓ implies

4. **[D]** No purchasing power + concentrated ownership → permanent underclass
   - Evidence: E4
   - Confidence: 0.5
   - Status: `CONTESTED` - political equilibrium claim, not economic law

### Chain Analysis
- **Weakest Link**: Step 3 (labor → no income)
- **Why Weak**: Conflates labor income with all income; ignores transfers, dividends, public provision
- **If Link Breaks**: Conclusion doesn't follow; high automation compatible with mass prosperity
- **Alternative Paths**: Could reach "inequality increases" without "permanent underclass"
```

---

## Scenario Matrix Template

For mapping possibility space across key variables:

### 2x2 Matrix (Standard)

```markdown
## Scenario Matrix: [Topic]

**Axes**:
- X-axis: [Variable 1] (Low ← → High)
- Y-axis: [Variable 2] (Low ← → High)

|                    | [Var1-Low]           | [Var1-High]          |
|--------------------|----------------------|----------------------|
| **[Var2-High]**    | **Quadrant A**       | **Quadrant B**       |
|                    | [Name]               | [Name]               |
|                    | [1-2 sentence desc]  | [1-2 sentence desc]  |
|                    | Likelihood: [L/M/H]  | Likelihood: [L/M/H]  |
|--------------------|----------------------|----------------------|
| **[Var2-Low]**     | **Quadrant C**       | **Quadrant D**       |
|                    | [Name]               | [Name]               |
|                    | [1-2 sentence desc]  | [1-2 sentence desc]  |
|                    | Likelihood: [L/M/H]  | Likelihood: [L/M/H]  |

### Key Discriminating Indicators
- [What evidence would tell us we're moving toward each quadrant?]
```

### Example: Post-Singularity Governance Matrix

```markdown
## Scenario Matrix: Post-Automation Governance

**Axes**:
- X-axis: Bottleneck Control (Diffuse ← → Concentrated)
- Y-axis: Governance Mode (Cooperative ← → Coercive)

|                      | Diffuse Control          | Concentrated Control       |
|----------------------|--------------------------|----------------------------|
| **Cooperative**      | **Pluralistic Abundance**| **Social Dividend State**  |
|                      | Many actors, open tech,  | High inequality but stable |
|                      | broad ownership          | transfers buy legitimacy   |
|                      | Likelihood: Medium       | Likelihood: Medium         |
|----------------------|--------------------------|----------------------------|
| **Coercive**         | **Chaotic Multipolarity**| **Neofeudal/Security State**|
|                      | Many armed actors,       | Oligarchic control,        |
|                      | high conflict risk       | managed/excluded underclass|
|                      | Likelihood: Medium       | Likelihood: Low-Medium     |

### Key Discriminating Indicators
- Bottleneck diffusion: Open model parity with frontier, commodity inference costs
- Governance mode: Expansion vs retrenchment of transfers, rights enforcement
```

---

## Indicator Dashboard Template

For tracking real-world signals that discriminate between scenarios:

```markdown
# Indicator Dashboard: [Topic]

**Purpose**: Track signals that tell us which scenario branch we're on
**Update Frequency**: [Monthly/Quarterly]
**Last Updated**: [YYYY-MM-DD]

## Summary Status

| Scenario | Trend | Confidence |
|----------|-------|------------|
| [Scenario A] | ↑ ↓ → | [0.0-1.0] |
| [Scenario B] | ↑ ↓ → | [0.0-1.0] |

## Indicators

### Category 1: [e.g., Capability Indicators]

| Indicator | Current State | Trend | Favors Scenario | Sources |
|-----------|---------------|-------|-----------------|---------|
| [Indicator 1] | [Value/Status] | ↑↓→ | [Which scenario?] | [refs] |
| [Indicator 2] | [Value/Status] | ↑↓→ | [Which scenario?] | [refs] |

### Category 2: [e.g., Institutional Indicators]

| Indicator | Current State | Trend | Favors Scenario | Sources |
|-----------|---------------|-------|-----------------|---------|
| [Indicator 1] | [Value/Status] | ↑↓→ | [Which scenario?] | [refs] |

## Recent Updates

| Date | Indicator | Change | Implication |
|------|-----------|--------|-------------|
| [YYYY-MM-DD] | [Which] | [What changed] | [What it means] |

## Watch List
- [Upcoming events/releases that could shift indicators]
```

---

## Source Types and Protocols

### Source Type Classification

| Type | Code | Description | Analysis Approach |
|------|------|-------------|-------------------|
| Academic Paper | `PAPER` | Peer-reviewed research | Full Source Analysis Template |
| Book | `BOOK` | Long-form published work | Chapter-by-chapter extraction |
| Report | `REPORT` | Institutional analysis (think tanks, govt) | Full template + institutional bias check |
| Article | `ARTICLE` | News/magazine piece | Quick extraction + fact verification |
| Blog Post | `BLOG` | Individual online writing | Extract claims + author credibility check |
| Social Media | `SOCIAL` | Twitter threads, posts | Extract claims, low initial confidence |
| Conversation | `CONVO` | AI-assisted analysis sessions | Special protocol below |
| Interview | `INTERVIEW` | Q&A format | Extract claims per speaker |
| Dataset | `DATA` | Raw data or statistics | Methodology review |
| Fiction | `FICTION` | Speculative fiction | Extract scenarios/mechanisms, not predictions |

### Conversational Source Protocol

For AI-assisted analysis sessions (like the GPT research transcripts):

```markdown
# Conversational Analysis: [Session Title]

## Session Metadata
- **Source URL**: [if applicable]
- **Date**: [YYYY-MM-DD]
- **Participants**: [human / AI model]
- **Session Type**: [exploratory | analytical | synthesis]
- **Rigor Level**: [SPITBALL | DRAFT | REVIEWED]

## Input Claims (User-Provided)

### Input 1: [Brief label]
- **Original Source**: [Where did user get this?]
- **Raw Text**:
  > [Quoted text user provided for analysis]
- **Extracted Claims**:
  | # | Claim | ID Assigned |
  |---|-------|-------------|
  | 1 | [claim text] | [DOMAIN-YYYY-NNN] |

## Analysis Evolution

### Turn 1: [Topic]
- **User Request**: [What was asked]
- **Key Analytical Moves**:
  - [What the analysis did: steelman, critique, compare, etc.]
- **Claims Generated**:
  | Claim | Type | Confidence | Evidence |
  |-------|------|------------|----------|
  | [text] | [T/H/P] | [0.0-1.0] | [E1-E6] |
- **Sources Cited**: [list]

### Turn 2: [Topic]
[...repeat structure...]

## Synthesis

### Core Findings
- [Bullet points of main conclusions]

### Claims to Register
[List of claims worth adding to registry]

### Argument Chains Identified
[Any A→B→C structures worth formalizing]

### Open Questions
[What wasn't resolved?]

### Suggested Follow-ups
[What should be investigated next?]
```

---

## Bibliography / Source Registry

### Source ID Format

`[author-lastname]-[year]-[short-title]`

Example: `epoch-2024-training-costs`

### Source Record Structure (BibTeX-compatible)

```yaml
source:
  id: "epoch-2024-training-costs"
  type: "REPORT"  # PAPER/BOOK/REPORT/ARTICLE/BLOG/SOCIAL/CONVO/etc.

  # Standard bibliographic fields
  title: "How Much Does It Cost to Train Frontier AI Models?"
  author: ["Epoch AI"]
  year: 2024
  url: "https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models"
  doi: ""

  # Extended metadata
  accessed: "2026-01-18"
  reliability: 0.8  # Source reliability assessment
  bias_notes: "Pro-AI-progress framing but methodologically careful"

  # Relationship to our analysis
  claims_extracted: ["TECH-2026-001", "TECH-2026-002"]
  analysis_file: "analysis/sources/epoch-2024-training-costs.md"

  # Tags
  topics: ["compute", "costs", "frontier-models"]
  domains: ["TECH", "RESOURCE"]
```

### Source Registry File

Maintain `reference/sources.yaml` as master list, with individual BibTeX-style entries.

---

## Prediction Tracking Rubric

For claims tagged as `[P]` Predictions:

| Status | Symbol | Criteria |
|--------|--------|----------|
| Confirmed | `[P+]` | Prediction occurred as specified |
| Partially Confirmed | `[P~]` | Core thesis correct, details differ |
| On Track | `[P→]` | Intermediate indicators align with prediction |
| Uncertain | `[P?]` | Insufficient data to evaluate |
| Off Track | `[P←]` | Intermediate indicators diverge from prediction |
| Partially Refuted | `[P!]` | Core thesis problematic, some elements valid |
| Refuted | `[P-]` | Prediction clearly failed |
| Unfalsifiable | `[P∅]` | No possible evidence could refute |

### Prediction Record Template

```markdown
### [Prediction Title]
- **Claim ID**: [P-DOMAIN-YYYY-NNN]
- **Source**: [source-id]
- **Date Made**: [YYYY-MM-DD]
- **Target Date**: [YYYY-MM-DD or range or condition]
- **Claim**: [Specific prediction text]
- **Falsification Criteria**: [What would prove this wrong?]
- **Verification Criteria**: [What would prove this right?]
- **Status**: [P→]
- **Confidence**: [0.0-1.0]
- **Last Evaluated**: [YYYY-MM-DD]
- **Related Claims**: [claim IDs this connects to]
- **Evidence Updates**:
  - [YYYY-MM-DD]: [Evidence/development and impact on assessment]
```

---

## Source Analysis Template

When analyzing a new document/source:

```markdown
# Source Analysis: [Title]

## Metadata
- **Source ID**: [author-year-shorttitle]
- **Author(s)**:
- **Date**:
- **Type**: [PAPER | BOOK | REPORT | ARTICLE | BLOG | SOCIAL | CONVO]
- **URL/DOI**:
- **Reliability**: [0.0-1.0]
- **Rigor Level**: [SPITBALL | DRAFT | REVIEWED | CANONICAL]

## Stage 1: Descriptive Summary

### Core Thesis
[1-3 sentence summary of main argument]

### Key Claims
| # | Claim | Claim ID | Type | Domain | Evidence Level | Confidence |
|---|-------|----------|------|--------|----------------|------------|
| 1 | | | | | | |

### Argument Structure
[Is this a chain argument? What's the logical flow?]

```
[Claim A]
    ↓ implies
[Claim B]
    ↓ requires
[Claim C]
```

### Theoretical Lineage
[What traditions/thinkers does this build on?]

### Scope & Limitations
[What does this theory attempt to explain? What does it explicitly not address?]

## Stage 2: Evaluation

### Internal Coherence
[Does the argument follow logically? Any contradictions?]

### Identified Contradictions
| Claim 1 | Claim 2 | Nature of Contradiction |
|---------|---------|------------------------|
| | | |

### Evidence Assessment
[Quality and relevance of supporting evidence]

### Unstated Assumptions
| Assumption | Claim ID | Critical? | Problematic? |
|------------|----------|-----------|--------------|
| | | | |

### Weak Links
[If chain argument, which links are weakest?]

### Confidence Assessment
- **Overall Confidence**: [0.0-1.0]
- **Reasoning**:

## Stage 3: Dialectical Analysis

### Steelmanned Argument
[Strongest possible version of this position]

### Strongest Counterarguments
1. [Counter + source if available]
2.

### Supporting Theories
[Other frameworks that align/support - with source IDs]

### Contradicting Theories
[Other frameworks that conflict - with source IDs]

### Synthesis Notes
[How does this update our overall understanding?]

### Claims to Cross-Reference
[Which claims should be checked against other sources?]

---
**Analysis Date**: [YYYY-MM-DD]
**Analyst**: [human/claude]
**Confidence in Analysis**: [0.0-1.0]
```

---

## Theory Comparison Matrix Template

For comparing multiple theories on a topic:

```markdown
# Theory Comparison: [Topic]

| Dimension | Theory A | Theory B | Theory C |
|-----------|----------|----------|----------|
| **Source** | [source-id] | [source-id] | [source-id] |
| **Core Claim** | | | |
| **On Labor** | | | |
| **On Value** | | | |
| **On Distribution** | | | |
| **On Transition** | | | |
| **Key Assumption** | | | |
| **Evidence Level** | | | |
| **Falsifiable?** | | | |
| **Time Horizon** | | | |
| **Confidence** | | | |

## Points of Agreement
- [Where do they converge?]

## Points of Conflict
| Issue | Theory A says | Theory B says | Resolution? |
|-------|---------------|---------------|-------------|
| | | | |

## Synthesis
[Can they be reconciled? What would integration look like?]

## Discriminating Evidence
[What evidence would favor one theory over another?]
```

---

## File Organization

```
/
├── AGENTS.md              # This file (symlinked to CLAUDE.md)
├── README.md              # Project overview
│
├── reference/             # Original source documents + registry
│   ├── sources.yaml       # Master source bibliography
│   ├── papers/
│   ├── books/
│   ├── articles/
│   ├── conversations/     # AI-assisted analysis transcripts
│   └── data/
│
├── claims/                # Claim registry
│   ├── registry.yaml      # Master claim index
│   ├── by-domain/         # Claims organized by domain
│   │   ├── TECH.md
│   │   ├── LABOR.md
│   │   └── ...
│   └── chains/            # Argument chain analyses
│
├── analysis/              # Completed analyses
│   ├── sources/           # Individual source analyses
│   ├── comparisons/       # Theory comparison matrices
│   └── syntheses/         # Cross-cutting synthesis documents
│
├── tracking/              # Prediction and indicator tracking
│   ├── predictions.md     # Master prediction registry
│   ├── dashboards/        # Indicator dashboards
│   └── updates/           # Chronological evidence updates
│
├── scenarios/             # Scenario matrices and analysis
│
└── frameworks/            # Theoretical frameworks and taxonomies
```

---

## Research Protocols

### When Analyzing a New Source
1. Assign source ID: `[author]-[year]-[shorttitle]`
2. Add to `reference/sources.yaml`
3. Add raw source to appropriate `reference/` subfolder
4. Create analysis document in `analysis/sources/`
5. Extract claims and assign claim IDs
6. Add claims to `claims/registry.yaml` and domain files
7. Add any predictions to `tracking/predictions.md`
8. Identify argument chains; create chain analyses if significant
9. Update relevant comparison matrices and scenario matrices
10. Note any theories/claims that need re-evaluation

### When Extracting Claims from Conversations
1. Use Conversational Source Protocol template
2. Distinguish between:
   - Claims user provided for analysis (input claims)
   - Claims generated by analysis (output claims)
3. Track analytical evolution through conversation
4. Synthesize at end: what's worth registering?
5. Assign lower initial confidence to conversational claims
6. Flag for verification against primary sources

### When Searching for Supporting/Counterfactual Evidence
1. Clearly state the claim being investigated (with claim ID)
2. Search for both supporting AND contradicting evidence
3. Document search methodology and sources consulted
4. Rate evidence quality using Evidence Hierarchy
5. Update claim confidence levels based on findings
6. Update claim relationships (supports/contradicts)

### When Updating Prediction Status
1. Document the new evidence/development
2. Re-evaluate against falsification criteria
3. Update status symbol and confidence
4. Add entry to Evidence Updates log
5. If status change is significant, note implications for related claims
6. Update relevant indicator dashboards

### When Building/Updating Dashboards
1. Define discriminating indicators for each scenario
2. Set update frequency appropriate to indicator volatility
3. On each update:
   - Record current state and trend
   - Note which scenario(s) the evidence favors
   - Update scenario probability assessments
   - Log significant changes

---

## Key Research Questions

This framework is designed to help investigate questions such as:

1. **Transition Dynamics**: How do economies transition to post-scarcity? What are plausible pathways?
2. **Value Theory**: What happens to economic value when marginal production cost approaches zero?
3. **Distribution**: Who owns the means of production in an AI-driven economy? What distribution mechanisms are proposed?
4. **Labor**: What happens to human labor? What theories exist for meaning/purpose/income in post-labor scenarios?
5. **Governance**: What governance structures are proposed? How do they handle coordination and conflict?
6. **Timeline**: What are the predicted timelines? How do we evaluate their plausibility?
7. **Risks**: What failure modes and risks are identified? How seriously should we take them?
8. **Bottlenecks**: What are the actual chokepoints (compute, energy, chips, data)? Who controls them?
9. **Multipolarity**: How does competition between states/blocs affect outcomes?
10. **Counter-strategies**: What "building outside" alternatives exist? How viable are they?

---

## Agent Instructions

When working on this project:

- **Be rigorous**: Follow the three-stage methodology consistently
- **Be balanced**: Actively seek counterfactuals, not just confirmation
- **Be precise**: Use the classification taxonomies and evidence hierarchy
- **Be humble**: Clearly distinguish confidence levels; speculation is allowed but must be labeled
- **Be cumulative**: Each analysis should build on and reference previous work
- **Be updateable**: All assessments should include falsification criteria and be revisable
- **Be ID-aware**: Assign and use claim IDs to enable cross-referencing
- **Be chain-aware**: Look for argument chains and identify weak links
- **Be meta-aware**: Note when the framework itself needs updating

### When asked to analyze a source:
1. First check if it's already in `analysis/sources/`
2. Determine source type and use appropriate template
3. Assign source ID and claim IDs as you extract
4. Be thorough on Stage 1 before moving to evaluation
5. Cross-reference with existing claims in Stage 3
6. Update claim registry with new claims

### When asked to compare theories:
1. Check for existing comparison matrices
2. Use the Theory Comparison Matrix Template
3. Ensure all theories have been individually analyzed first
4. Identify discriminating evidence

### When asked to update predictions:
1. Check `tracking/predictions.md` for the relevant prediction
2. Document what triggered the update
3. Be conservative about status changes (require strong evidence)
4. Update related indicator dashboards

### When asked to build scenarios:
1. Identify key variables that drive different outcomes
2. Build scenario matrix with named quadrants
3. Assess likelihood for each scenario
4. Define discriminating indicators
5. Create or update relevant dashboard

---

## Confidence Calibration

To maintain well-calibrated confidence:

- **0.9-1.0**: Would bet significant resources; very strong evidence
- **0.7-0.8**: Confident but acknowledge meaningful uncertainty
- **0.5-0.6**: Genuine uncertainty; could go either way
- **0.3-0.4**: Lean against but not confident
- **0.1-0.2**: Strongly doubt but can't rule out
- **0.0-0.1**: Would bet heavily against; extraordinary evidence needed

When aggregating across claims, note that:
- A theory with many 0.7 confidence claims is not itself 0.7 confidence
- Confidence in overall theory depends on logical structure and weakest critical links
- Chain arguments: overall confidence ≤ weakest link
- Explicitly model dependencies when possible

---

## Reading Lists

When building reading lists from source analysis:

```markdown
## Reading List: [Topic]

### Tier 1: Essential (Start Here)
1. **[Title]** by [Author] - [1 sentence why]
2. ...

### Tier 2: Deep Dive
1. **[Title]** by [Author] - [1 sentence why]
2. ...

### Tier 3: Specialized
1. **[Title]** by [Author] - [1 sentence why]
2. ...

### Suggested Path
[Ordered sequence for building understanding]
1. Start with X to get [foundation]
2. Then Y for [next layer]
3. Then Z for [synthesis/critique]
```

---

*Framework Version: 2.0*
*Last Updated: 2026-01-18*
*Changelog*:
- v2.0: Added claim registry, argument chains, scenario matrices, indicator dashboards, conversational source protocol, source registry with bibtex-style metadata, meta-framework section
- v1.0: Initial framework with 3-stage analysis, evidence hierarchy, prediction tracking
