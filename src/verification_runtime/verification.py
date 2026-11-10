"""Versioned exact-match verification over explicit text inputs."""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True)
class VerificationResult:
    subject_id: str
    candidate_sha256: str
    reference_sha256: str | None
    accepted: bool
    verifier: str
    reason: str


def text_sha256(value: str) -> str:
    """Hash original UTF-8 bytes, before the verifier's documented normalization."""
    return sha256(value.encode("utf-8")).hexdigest()


def verify_exact_match(*, subject_id: str, candidate: str,
                       reference: str | None) -> VerificationResult:
    """Compare stripped strings, preserving the identity of each original input."""
    if not isinstance(subject_id, str) or not subject_id.strip():
        raise ValueError("subject_id must be a non-empty string")
    if not isinstance(candidate, str) or (reference is not None and not isinstance(reference, str)):
        raise ValueError("candidate and any supplied reference must be strings")
    accepted = reference is not None and candidate.strip() == reference.strip()
    reason = ("task has no expected answer" if reference is None else
              "matched expected answer" if accepted else "did not match expected answer")
    return VerificationResult(
        subject_id=subject_id,
        candidate_sha256=text_sha256(candidate),
        reference_sha256=text_sha256(reference) if reference is not None else None,
        accepted=accepted, verifier="exact_match/v1", reason=reason,
    )
