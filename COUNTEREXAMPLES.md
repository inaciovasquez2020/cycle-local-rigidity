# Counterexamples Record

This document records the outcome of the exhaustive counterexample search
performed as part of the Cycle–Local Rigidity bounded verification project.

## 1. Definitions and Scope

We examine simple, undirected graphs \(G\) satisfying all of the following:

- **Vertex bound:** \(n \leq 7\)
- **Max degree:** \(\Delta(G) \leq 4\)
- **Homogeneity:** FO⁴ radius-2 homogeneity
- **Spectral condition:** Ihara–Bass / nonbacktracking spectral condition with \(\rho_0 = 1\)

No other graph classes or parameters are included in this search.

## 2. Search Methodology

The exhaustive search used the following deterministic process:

1. **Enumerate all simple graphs** up to 7 vertices with \(\Delta(G) \leq 4\).
2. **Apply spectral filter:** Evaluate Ihara–Bass / nonbacktracking condition.
3. **Check homogeneity:** Test FO⁴ radius-2 homogeneity.
4. **Local rank evaluation:** For graphs that pass (2) and (3), evaluate the
   local \(\mathbb{F}_2\) cycle rank bound within radius 2.
5. **Counterexample test:** A graph is labeled a counterexample if it violates
   the verified cycle–local rigidity bound under the stated parameters.

## 3. Outcome

**No counterexample was found** within the verified domain.

This means that for all graphs examined under steps (1)–(5), the cycle–local
rigidity implication held.

## 4. Interpretation and Limitations

The absence of a counterexample in the bounded domain does **not** prove the
implication for all graphs beyond \(n > 7\) or without the listed constraints.
This record documents only a bounded exhaustive negative result.

## 5. Artifacts

The following artifacts support this counterexample search and its outcome:

- `certificate.json`: Structured verification summary
- `certificate.sha256`: Verification artifact hashes
- `verify.sh`: Verification script
- Enumeration and filter code (in repository)

## 6. Reproducibility

All artifacts and scripts required to reconstruct this search and its outcome
are included in the repository and in release **v0.1.0**.
The verification process is deterministic.

## 7. References

See also:

- `counterexamples/README.md` (directory index)
- Repository release v0.1.0 draft assets
- MANUSCRIPT.md (bounded verification manuscript)
