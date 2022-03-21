import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph() #inbuilt graph

nx.draw(G, with_labels = True)

def edge_to_remove(graph):
    G_dict = nx.edge_betweenness_centrality(graph)
    edge = ()
    
    #extract value with highest edge betweenness centrality
    for key, value in sorted(G_dict.items(), key = lambda item: item[1], reverse = True):
        edge = key
        break
    return edge

def girvan_newman(graph):
    # find no. of connected components
    sg = nx.connected_components(graph)
    sg_count = nx.number_connected_components(graph)
    
    while(sg_count == 1):
        graph.remove_edge(edge_to_remove(graph)[0], edge_to_remove(graph)[1])
        sg = nx.connected_components(graph)
        sg_count = nx.number_connected_components(graph)
    
    return sg
#find communities in the group
communities = girvan_newman(G.copy())

node_groups = []
for com in communities:
    node_groups.append(list(com))
    
    
color_map = []
for node in G:
    if node in node_groups[0]:
        color_map.append('green')
    else:
        color_map.append('red')

nx.draw(G, node_color = color_map, with_labels = True)
print(node_groups) # We can see 3 plots since we classify according to 2 groups and then dump the rest in another class by default
plt.show()