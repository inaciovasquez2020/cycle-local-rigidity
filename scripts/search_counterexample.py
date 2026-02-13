import sys
import subprocess
import glob

def run(cmd):
    return subprocess.call(cmd) == 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    n = int(sys.argv[1])
    cert = sys.argv[2]

    subprocess.check_call([sys.executable, "scripts/enumerate_graphs.py", str(n)])

    for path in sorted(glob.glob("graphs/*.edgelist")):
        ok = run([sys.executable, "scripts/verify_all.py", path, cert])
        if not ok:
            print("COUNTEREXAMPLE FOUND:", path)
            sys.exit(2)

    print("no counterexample up to n =", n)
    sys.exit(0)
