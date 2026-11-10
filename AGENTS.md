# Verification runtime agent instructions

- Read README.md and docs/specs/README.md before changing behavior.
- Own headless verification execution and result provenance; never import Lab, distillation, trainers or Open Evals.
- Keep verification separate from teacher rights, preference selection, reward mapping and evaluation gates.
- Exact-match v1 is implemented. Sandboxed code, math, schema, environment and citation adapters remain planned.
- Never execute candidate code, fetch artifacts or contact services implicitly.
- Preserve source snapshots and historical receipts. Run focused checks and git diff --check.
