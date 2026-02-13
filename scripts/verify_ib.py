import json
import sys
import networkx as nx
import numpy as np

def nonbacktracking_matrix(G):
    edges = []
    index = {}
    for u, v in G.edges():
        edges.append((u, v))
        edges.append((v, u))
    for i, e in enumerate(edges):
        index[e] = i
    n = len(edges)
    if n == 0:
        return np.zeros((0, 0))
    B = np.zeros((n, n), dtype=int)
    for (u, v), i in index.items():
        for w in G.neighbors(v):
            if w != u:
                j = index[(v, w)]
                B[i, j] = 1
    return B

def spectral_radius(B):
    if B.size == 0:
        return 0.0
    vals = np.linalg.eigvals(B)
    return float(max(abs(vals)))

def verify_ib(graph_path, cert_path):
    with open(cert_path) as f:
        cert = json.load(f)
    G = nx.read_edgelist(graph_path, nodetype=int)
    B = nonbacktracking_matrix(G)
    rho = spectral_radius(B)
    return rho <= cert["ib"]["rho"]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    ok = verify_ib(sys.argv[1], sys.argv[2])
    sys.exit(0 if ok else 1)
