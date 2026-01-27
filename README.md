![CI](https://github.com/inaciovasquez2020/cycle-local-rigidity/actions/workflows/ci.yml/badge.svg)

# Cycle Local Rigidity
**Verification of Logic-Width Dependency in Periodic Systems**

---

### 🛡️ Institutional Verification
* **Registry ID:** `CORE-LW-01`
* **Status:** Core Mathematically Closed
* **Verification Method:** Lean 4 Formal Proof / LaTeX Structural Analysis
* **Framework Alignment:** Unified Rigidity Framework (URF) — Law 3

---

## Purpose
This repository provides the formal computational witness for the **Logic-Width Dependency** ($k \ge f(tw)$). It exists to prove that local homogeneity forces global rigidity in cyclic and periodic operator systems, specifically resolving the "Expander Obstruction" by isolating the spectral gap within bounded-treewidth regimes.

## Scope
- **Includes:** Lean 4 formalizations of cycle-local types, LaTeX manuscripts detailing the Rigidity Wall, and CI-verified proofs of spectral isolation.
- **Does Not Include:** Heuristic simulations or probabilistic modeling; all results are deterministic and formally verified.

## Contents
- `docs/` — Formal manuscripts, including the structural resolution of the Expander Obstruction.
- `src/` — Source files including **Lean 4** formalizations and **LaTeX** source for citable artifacts.
- `examples/` — Minimal runnable witnesses of the Spectral Gap in cycle-local regimes.

## Quickstart

### LaTeX
To compile the structural proofs:
```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
