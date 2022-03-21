import networkx as nx

G = nx.path_graph(10)
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
print(f'Degree Centrality : \n{degree_centrality} \n\nCloseness Centrality : \n{closeness_centrality} \n\nBetweenness Centrality : \n{betweenness_centrality}')
