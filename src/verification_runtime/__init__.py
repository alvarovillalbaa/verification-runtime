"""Headless verification primitives; no training or evaluation service required."""
from .verification import VerificationResult, text_sha256, verify_exact_match

__all__ = ["VerificationResult", "text_sha256", "verify_exact_match"]
