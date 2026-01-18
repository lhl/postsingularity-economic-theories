#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml

CLAIM_ID_RE = re.compile(r"^[A-Z]+-\d{4}-\d{3}$")
CHAIN_ID_RE = re.compile(r"^CHAIN-\d{4}-\d{3}$")

ALLOWED_CLAIM_TYPES = {"[F]", "[T]", "[H]", "[P]", "[A]", "[C]", "[S]", "[X]"}
ALLOWED_EVIDENCE_LEVELS = {f"E{i}" for i in range(1, 7)}


@dataclass(frozen=True)
class Finding:
    level: str  # "ERROR" | "WARN"
    code: str
    message: str


def _load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text())
    except FileNotFoundError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"Failed to parse YAML: {path}: {exc}") from exc


def _is_probability(value: Any) -> bool:
    if not isinstance(value, (int, float)):
        return False
    return 0.0 <= float(value) <= 1.0


def _as_str_list(value: Any) -> list[str] | None:
    if not isinstance(value, list):
        return None
    if not all(isinstance(item, str) for item in value):
        return None
    return value


def _validate_claims_and_chains(
    *,
    findings: list[Finding],
    claims_data: dict[str, Any],
    sources_by_id: dict[str, Any],
    strict_paths: bool,
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, int], dict[str, list[str]]]:
    counters = claims_data.get("counters")
    claims_by_id = claims_data.get("claims")
    chains_by_id = claims_data.get("chains")

    if not isinstance(counters, dict):
        findings.append(Finding("ERROR", "CLAIMS_SCHEMA_COUNTERS", "Missing/invalid top-level `counters` in claims registry"))
        counters = {}
    if not isinstance(claims_by_id, dict):
        findings.append(Finding("ERROR", "CLAIMS_SCHEMA_CLAIMS", "Missing/invalid top-level `claims` in claims registry"))
        claims_by_id = {}
    if not isinstance(chains_by_id, dict):
        findings.append(Finding("ERROR", "CLAIMS_SCHEMA_CHAINS", "Missing/invalid top-level `chains` in claims registry"))
        chains_by_id = {}

    claim_ids = set(claims_by_id.keys())
    source_ids = set(sources_by_id.keys())
    chain_ids = set(chains_by_id.keys())

    # Track per-domain maxima for counter consistency checks.
    max_year_by_domain: dict[str, int] = {}
    max_num_by_domain_year: dict[tuple[str, int], int] = {}

    for claim_id, claim in claims_by_id.items():
        if not isinstance(claim_id, str) or not CLAIM_ID_RE.match(claim_id):
            findings.append(Finding("ERROR", "CLAIM_ID_FORMAT", f"Invalid claim ID format: {claim_id!r}"))
            continue
        if not isinstance(claim, dict):
            findings.append(Finding("ERROR", "CLAIM_ENTRY_TYPE", f"{claim_id}: claim entry must be a mapping"))
            continue

        domain_from_id, year_str, num_str = claim_id.split("-")
        claim_year = int(year_str)
        claim_num = int(num_str)

        max_year_by_domain[domain_from_id] = max(max_year_by_domain.get(domain_from_id, 0), claim_year)
        max_num_by_domain_year[(domain_from_id, claim_year)] = max(
            max_num_by_domain_year.get((domain_from_id, claim_year), 0), claim_num
        )

        # Required fields (lightweight, focused on integrity rules).
        claim_type = claim.get("type")
        if claim_type not in ALLOWED_CLAIM_TYPES:
            findings.append(
                Finding("ERROR", "CLAIM_TYPE", f"{claim_id}: invalid/missing `type` (got {claim_type!r})")
            )

        claim_domain = claim.get("domain")
        if claim_domain != domain_from_id:
            findings.append(
                Finding(
                    "ERROR",
                    "CLAIM_DOMAIN",
                    f"{claim_id}: domain mismatch (ID domain {domain_from_id!r} vs field {claim_domain!r})",
                )
            )

        evidence_level = claim.get("evidence_level")
        if evidence_level not in ALLOWED_EVIDENCE_LEVELS:
            findings.append(
                Finding("ERROR", "CLAIM_EVIDENCE_LEVEL", f"{claim_id}: invalid/missing `evidence_level` (got {evidence_level!r})")
            )

        confidence = claim.get("confidence")
        if not _is_probability(confidence):
            findings.append(
                Finding("ERROR", "CLAIM_CONFIDENCE", f"{claim_id}: invalid/missing `confidence` (got {confidence!r})")
            )

        claim_text = claim.get("text")
        if not isinstance(claim_text, str) or not claim_text.strip():
            findings.append(Finding("ERROR", "CLAIM_TEXT", f"{claim_id}: missing/empty `text`"))

        # Provenance: source_ids must exist and be back-linked by sources.yaml.
        source_id_list = _as_str_list(claim.get("source_ids"))
        if not source_id_list:
            findings.append(Finding("ERROR", "CLAIM_SOURCE_IDS", f"{claim_id}: missing/empty `source_ids`"))
            source_id_list = []
        for source_id in source_id_list:
            if source_id not in source_ids:
                findings.append(
                    Finding("ERROR", "CLAIM_SOURCE_MISSING", f"{claim_id}: source_id not in reference/sources.yaml: {source_id!r}")
                )
            else:
                extracted = sources_by_id.get(source_id, {}).get("claims_extracted", [])
                if claim_id not in extracted:
                    findings.append(
                        Finding(
                            "ERROR",
                            "SOURCE_BACKLINK_MISSING",
                            f"{claim_id}: source {source_id!r} missing backlink in `claims_extracted`",
                        )
                    )

        for field_name in ("first_extracted", "extracted_by", "version", "last_updated", "part_of_chain"):
            if field_name not in claim:
                findings.append(Finding("ERROR", "CLAIM_REQUIRED_FIELD", f"{claim_id}: missing required field `{field_name}`"))

        # Relationships must only reference claim IDs.
        for rel_field in ("supports", "contradicts", "depends_on", "modified_by"):
            rel_list = _as_str_list(claim.get(rel_field))
            if rel_list is None:
                findings.append(Finding("ERROR", "CLAIM_RELATIONSHIP_TYPE", f"{claim_id}: `{rel_field}` must be a list of strings"))
                continue
            for rel_id in rel_list:
                if rel_id not in claim_ids:
                    findings.append(Finding("ERROR", "CLAIM_RELATIONSHIP_REF", f"{claim_id}: `{rel_field}` references unknown claim {rel_id!r}"))

        # Optional: part_of_chain integrity.
        part_of_chain = claim.get("part_of_chain", "")
        if isinstance(part_of_chain, str) and part_of_chain:
            if part_of_chain not in chain_ids:
                findings.append(
                    Finding("ERROR", "CLAIM_CHAIN_REF", f"{claim_id}: `part_of_chain` references unknown chain {part_of_chain!r}")
                )

    # Validate chains.
    for chain_id, chain in chains_by_id.items():
        if not isinstance(chain_id, str) or not CHAIN_ID_RE.match(chain_id):
            findings.append(Finding("ERROR", "CHAIN_ID_FORMAT", f"Invalid chain ID format: {chain_id!r}"))
            continue
        if not isinstance(chain, dict):
            findings.append(Finding("ERROR", "CHAIN_ENTRY_TYPE", f"{chain_id}: chain entry must be a mapping"))
            continue

        for required in ("name", "thesis", "confidence", "claims", "analysis_file", "weakest_link"):
            if required not in chain:
                findings.append(Finding("ERROR", "CHAIN_REQUIRED_FIELD", f"{chain_id}: missing required field `{required}`"))

        chain_confidence = chain.get("confidence")
        if not _is_probability(chain_confidence):
            findings.append(Finding("ERROR", "CHAIN_CONFIDENCE", f"{chain_id}: invalid `confidence` (got {chain_confidence!r})"))

        chain_claims = _as_str_list(chain.get("claims"))
        if chain_claims is None:
            findings.append(Finding("ERROR", "CHAIN_CLAIMS_TYPE", f"{chain_id}: `claims` must be a list of strings"))
            chain_claims = []
        for claim_id in chain_claims:
            if claim_id not in claim_ids:
                findings.append(Finding("ERROR", "CHAIN_CLAIM_MISSING", f"{chain_id}: references missing claim {claim_id!r}"))

        analysis_file = chain.get("analysis_file", "")
        if isinstance(analysis_file, str) and analysis_file:
            analysis_path = repo_root / analysis_file
            if not analysis_path.exists():
                findings.append(
                    Finding(
                        "ERROR" if strict_paths else "WARN",
                        "CHAIN_ANALYSIS_FILE_MISSING",
                        f"{chain_id}: analysis_file does not exist: {analysis_file!r}",
                    )
                )

    # Counter consistency: counter >= max num for the latest year in that domain.
    for domain, max_year in max_year_by_domain.items():
        max_num = max_num_by_domain_year.get((domain, max_year), 0)
        counter_value = counters.get(domain)
        if not isinstance(counter_value, int):
            findings.append(Finding("ERROR", "COUNTER_TYPE", f"counters.{domain}: must be integer (got {counter_value!r})"))
            continue
        if counter_value < max_num:
            findings.append(
                Finding(
                    "ERROR",
                    "COUNTER_BEHIND",
                    f"counters.{domain}={counter_value} is behind existing max ID {domain}-{max_year}-{max_num:03d}",
                )
            )

    return claims_by_id, chains_by_id, max_year_by_domain, counters


