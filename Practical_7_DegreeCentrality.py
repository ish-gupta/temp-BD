import networkx as nx

def degree_centrality(G):
    if len(G) <= 1:
        return {n:1 for n in G}
    
    s = 1.0/ (len(G) - 1.0)
    centrality = {n: d*s for n,d in G.degree()}
    return centrality

G = nx.erdos_renyi_graph(3,0.5)
d = degree_centrality(G)
d_in = nx.degree_centrality(G)
print(f'Function : {d} \nInbuilt : {d_in}')
