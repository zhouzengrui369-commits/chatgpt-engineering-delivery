#!/usr/bin/env python3
"""Validate the canonical delivery lifecycle and contract templates."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "core/ENGINEERING_DELIVERY_SKILL.md",
    "core/DELIVERY_STATE_MACHINE.json",
    "contracts/GOAL_DELIVERY.md",
    "contracts/CANDIDATE_MANIFEST.md",
    "contracts/TECHNICAL_RECEIPT.md",
    "contracts/LOCAL_EXECUTION.md",
    "contracts/ENGINEERING_TERMINAL.md",
    "starter-kit/AGENTS.md",
    "VERSION",
]

for rel in REQUIRED_FILES:
    path = ROOT / rel
    if not path.is_file():
        raise SystemExit(f"missing required file: {rel}")

machine = json.loads((ROOT / "core/DELIVERY_STATE_MACHINE.json").read_text())
assert machine["protocol_version"] == "DELIVERY-LIFECYCLE-1.0"
assert machine["foundational_rule"] == "ONE_GOAL_EQUALS_ONE_MILESTONE"

states = {item["id"]: item for item in machine["states"]}
assert states["ENGINEERING_READY"]["owner"] == "ENGINEERING_DELIVERY"
assert states["ENGINEERING_READY"]["atomic"] is True
assert states["CANDIDATE_ADMITTED"]["owner"] == "PRODUCT_GOVERNANCE"
assert states["PRODUCT_REVIEW_ELIGIBLE"]["owner"] == "PRODUCT_GOVERNANCE"
assert states["PRODUCT_EXPERIENCE_PASS"]["owner"] == "INDEPENDENT_PRODUCT_EXPERIENCE_REVIEWER"
assert states["HUMAN_OWNER_ACCEPTED"]["owner"] == "HUMAN_OWNER"

required_ready = set(states["ENGINEERING_READY"]["required_inputs"])
for token in {
    "candidate_sha",
    "candidate_tree",
    "candidate_manifest_ref",
    "technical_receipt_ref",
    "engineering_required_evidence=complete",
    "unapproved_deviations=none",
}:
    assert token in required_ready, f"ENGINEERING_READY missing {token}"

for rel, tokens in {
    "contracts/GOAL_DELIVERY.md": [
        "engineering_required",
        "admission_required",
        "review_required",
        "product_experience",
        "human_owner",
    ],
    "contracts/CANDIDATE_MANIFEST.md": [
        "recommended_next_gate: PRODUCT_GOVERNANCE_CANDIDATE_ADMISSION",
        "PRODUCT_REVIEW_ELIGIBLE",
    ],
    "contracts/TECHNICAL_RECEIPT.md": [
        "engineering_delivery_result",
        "OPEN",
        "COMPLETE",
    ],
    "contracts/LOCAL_EXECUTION.md": [
        "verdict_claimed: NONE",
        "source_mutation: NO",
    ],
}.items():
    text = (ROOT / rel).read_text()
    for token in tokens:
        assert token in text, f"{rel} missing {token}"

skill = (ROOT / "core/ENGINEERING_DELIVERY_SKILL.md").read_text()
for forbidden_claim in [
    "CANDIDATE_ADMITTED",
    "PRODUCT_REVIEW_ELIGIBLE",
    "PRODUCT_EXPERIENCE_PASS",
    "HUMAN_OWNER_ACCEPTED",
    "GOAL_MILESTONE_CLOSED",
]:
    assert forbidden_claim in skill

print("DELIVERY_LIFECYCLE_VALIDATION=PASS")
