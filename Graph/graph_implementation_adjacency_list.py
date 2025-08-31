# To Implement Graph Insertion Operation Adjacency List 

def add_node(v):
    # check given node already present in graph 
    if v in graph:
        print(f"Node/vertices {v} already present in graph")
    ## adding the node 
    else:
        graph[v] = []

graph = {}

add_node('A')
print(graph)