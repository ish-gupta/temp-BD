import networkx as nx
import functools

def closeness_centrality(G, u = None, distance = None, normalized = True):
    if distance is not None:
        #use Dijkstra's algorithm with specified attribute as edge weight
        path_length = functools.partial(nx.single_source_dijkstra_path_length, weight = distance)
    else:
        path_length = nx.single_source_shortest_path_length
        
    if u is None:
        nodes = G.nodes()
    else: nodes = [u]
    closeness_centrality = {}
    
    for n in nodes:
        sp = path_length(G, n)
        totsp = sum(sp.values())
        if totsp > 0.0 and len(G) > 1:
            closeness_centrality[n] = (len(sp) - 1.0) / totsp
            
            #normalize to number of nodes-1 in connected part
            if normalized:
                s = (len(sp) - 1.0) / (len(G) - 1)
                closeness_centrality[n] *= s
                
        else:
            closeness_centrality[n] = 0.0
    
    if u is not None:
        return closeness_centrality[u]
    else:
        return closeness_centrality
    
G = nx.path_graph(10)
c = closeness_centrality(G)
c_in = nx.closeness_centrality(G)
print(f'Function : \n{c} \n\nInbuilt : \n{c_in}')
    