from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cycle_rigidity_boundary_certificate import missing_required_paths, cycle_rigidity_boundary_certificate


BOUNDARY = """
No repository-level claim of universal cycle-local rigidity completeness.
No repository-level claim that finite cycle-rigidity closure implies external validation.
No repository-level claim of peer-reviewed acceptance unless explicitly documented.
No repository-level claim that finite cycle-rigidity-boundary closure equals theorem-level completion.
"""


def test_missing_required_paths_detects_absence() -> None:
    missing = missing_required_paths(ROOT, ["docs/status/CYCLE_RIGIDITY_BOUNDARY_CERTIFICATE.md", "definitely_missing.file"])
    assert "definitely_missing.file" in missing


def test_cycle_rigidity_boundary_certificate_passes_for_manifest() -> None:
    cert = cycle_rigidity_boundary_certificate(
        ROOT,
        [
            "docs/status/CYCLE_RIGIDITY_BOUNDARY_CERTIFICATE.md",
            "scripts/verify_cycle_rigidity_boundary_certificate.py",
            "src/cycle_rigidity_boundary_certificate.py",
            "tests/test_cycle_rigidity_boundary_certificate.py",
        ],
        BOUNDARY,
    )
    assert cert.theorem_id == "CLR-CBC-1"
    assert cert.status == "PASS"
    assert cert.required_count == 4
    assert cert.present_count == 4
    assert cert.missing == ()
    assert cert.all_required_present is True
    assert cert.boundary_declared is True


def test_cycle_rigidity_boundary_certificate_fails_without_boundary() -> None:
    cert = cycle_rigidity_boundary_certificate(ROOT, ["docs/status/CYCLE_RIGIDITY_BOUNDARY_CERTIFICATE.md"], "")
    assert cert.status == "FAIL"
    assert cert.boundary_declared is False


def test_repository_scope_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/verify_cycle_rigidity_boundary_certificate.py"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    assert '"theorem_id": "CLR-CBC-1"' in result.stdout
    assert '"status": "PASS"' in result.stdout


def test_nonclaim_boundary_retained() -> None:
    text = (ROOT / "docs/status/CYCLE_RIGIDITY_BOUNDARY_CERTIFICATE.md").read_text(encoding="utf-8")
    assert "No repository-level claim of universal cycle-local rigidity completeness." in text
    assert "No repository-level claim that finite cycle-rigidity closure implies external validation." in text
    assert "No repository-level claim of peer-reviewed acceptance unless explicitly documented." in text
    assert "No repository-level claim that finite cycle-rigidity-boundary closure equals theorem-level completion." in text
