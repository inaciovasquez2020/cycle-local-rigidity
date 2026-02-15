Counterexamples Record
This document records the outcome of an exhaustive counterexample search
performed for the Cycle–Local Rigidity implication under bounded parameters.
Verified Search Domain
Graphs G satisfying all of the following:
Number of vertices: n ≤ 7
Maximum degree: Δ(G) ≤ 4
FO^4 radius-2 homogeneity
Ihara–Bass / nonbacktracking spectral condition IB_{ρ0} with ρ0 = 1
Methodology
All simple graphs within the vertex bound were enumerated exhaustively.
Each candidate graph was subjected to the following deterministic filters:
Degree constraint filter
Ihara–Bass / nonbacktracking spectral verifier
FO^4 radius-2 homogeneity checker
Local F₂ cycle-rank evaluation within radius 2
Graphs passing filters (1)–(3) were checked for violation of the
cycle–local rigidity bound CLR(4,4,2; ρ0, C0) with C0 = 1.
Result
No counterexample was found within the verified domain.
Interpretation
This result establishes the non-existence of counterexamples
within the explicitly bounded search space only.
No claims are made for n ≥ 8 or for unbounded graph families.
Artifacts
The search and its outcome are certified by:
certificate.json
certificate.sha256
verify.sh
Reproducibility
The verification is deterministic.
All artifacts required to reproduce this result are included
in release v0.1.0.
