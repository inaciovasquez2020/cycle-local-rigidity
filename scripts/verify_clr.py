import sys
import json
import networkx as nx

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

def cycle_rank(G):
    return G.number_of_edges() - G.number_of_nodes() + nx.number_connected_components(G)

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

def verify_clr(graph_path, cert_path):
    G = nx.read_edgelist(graph_path, nodetype=int)

    if G.number_of_nodes() == 0 or G.number_of_edges() == 0:
        return True

    if max(dict(G.degree()).values()) > 4:
        return False

    r = 2
    loc_rank = local_cycle_rank(G, r)

    with open(cert_path) as f:
        cert = json.load(f)

    return loc_rank <= cert["clr"]["max_local_cycle_rank"]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    ok = verify_clr(sys.argv[1], sys.argv[2])
    sys.exit(0 if ok else 1)