def _validate_sources(
    *,
    findings: list[Finding],
    sources_data: dict[str, Any],
    claims_by_id: dict[str, Any],
    strict_paths: bool,
    repo_root: Path,
) -> dict[str, Any]:
    sources_by_id = sources_data.get("sources")
    if not isinstance(sources_by_id, dict):
        findings.append(Finding("ERROR", "SOURCES_SCHEMA", "Missing/invalid top-level `sources` in reference/sources.yaml"))
        return {}

    for source_id, source in sources_by_id.items():
        if not isinstance(source_id, str) or not source_id.strip():
            findings.append(Finding("ERROR", "SOURCE_ID", f"Invalid source ID key: {source_id!r}"))
            continue
        if not isinstance(source, dict):
            findings.append(Finding("ERROR", "SOURCE_ENTRY_TYPE", f"{source_id}: source entry must be a mapping"))
            continue

        for required in ("type", "title", "author", "year", "url", "accessed", "reliability", "bias_notes", "claims_extracted", "analysis_file", "topics", "domains"):
            if required not in source:
                findings.append(Finding("ERROR", "SOURCE_REQUIRED_FIELD", f"{source_id}: missing required field `{required}`"))

        extracted_claims = source.get("claims_extracted", [])
        if extracted_claims is None:
            extracted_claims = []
        extracted_list = _as_str_list(extracted_claims)
        if extracted_list is None:
            findings.append(Finding("ERROR", "SOURCE_CLAIMS_EXTRACTED_TYPE", f"{source_id}: `claims_extracted` must be a list of strings"))
            extracted_list = []

        for claim_id in extracted_list:
            claim = claims_by_id.get(claim_id)
            if claim is None:
                findings.append(Finding("ERROR", "SOURCE_CLAIM_UNKNOWN", f"{source_id}: `claims_extracted` references unknown claim {claim_id!r}"))
                continue
            claim_sources = claim.get("source_ids", [])
            if isinstance(claim_sources, list) and source_id not in claim_sources:
                findings.append(
                    Finding(
                        "ERROR",
                        "SOURCE_BACKLINK_EXTRA",
                        f"{source_id}: lists claim {claim_id!r} but claim does not include this source_id",
                    )
                )

        analysis_file = source.get("analysis_file", "")
        if isinstance(analysis_file, str) and analysis_file:
            analysis_path = repo_root / analysis_file
            if not analysis_path.exists():
                findings.append(
                    Finding(
                        "ERROR" if strict_paths else "WARN",
                        "SOURCE_ANALYSIS_FILE_MISSING",
                        f"{source_id}: analysis_file does not exist: {analysis_file!r}",
                    )
                )

    return sources_by_id


