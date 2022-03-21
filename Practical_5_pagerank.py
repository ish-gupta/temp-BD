# Importing the necessary libraries to execute the "Random Walk Method"
import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

#select random graph using gnp_random_graph() function of networkx
Graph = nx.gnp_random_graph(10, 0.5, directed=True) #first value = no. of nodes, second value = probability
nx.draw(Graph, with_labels=True, node_color='green') #draw the network graph 
plt.figure(figsize=(15,10))
#plt.show() #to show the graph by plotting it

# random_node is the start node selected randomly
random_node = random.choice([i for i in range(Graph.number_of_nodes())])
dict_counter = {} #initialise the value for all nodes as 0
# increment only for random node by traversing through all neighbors nodes, assign rest as 0
for i in range(Graph.number_of_nodes()):
    if random_node == i : dict_counter[i] = dict_counter.get(i, 0)+1
    else : dict_counter[i] = dict_counter.get(i, 0)

'''for i in (Graph.neighbors(random_node)):
    print(i)'''
    
#Traversing through the neighbors of start node
#Randomy choosing and incrementing means randomly visiting one of the linked pages out of all linked pages, thus the value for that one page increases
for i in range(500):
    list_for_nodes = list(Graph.neighbors(random_node))
    if len(list_for_nodes)==0:# if random_node having no outgoing edges/neighbours
        random_node = random.choice([i for i in range(Graph.number_of_nodes())])
        dict_counter[random_node] = dict_counter[random_node]+1 #randomly choose a value for neighbour and increment
        
    else:
        random_node = random.choice(list_for_nodes) #choose a node randomly from neighbors
        dict_counter[random_node] = dict_counter[random_node]+1
        
# using pagerank() method to provide ranks for the nodes        
rank_node = nx.pagerank(Graph)

#sorting the values of rank and random walk of respective nodes
sorted_rank = sorted(rank_node.items(), key=operator.itemgetter(1))#each tuple in rank_node can be presented as (itemgetter(0), itemgetter(1)), so according to which parameter you want to sort matters
sorted_random_walk = sorted(dict_counter.items(), key=operator.itemgetter(1))
print(sorted_rank)
print(sorted_random_walk)
