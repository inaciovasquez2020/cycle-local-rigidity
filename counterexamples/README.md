# Counterexamples Directory

This directory contains artifacts and records pertaining to the exhaustive
counterexample search performed as part of the Cycle–Local Rigidity
bounded verification.

## Verified Domain

The search domain was explicitly bounded as follows:

- Graphs \(G\) with number of vertices \(n \leq 7\)
- Maximum degree constraint \(\Delta(G) \leq 4\)
- **FO⁴ radius-2 homogeneity**
- **Ihara–Bass / nonbacktracking spectral condition** with \(\rho_0 = 1\)

Only graphs satisfying all of the above criteria were examined.

## Search Methodology

Each candidate graph was subjected to deterministic enumeration and filter
stages:

1. Max-degree filter
2. Ihara–Bass / nonbacktracking spectral verifier
3. Radius-2 homogeneity check
4. Local \(\mathbb{F}_2\) cycle rank bound evaluation

Graphs that passed (1)–(3) were tested for violation of the cycle–local
rigidity implication within the bounded space.

## Search Outcome

**No counterexample was found** within the verified search domain.

This result is a negative (none found) record only and does *not* imply
non-existence beyond the stated bounds (e.g., \(n \geq 8\)).

## Artifacts

Files in this directory (or linked from here) include:

- `COUNTEREXAMPLES.md`: Detailed description of search and its outcome
- (optional) Raw enumeration logs
- (optional) Filter pass/fail trace files

## Reproducibility

All artifacts required to reproduce this outcome are included in the
primary release **v0.1.0**:

- `certificate.json`
- `certificate.sha256`
- `verify.sh`
- Enumeration and verification scripts

These guarantee deterministic reconstruction of the search.

## Interpretation

This counterexample record documents a bounded negative result only.
It contributes to confidence in the cycle-local rigidity implication
within the finite domain examined and supports the release artifacts.
