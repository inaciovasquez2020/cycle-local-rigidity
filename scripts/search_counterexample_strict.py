import sys
import subprocess
import glob

def ok(cmd):
    return subprocess.call(cmd) == 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    n = int(sys.argv[1])
    cert = sys.argv[2]

    subprocess.check_call([sys.executable, "scripts/enumerate_graphs.py", str(n)])

    for path in sorted(glob.glob("graphs/*.edgelist")):
        if not ok([sys.executable, "scripts/verify_ib.py", path, cert]):
            continue
        if not ok([sys.executable, "scripts/check_fo4_r2.py", path]):
            continue
        if not ok([sys.executable, "scripts/verify_clr.py", path, cert]):
            print("STRICT COUNTEREXAMPLE FOUND:", path)
            sys.exit(2)

    print("no strict counterexample up to n =", n)
    sys.exit(0)
