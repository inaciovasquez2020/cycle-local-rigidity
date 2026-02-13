Cycle–Local Rigidity (bounded verification)

This repository contains a bounded, exhaustive verification of a cycle–local rigidity implication for finite graphs.

Result.
Fix parameters rho0 = 1 and C0 = 1. For all graphs G with at most 7 vertices satisfying:
- maximum degree ≤ 4,
- IB_{rho0} (nonbacktracking spectral radius ≤ rho0),
- FO^4 radius-2 homogeneity,

no counterexample exists to the implication:
IB_{rho0} ⇒ CLR(4,4,2; rho0, C0),

where CLR(4,4,2) bounds the radius-2 local F2 cycle rank.

Method.
All graphs up to n ≤ 7 are exhaustively enumerated. The search is restricted to the theorem domain using:
- a concrete Ihara–Bass / nonbacktracking spectral verifier,
- an FO^4 radius-2 homogeneity checker,
- a local cycle-rank checker.

The verification is deterministic and enforced by CI.

Status.
The result is fully verified for n ≤ 7. Enumeration for n ≥ 8 is computationally infeasible without additional theoretical pruning. No general (unbounded-n) claim is made.
