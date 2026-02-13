import sys
import subprocess
import glob

def run(cmd):
    return subprocess.call(cmd) == 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    nmax = int(sys.argv[1])
    cert = sys.argv[2]

    for n in range(1, nmax + 1):
        subprocess.check_call([sys.executable, "scripts/enumerate_graphs.py", str(n)])
        any_ib = False
        for path in glob.glob("graphs/*.edgelist"):
            if run([sys.executable, "scripts/verify_ib.py", path, cert]):
                any_ib = True
                break
        if not any_ib:
            print("IB_rho0 first fails at n =", n)
            sys.exit(0)

    print("IB_rho0 holds for some graph up to n =", nmax)
    sys.exit(0)