def _validate_predictions_md(
    *,
    findings: list[Finding],
    predictions_md_path: Path,
    claims_by_id: dict[str, Any],
    sources_by_id: dict[str, Any],
) -> None:
    try:
        text = predictions_md_path.read_text()
    except FileNotFoundError:
        findings.append(Finding("ERROR", "PREDICTIONS_MISSING_FILE", "Missing tracking/predictions.md"))
        return

    claim_ids_in_md = set(re.findall(r"\*\*Claim ID\*\*:\s*([A-Z]+-\d{4}-\d{3})\b", text))
    sources_in_md = set(re.findall(r"\*\*Source\*\*:\s*([a-z0-9][a-z0-9\\-]*)\b", text))

    prediction_claim_ids = {cid for cid, c in claims_by_id.items() if c.get("type") == "[P]"}
    missing_from_md = sorted(prediction_claim_ids - claim_ids_in_md)
    if missing_from_md:
        findings.append(
            Finding(
                "ERROR",
                "PREDICTION_SYNC_MISSING",
                f"Missing {len(missing_from_md)} [P] claims from tracking/predictions.md: {', '.join(missing_from_md)}",
            )
        )

    unknown_claims = sorted(claim_ids_in_md - set(claims_by_id.keys()))
    if unknown_claims:
        findings.append(
            Finding(
                "ERROR",
                "PREDICTION_UNKNOWN_CLAIM",
                f"tracking/predictions.md references unknown claim IDs: {', '.join(unknown_claims)}",
            )
        )

    non_prediction_claims = sorted([cid for cid in claim_ids_in_md if claims_by_id.get(cid, {}).get("type") != "[P]"])
    if non_prediction_claims:
        findings.append(
            Finding(
                "ERROR",
                "PREDICTION_NON_P_CLAIM",
                f"tracking/predictions.md includes non-[P] claims in Claim ID fields: {', '.join(non_prediction_claims)}",
            )
        )

    unknown_sources = sorted([sid for sid in sources_in_md if sid not in sources_by_id])
    if unknown_sources:
        findings.append(
            Finding(
                "ERROR",
                "PREDICTION_UNKNOWN_SOURCE",
                f"tracking/predictions.md references unknown sources: {', '.join(unknown_sources)}",
            )
        )


