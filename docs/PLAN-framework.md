# Framework Development Plan

> **Status**: ACTIVE
> **Created**: 2026-01-18
> **Purpose**: Track reorganization and framework iteration

---

## Current State

### Files We Have

```
/reference/
  primary/blogs/hotz-2026-three-minutes.md             # PRIMARY - Hotz blog post
  primary/blogs/hotz-2026-how-stop.md                  # PRIMARY - Hotz follow-up
  primary/social/teortaxes-2026-thread.md              # PRIMARY - Twitter thread
  transcripts/gpt-2026-01-18-hottakes.md               # TRANSCRIPT - GPT analysis session
  transcripts/gpt-2026-01-18-fiction-hottakes.md       # TRANSCRIPT - GPT session
  sources.yaml                              # Registry (partially populated)
```

### Problems
1. No clear workflow tracking (what's processed vs pending)

---

## Proposed Structure

```
/
├── AGENTS.md                    # Framework (symlink → CLAUDE.md)
├── PLAN-framework.md            # This file - framework dev tracking
│
├── inbox/                       # SYMLINKS to items needing work
│   └── [symlinks to files in reference/ or analysis/]
│
├── reference/                   # All source materials (canonical location)
│   ├── sources.yaml             # Master bibliography
│   ├── primary/                 # Original texts being analyzed
│   │   ├── hotz-2026-three-minutes.md
│   │   ├── hotz-2026-how-stop.md
│   │   └── teortaxes-2026-thread.md
│   └── transcripts/             # AI-assisted analysis sessions
│       ├── gpt-2026-01-18-hottakes.md
│       └── gpt-2026-01-18-fiction-hottakes.md
│
├── claims/                      # Claim registry
│   ├── registry.yaml
│   ├── by-domain/
│   └── chains/
│
├── analysis/                    # Our structured analyses
│   ├── sources/                 # Individual source analyses
│   ├── conversations/           # Extracted findings from transcripts
│   ├── chains/                  # Argument chain breakdowns
│   ├── comparisons/             # Theory comparison matrices
│   └── syntheses/               # Cross-cutting syntheses
│
├── scenarios/                   # Scenario matrices
│
├── tracking/                    # Predictions & dashboards
│   ├── predictions.md
│   ├── dashboards/
│   └── updates/
│
└── frameworks/                  # Theoretical frameworks we develop
```

---

## Naming Conventions

### Source IDs (used in sources.yaml and filenames)

Format: `[author]-[year]-[short-title]`

Examples:
- `hotz-2026-three-minutes`
- `hotz-2026-how-stop`
- `teortaxes-2026-thread`
- `epoch-2024-training-costs`

### Transcript IDs

Format: `[model]-[date]-[topic]`

Examples:
- `gpt-2026-01-18-hottakes`
- `claude-2026-01-18-framework`

### Analysis Files

Format: `[source-id]-analysis.md` or `[topic]-[type].md`

Examples:
- `hotz-2026-three-minutes-analysis.md`
- `neofeudalism-chain.md`
- `post-automation-governance-matrix.md`

### Claim IDs

Format: `[DOMAIN]-[YYYY]-[NNN]`

Examples:
- `TECH-2026-001`
- `LABOR-2026-015`

---

## Inbox/WIP Workflow

The `inbox/` folder contains **symlinks only**, pointing to files that need work.

### Workflow States (via symlink naming or subfolder)

```
/inbox/
  /to-catalog/           # New sources, not yet in sources.yaml
  /to-analyze/           # Cataloged but not analyzed
  /to-extract/           # Transcripts needing claim extraction
  /in-progress/          # Currently being worked on
```

Or simpler - just flat symlinks with prefix:
```
/inbox/
  CATALOG-hotz-2026-three-minutes.md → ../reference/primary/...
  ANALYZE-teortaxes-2026-thread.md → ../reference/primary/...
  EXTRACT-gpt-2026-01-18-hottakes.md → ../reference/transcripts/...
```

### When done:
- Remove symlink from inbox
- File stays in reference/ (canonical location)
- Analysis output goes to analysis/

---

## Migration Tasks

### Phase 1: Reorganize Files

- [x] Create new directory structure
- [x] Rename and move primary sources to `reference/primary/`
  - `reference/20260117-geohotz-perpetualunderclass.md` → `reference/primary/blogs/hotz-2026-three-minutes.md`
  - `reference/20260118-geohotz-howtostop.md` → `reference/primary/blogs/hotz-2026-how-stop.md`
  - `reference/20260118-teortaxes.md` → `reference/primary/social/teortaxes-2026-thread.md`
- [x] Rename and move transcripts to `reference/transcripts/`
  - `reference/RESEARCH-gpt5.2pro-hottakes-analysis.md` → `reference/transcripts/gpt-2026-01-18-hottakes.md`
  - `reference/RESEARCH-gpt5.2pro-fiction-then-hottakes-analysis.md` → `reference/transcripts/gpt-2026-01-18-fiction-hottakes.md`
- [x] Update sources.yaml with correct IDs
- [ ] Set up inbox/ with initial symlinks

### Phase 2: Process Existing Sources

- [ ] Analyze `hotz-2026-three-minutes` → create `analysis/sources/hotz-2026-three-minutes-analysis.md`
- [ ] Analyze `hotz-2026-how-stop` → create analysis
- [ ] Analyze `teortaxes-2026-thread` → create analysis
- [ ] Extract claims from `gpt-2026-01-18-hottakes` transcript
- [ ] Extract claims from `gpt-2026-01-18-fiction-hottakes` transcript
- [ ] Build "permanent underclass" argument chain
- [ ] Create post-automation governance scenario matrix

### Phase 3: Framework Refinements

- [ ] Test templates on real sources, iterate as needed
- [ ] Add any missing claim types or domains discovered
- [ ] Document lessons learned in AGENTS.md changelog

---

## Open Questions

1. **Transcript processing**: Should we create a separate "analysis" for each transcript, or just extract claims directly to registry?

2. **Granularity**: How granular should claim extraction be? Every sentence? Major assertions only?

3. **Cross-referencing**: The transcripts already cite external sources (IEA, Reuters, Epoch AI). Do we:
   - Add those to sources.yaml too?
   - Mark them as "secondary" (cited but not directly analyzed)?
   - Only add if we fetch and analyze the original?

4. **Versioning**: Should we track analysis versions? (e.g., if we re-analyze a source with new framework)

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-01-18 | Separate primary sources from transcripts | Different source types need different handling |
| 2026-01-18 | Use symlinks for inbox/workflow | Keeps canonical files in one place |
| 2026-01-18 | Match filenames to source IDs | Reduces confusion, enables automation |

---

## Notes

*Add working notes, observations, ideas here*

- The GPT transcripts are already quite analytical - we're not starting from raw claims, we're starting from structured critique. May need a "meta-analysis" approach.
- Consider: should this repo eventually have tooling (scripts) to help manage claims/sources? Or stay pure markdown?

---

*Last Updated: 2026-01-18*
