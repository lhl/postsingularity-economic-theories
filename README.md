# Post-Singularity Economic Theories

A research framework for rigorous analysis of economic theories related to technological singularity, AI-driven transformation, and post-scarcity economics.

## What This Is

This repository serves two purposes:

1. **An analytical framework** for systematically evaluating claims, tracking predictions, and synthesizing across theoretical frameworks
2. **Active research** applying that framework to contemporary discourse about AI, automation, and economic futures

The framework is itself under development—we refine it as we encounter new types of arguments and evidence.

---

## Current Research

### Analyses

| Document | Status | Summary |
|----------|--------|---------|
| [Neofeudalism Discourse Synthesis](analysis/syntheses/neofeudalism-discourse-synthesis.md) | `[DRAFT]` | Synthesis of Jan 2026 Twitter discourse on post-labor economics, permanent underclass thesis, and counter-arguments |

### Claims Registered

**28 claims** across 6 domains, with **3 argument chains** mapped:

| Chain | Thesis | Confidence |
|-------|--------|------------|
| Permanent Underclass | Post-labor → permanent underclass by default | 0.30 |
| Genocide Default | Elites will choose genocide over UBI | 0.10 |
| Open Source De-Darkener | Open models shift power struggle from cognition to infrastructure | 0.60 |

See [claims/registry.yaml](claims/registry.yaml) for full claim database.

### Key Finding So Far

> **Bottleneck control (compute, energy, chips), not model access, determines outcomes.** The "permanent underclass" thesis has weak links (assumes no redistribution); open-source diffusion is already eroding cognitive monopoly claims.

---

## Framework Overview

### Core Methodology

All analysis follows a **three-stage process**:

1. **Descriptive**: Extract claims, identify theoretical lineage, note scope
2. **Evaluative**: Assess coherence, evidence quality, identify assumptions
3. **Dialectical**: Steelman, find counterarguments, synthesize with other theories

### Key Components

| Component | Purpose | File |
|-----------|---------|------|
| **Claim Registry** | Track individual claims with IDs, confidence, relationships | [claims/registry.yaml](claims/registry.yaml) |
| **Source Registry** | Bibliography with metadata and claim back-links | [reference/sources.yaml](reference/sources.yaml) |
| **Prediction Tracking** | Monitor predictions over time with falsification criteria | [tracking/predictions.md](tracking/predictions.md) |
| **Argument Chains** | Map logical dependencies, identify weak links | In registry + analyses |
| **Scenario Matrices** | 2x2 possibility spaces with discriminating indicators | In analyses |

### Claim Classification

| Type | Symbol | Description |
|------|--------|-------------|
| Fact | `[F]` | Empirically verified |
| Theory | `[T]` | Coherent framework with support |
| Hypothesis | `[H]` | Testable, awaiting evidence |
| Prediction | `[P]` | Future-oriented with conditions |
| Assumption | `[A]` | Underlying premise |
| Counterfactual | `[C]` | Alternative scenario |
| Speculation | `[S]` | Unfalsifiable |

### Evidence Hierarchy

| Level | Category | Confidence Weight |
|-------|----------|-------------------|
| E1 | Empirical-Strong | 0.9-1.0 |
| E2 | Empirical-Moderate | 0.6-0.8 |
| E3 | Theoretical-Grounded | 0.5-0.7 |
| E4 | Theoretical-Speculative | 0.3-0.5 |
| E5 | Expert Opinion | 0.2-0.4 |
| E6 | Pure Speculation | 0.0-0.2 |

---

## Repository Structure

```
├── AGENTS.md              # Framework methodology (also CLAUDE.md)
├── README.md              # This file
│
├── docs/                  # Framework development (NOT research)
│   ├── WORKFLOWS.md       # Operational procedures
│   ├── SCHEMA.md          # Data file schemas
│   └── PLAN-framework.md  # Development planning
│
├── scripts/               # Tooling
│   ├── validate.py        # Data integrity validator
│   └── hooks/             # Git hooks
│       └── pre-commit     # Pre-commit validation
│
├── inbox/                 # Work tracking (symlinks)
│   ├── to-catalog/
│   ├── to-analyze/
│   ├── in-progress/
│   └── needs-update/
│
├── reference/             # Source materials
│   ├── sources.yaml       # Master bibliography
│   └── [source files]
│
├── claims/                # Claim database
│   ├── registry.yaml      # Master claim index
│   └── chains/            # Detailed chain analyses
│
├── analysis/              # Our analyses
│   ├── sources/           # Individual source analyses
│   ├── comparisons/       # Theory comparisons
│   └── syntheses/         # Cross-source syntheses
│
├── scenarios/             # Scenario matrices
│
└── tracking/              # Predictions & indicators
    ├── predictions.md
    └── dashboards/        # Indicator dashboards
```