def validate_repo(*, repo_root: Path, strict_paths: bool) -> list[Finding]:
    findings: list[Finding] = []

    claims_registry_path = repo_root / "claims" / "registry.yaml"
    sources_registry_path = repo_root / "reference" / "sources.yaml"
    predictions_md_path = repo_root / "tracking" / "predictions.md"

    try:
        claims_data = _load_yaml(claims_registry_path)
    except FileNotFoundError:
        return [Finding("ERROR", "CLAIMS_MISSING_FILE", "Missing claims/registry.yaml")]

    try:
        sources_data = _load_yaml(sources_registry_path)
    except FileNotFoundError:
        return [Finding("ERROR", "SOURCES_MISSING_FILE", "Missing reference/sources.yaml")]

    if not isinstance(claims_data, dict):
        return [Finding("ERROR", "CLAIMS_SCHEMA", "claims/registry.yaml must be a mapping")]
    if not isinstance(sources_data, dict):
        return [Finding("ERROR", "SOURCES_SCHEMA", "reference/sources.yaml must be a mapping")]

    # Validate sources first so claims can validate source_ids/backlinks.
    sources_by_id = sources_data.get("sources")
    if not isinstance(sources_by_id, dict):
        sources_by_id = {}

    # Claims need sources; sources need claims for back-link checks.
    claims_by_id = claims_data.get("claims")
    if not isinstance(claims_by_id, dict):
        claims_by_id = {}

    sources_by_id = _validate_sources(
        findings=findings,
        sources_data=sources_data,
        claims_by_id=claims_by_id,
        strict_paths=strict_paths,
        repo_root=repo_root,
    )

    _validate_claims_and_chains(
        findings=findings,
        claims_data=claims_data,
        sources_by_id=sources_by_id,
        strict_paths=strict_paths,
        repo_root=repo_root,
    )

    _validate_predictions_md(
        findings=findings,
        predictions_md_path=predictions_md_path,
        claims_by_id=claims_by_id,
        sources_by_id=sources_by_id,
    )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate research framework data integrity.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Path to repo root (default: parent of this script's directory).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat missing analysis_file paths as errors (otherwise warnings).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output findings as JSON (machine-readable).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root or Path(__file__).resolve().parent.parent
    findings = validate_repo(repo_root=repo_root, strict_paths=args.strict)

    errors = [finding for finding in findings if finding.level == "ERROR"]
    warnings = [finding for finding in findings if finding.level == "WARN"]

    if args.json:
        payload = {
            "ok": len(errors) == 0,
            "error_count": len(errors),
            "warning_count": len(warnings),
            "findings": [asdict(finding) for finding in findings],
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        if errors:
            print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        else:
            print(f"OK: {len(errors)} error(s), {len(warnings)} warning(s)")
        for finding in findings:
            print(f"{finding.level} [{finding.code}] {finding.message}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

