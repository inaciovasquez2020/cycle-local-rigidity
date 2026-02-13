set -euo pipefail
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/search_counterexample.py 6 certificate.json
