# Verification execution contract

Last updated: 2026-11-10

Exact-match v1 is implemented over supplied text. It returns a frozen result with
subject identity, raw candidate/reference hashes, verdict, versioned verifier
identity and diagnostic reason. This is the only current execution adapter.

## Planned adapter contract

A broader adapter accepts immutable task/candidate artifacts, an exact verifier
implementation/configuration and explicit resource/isolation policy. It emits
input/output identities, verdict or error/timeout, diagnostics and observation
coverage. Unavailable measurements stay unknown. Code execution requires an
explicitly selected sandbox and limits; it must never run as an implicit side
effect of importing or validating a record.

- [ ] Add bounded JSON Schema, numeric/symbolic, code, environment and source-span adapters individually.
- [ ] Define adapter-specific configuration/version and error/timeout results before implementation.
- [ ] Validate each adapter independently, including malformed input and isolation failure.
- [ ] Add optional consumers for Open Evals, RL reward mapping and research-controller.

Open Evals owns evaluation catalogues, composition, scores and gates.
Distillation owns teacher eligibility and preference policy. RL trainers map
objective results into rewards. This package owns none of those policies.
