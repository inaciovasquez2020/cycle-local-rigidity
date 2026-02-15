# Cycle–Local Rigidity (bounded verification)

Bounded, exhaustive verification of a cycle–local rigidity implication for finite graphs.

## Result (bounded)
Fix parameters ρ₀ = 1 and C₀ = 1. For all graphs G with at most 7 vertices satisfying:
- maximum degree Δ(G) ≤ 4
- Ihara–Bass / nonbacktracking spectral condition IB_{ρ₀}
- FO^4 radius-2 homogeneity

no counterexample exists to:
IB_{ρ₀} ⇒ CLR(4,4,2; ρ₀, C₀)

## Method
All graphs up to n ≤ 7 are exhaustively enumerated and filtered by:
- nonbacktracking / Ihara–Bass spectral verifier
- FO^4 radius-2 homogeneity checker
- local F₂ cycle-rank checker

Verification is deterministic and enforced by CI.

## Status / Scope
- Verified: n ≤ 7 (bounded exhaustive)
- Not claimed: any unbounded-n theorem
- n ≥ 8: infeasible without additional structure

## Quickstart
```bash
./verify.sh
Artifacts
certificate.json
certificate.sha256
Citation
See CITATION.cff.
