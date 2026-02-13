Replication procedure (deterministic)

Environment
- Python 3.11
- networkx 3.2.1
- numpy 1.26.4

Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Recompute certificate from a reference graph
python scripts/recompute_certificate.py graphs/reference.edgelist > certificate.recomputed.json

Verify a graph against the certificate
python scripts/verify_all.py graphs/reference.edgelist certificate.recomputed.json

Enumerate Δ≤4 graphs up to size n and search for counterexamples
python scripts/search_counterexample.py 6 certificate.recomputed.json

Outputs
- exit code 0 means no counterexample found up to n
- exit code 2 prints the first counterexample path
