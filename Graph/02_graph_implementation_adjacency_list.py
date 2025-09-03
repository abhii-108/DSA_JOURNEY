# To Implement Graph Insertion Operation Adjacency List 

def add_node(v):
    # check given node already present in graph 
    if v in graph:
        print(f"Node/vertices {v} already present in graph")
    ## adding the node 
    else:
        graph[v] = []

# undirected & un-wighted graph 
def add_edges(v1,v2):
    ## check if both vertices are present in graph 
    if v1 not in graph:
        print(f'node {v1} not present in graph ')
    elif v2 not in graph:
        print(f'node {v2} is not present in graph')
    
    else:## We need to add this check conditio
        if v2 not in graph[v1]:
            graph[v1].append(v2)
        if v1 not in graph[v2]:
            graph[v2].append(v1)


# undirected & weighted graph 
def add_edges_weighted(v1,v2, cost):
    ## check if both vertices are present in graph 
    if v1 not in graph:
        print(f'node {v1} not present in graph ')
    elif v2 not in graph:
        print(f'node {v2} is not present in graph')
    
    else:
        list1 = [v2, cost]
        list2 = [v1, cost]
        graph[v1].append(list1)
        graph[v2].append(list2)


## directed & un-weighted graph 
def add_edges_weighted_undirected(v1,v2):
    ## check if both vertices are present in graph 
    if v1 not in graph:
        print(f'node {v1} not present in graph ')
    elif v2 not in graph:
        print(f'node {v2} is not present in graph')
    
    else:
        graph[v1].append(v2)


# undirected & weighted graph 
def add_edges_weighted_directed(v1,v2, cost):
    ## check if both vertices are present in graph 
    if v1 not in graph:
        print(f'node {v1} not present in graph ')
    elif v2 not in graph:
        print(f'node {v2} is not present in graph')
    
    else:
        list1 = [v2, cost]
        graph[v1].append(list1)



#### Delete Node 
def delete_node(v):
    ## check node in graph 
    if v not in graph:
        print(f'node {v} is not present in graph')
    else:
        ## delete key value pair from dictionary for pop method we need to provide dictionary key 
        graph.pop(v)

        for key in graph:
            list1 = graph[key]
            for j in list1: 

                if v == j[0]:
                    list1.remove(j)
                    break

def delete_edge(v1,v2):
    if v1 not in graph:
        print(f'node {v1} not present in graph ')
    elif v2 not in graph:
        print(f'node {v2} is not present in graph')

    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

graph = {}

add_node('A')
print(graph)  ## {'A': []}

add_node('B')
print(graph)  ## {'A': [], 'B': []}

add_edges('A','B')
print(graph)  ## {'A': ['B'], 'B': ['A']}

add_node('C')
print(graph) ## {'A': ['B'], 'B': ['A'], 'C': []}


#add_edges_weighted('A','C',10)
#print(graph)  ## {'A': [['C', 10]], 'B': [], 'C': [['A', 10]]}


# add_edges_weighted_directed('A','B')
# add_edges_weighted_directed('C','B')
#print(graph) ## {'A': ['B'], 'B': [], 'C': ['B']}

# add_edges_weighted_directed('A','C',10)
# add_edges_weighted_directed('B','C',20)

add_edges('B','A')
add_edges('A','C')
add_edges('B','C')
print(graph)  ## {'A': [['C', 10]], 'B': [['C', 20]], 'C': []}

#delete_node('C')
#print(graph)

delete_edge('A','C')
print(graph)
