import sys
import subprocess

def run(cmd):
    return subprocess.call(cmd) == 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    graph = sys.argv[1]
    cert  = sys.argv[2]

    ok_ib  = run([sys.executable, "scripts/verify_ib.py", graph, cert])
    ok_clr = run([sys.executable, "scripts/verify_clr.py", graph, cert])

    sys.exit(0 if (ok_ib and ok_clr) else 1)
