# Cycle Local Rigidity  
**Verification of Logic–Width Dependency in Periodic Systems**

---

## Scope

This repository is a **Tier A module** in the **Scientific Infrastructure (URF)**.  
It provides the **formal logic and proof layer** for the Logic–Width Dependency:

\[
k \ge f(tw)
\]

It constitutes the **cycle / periodic specialization** of the URF rigidity wall.

This module contains:
- Lean 4 formal proofs,
- LaTeX structural manuscripts,
- finite certificates of cycle-local rigidity,
- deterministic witnesses of spectral isolation.

No simulations, heuristics, or probabilistic models are used.

---

## Institutional Verification

- **Registry ID:** CORE-LW-01  
- **Status:** Core Mathematically Closed  
- **Verification Method:** Lean 4 Formal Proof / LaTeX Structural Analysis  
- **Framework Alignment:** Unified Rigidity Framework (URF) — Law 3  

---

## Purpose

This repository provides the **formal computational witness** for the  
**Logic–Width Dependency** in periodic and cyclic systems.

It resolves the **Expander Obstruction** by proving:

- local FOᵏ homogeneity,
- plus bounded structural width,
- forces global rigidity in cyclic regimes.

This establishes the **logic–geometry bridge** required by URF.

---

## Core Result

### FO⁴ Cycle-Local Rigidity Theorem

For bounded-degree periodic systems:

\[
\text{FO}^4\text{-local equivalence} \;\Rightarrow\; \text{global rigidity}
\]

with finite certificates depending only on radius and degree bounds.

This result is:
- deterministic,
- formally verified,
- independent of probabilistic arguments.

---

## Contents

- `docs/` — Formal manuscripts resolving the Expander Obstruction.  
- `src/` — Lean 4 formalizations and LaTeX source.  
- `examples/` — Minimal witnesses of spectral isolation in cycle-local regimes.  

All contents are versioned and citable.

---

## Reproducibility

All verification is deterministic.

### Lean

To build formal proofs:

```bash
lake build
