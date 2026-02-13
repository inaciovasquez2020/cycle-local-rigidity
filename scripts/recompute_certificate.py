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

def cycle_rank(G):
    return G.number_of_edges() - G.number_of_nodes() + nx.number_connected_components(G)

def ball(G, v, r):
    nodes = {v}
    frontier = {v}
    for _ in range(r):
        new = set()
        for u in frontier:
            new |= set(G.neighbors(u))
        new -= nodes
        nodes |= new
        frontier = new
    return G.subgraph(nodes).copy()

def local_cycle_rank(G, r):
    seen = set()
    rank = 0
    for v in G.nodes():
        H = ball(G, v, r)
        edges = frozenset(tuple(sorted(e)) for e in H.edges())
        if edges not in seen:
            seen.add(edges)
            rank += cycle_rank(H)
    return rank

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    graph_path = sys.argv[1]
    G = nx.read_edgelist(graph_path, nodetype=int)

    B = nonbacktracking_matrix(G)
    rho = spectral_radius(B)
    clr_rank = local_cycle_rank(G, 2)

    cert = {
        "ib": {
            "rho": rho
        },
        "clr": {
            "max_local_cycle_rank": clr_rank
        }
    }

    print(json.dumps(cert, indent=2, sort_keys=True))
