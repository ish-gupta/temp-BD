graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['E', 'G'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : ['A', 'H'],
    'H' : []
    }

visited = list()
queue = list()
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, 'A')
print(visited)