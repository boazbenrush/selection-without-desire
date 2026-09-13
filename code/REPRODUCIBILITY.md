# Reproducibility Notes

The release contains the reported synthetic datasets plus a clean implementation
of the neutral-policy lineage-selection model.

## Important evidence distinction

- Numerical verification: confirms code and formulas agree.
- Synthetic hold-out prediction: tests the analytical boundary on unseen synthetic environments from the same structural model family.
- External empirical validation: not yet performed.

The supplied script contains a smoke test only. The reported full experiment used
200 replications per D/E cell (800 main runs) and a separate 300-environment GPIN
evaluation. The CSV outputs in `../data/` are the canonical reported synthetic data.

## Determinism

Seeds in the reported analysis were deterministic functions of replication and
condition identifiers. This makes the synthetic run structure auditable.

## External test

The next stage is the preregistered agent-population experiment described in
`../PREREGISTRATION_OSF.md`.
