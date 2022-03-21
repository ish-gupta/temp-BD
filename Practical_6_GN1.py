import networkx as nx
import itertools
from networkx.algorithms.community.centrality import girvan_newman

G = nx.path_graph(10)
k = 4

comp = girvan_newman(G)
tuple(sorted(c) for c in next(comp))

for communities in itertools.islice(comp, k):
    print(tuple(sorted(c) for c in communities))
