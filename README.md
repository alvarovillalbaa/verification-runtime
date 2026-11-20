# verification-runtime

<!-- project-family:start -->
> **Project family:** [AI Research Lab](https://github.com/alvarovillalbaa#ai-research-lab) · **Area:** Verification
<!-- project-family:end -->

Last updated: 2026-11-10

Run objective verification independently of a training pipeline or evaluation platform.

**Implemented scope:** a standard-library Python 3.11+ package and CLI for exact-match
text verification with subject, candidate and reference identities. Code sandbox,
symbolic math, JSON Schema, environment-success and citation execution are planned
adapters. This extraction does not claim those engines exist.

## Independent use

```sh
python3 -m pip install .
verification-runtime examples/exact-match.json
python3 examples/quickstart.py
```

`verify_exact_match(subject_id=..., candidate=..., reference=...)` compares
stripped strings using `exact_match/v1`. Results retain SHA-256 of the original
UTF-8 candidate/reference bytes. Missing references fail verification. The CLI
returns 0 for accepted, 1 for rejected, and 2 for invalid input.

The verifier does not know about teachers, licenses, preference pairs or reward
policy. Model-distillation checks eligibility and binds results to its task and
response before constructing data. Open Evals retains evaluator definitions,
composition, scoring, runs and gates; an adapter can consume these results.

[Specification](docs/specs/README.md) · [Source lineage](docs/sources/lineage.json)

MIT covers authored code/docs. No sibling checkout, GPU, service, database or
account is required. Input hashes provide binding, not signed execution
attestation or proof that a caller-supplied result was produced by trusted code.
