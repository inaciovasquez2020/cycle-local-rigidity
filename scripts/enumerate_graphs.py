import sys
import itertools
import networkx as nx

def graphs_n(n):
    nodes = list(range(n))
    edges = list(itertools.combinations(nodes, 2))
    for mask in range(1 << len(edges)):
        G = nx.Graph()
        G.add_nodes_from(nodes)
        for i, e in enumerate(edges):
            if (mask >> i) & 1:
                G.add_edge(*e)
        yield G

def bounded_degree(G, d):
    return all(deg <= d for _, deg in G.degree())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    n = int(sys.argv[1])
    for G in graphs_n(n):
        if bounded_degree(G, 4):
            name = f"graphs/G_n{n}_{G.number_of_edges()}.edgelist"
            nx.write_edgelist(G, name, data=False)
