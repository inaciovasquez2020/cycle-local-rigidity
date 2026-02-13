import sys
import subprocess
import glob
import json

def run(cmd):
    return subprocess.call(cmd) == 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    n = int(sys.argv[1])
    cert = sys.argv[2]

    subprocess.check_call([sys.executable, "scripts/enumerate_graphs.py", str(n)])

    for path in sorted(glob.glob("graphs/*.edgelist")):
        if run([sys.executable, "scripts/verify_ib.py", path, cert]):
            print(path)
