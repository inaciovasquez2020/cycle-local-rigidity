import sys
import networkx as nx

def ball_signature(G, v, r):
    nodes = {v}
    frontier = {v}
    for _ in range(r):
        new = set()
        for u in frontier:
            new |= set(G.neighbors(u))
        new -= nodes
        nodes |= new
        frontier = new
    H = G.subgraph(nodes)
    degs = sorted(d for _, d in H.degree())
    return tuple(degs)

def fo4_radius2_homogeneous(G):
    sigs = {ball_signature(G, v, 2) for v in G.nodes()}
    return len(sigs) == 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    G = nx.read_edgelist(sys.argv[1], nodetype=int)
    sys.exit(0 if fo4_radius2_homogeneous(G) else 1)