---

## Sources Analyzed

| Source | Author | Type | Reliability |
|--------|--------|------|-------------|
| [Three Minutes to Escape](https://geohot.github.io/blog/jekyll/update/2026/01/17/three-minutes.html) | George Hotz | Blog | 0.5 |
| [How Do I Stop?](https://geohot.github.io/blog/jekyll/update/2026/01/18/how-do-i-stop.html) | George Hotz | Blog | 0.5 |
| Post-labor thread | @teortaxesTex | Social | 0.4 |
| [Greenland endgame post](https://x.com/teortaxesTex/status/2012127205728440495) | @teortaxesTex | Social | 0.3 |
| Genocide > UBI thread | @Xenoimpulse | Social | 0.3 |
| [Training Costs Report](https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models) | Epoch AI | Report | 0.8 |
| [Energy and AI](https://www.iea.org/reports/energy-and-ai/energy-supply-for-ai) | IEA | Report | 0.85 |

Plus 2 AI-assisted analysis transcripts.

---

## Using This Framework

### Setup

```bash
# Clone the repo
git clone https://github.com/lhl/postsingularity-economic-theories.git
cd postsingularity-economic-theories

# Enable pre-commit validation (recommended)
git config core.hooksPath scripts/hooks
```

The pre-commit hook runs `scripts/validate.py` before each commit to ensure data integrity.

### To add a new source
```bash
# 1. Add to reference/
# 2. Register in sources.yaml
# 3. Create inbox symlink
ln -s ../reference/[file] inbox/to-analyze/
```

### To analyze a source
See [docs/WORKFLOWS.md](docs/WORKFLOWS.md) for step-by-step procedures.

### To validate data integrity
```bash
python scripts/validate.py          # Normal mode
python scripts/validate.py --strict # Also check analysis_file paths exist
python scripts/validate.py --json   # Machine-readable output
```

### To query claims
All claims are in `claims/registry.yaml` with:
- Unique IDs (`TECH-2026-001`)
- Confidence scores
- Source back-links
- Relationship mappings (supports, contradicts, depends_on)

---

## Framework Development Status

This framework is actively evolving. Current status:

- [x] Core 3-stage methodology
- [x] Claim registry with IDs and relationships
- [x] Source registry with back-links
- [x] Argument chain notation and detailed chain analyses
- [x] Prediction tracking structure
- [x] Workflow documentation
- [x] Inbox system for work tracking
- [x] Scenario matrix (post-automation governance)
- [x] Indicator dashboard (neofeudalism tracking)
- [x] Automated cross-reference validation (`scripts/validate.py`)
- [x] Pre-commit hook for data integrity
- [ ] File reorganization (sources in legacy locations)

See [docs/PLAN-framework.md](docs/PLAN-framework.md) for development roadmap.

---

## Key Research Questions

1. **Transition Dynamics**: How do economies transition to post-scarcity?
2. **Value Theory**: What happens to value when marginal cost → 0?
3. **Distribution**: Who owns AI/automation means of production?
4. **Labor**: What happens to human work and meaning?
5. **Governance**: What structures handle coordination in post-labor world?
6. **Timeline**: How plausible are 2035-2045 predictions?
7. **Bottlenecks**: Who controls compute, energy, chips?
8. **Multipolarity**: How does state competition affect outcomes?
9. **Counter-strategies**: What "building outside" alternatives exist?

---

## Contributing

This is currently a personal research project. The framework is designed for rigorous idea validation/invalidation—if you're interested in similar analysis, the methodology in [AGENTS.md](AGENTS.md) may be useful.

---

## License

Framework methodology: Open for use/adaptation.
Analyses: Cite appropriately.

---

*Last updated: 2026-01-19*
