# To Implement Graph Insertion Operation Adjacency Matrix 


def add_node(v):
    global node_count
    if v in nodes:
        print("The node is already present in graph")
    else:
        node_count += 1
        nodes.append(v)  ## appending new node to nodes list 
        # now we need to add new row & column to adjacency matrix with 0 value 
        ## First ADD the column 
        for n in graph:
            n.append(0)
        #now we create a row for new node to be added in adjacency matrix     
        temp = [0] * node_count
        graph.append(temp)

## To add Edge
def add_edge(v1,v2):
    # need to check if given nodes are present in graph 
    if v1 not in nodes:
        print(f"Given node {v1} is not present in garph")
    elif v2 not in nodes:
        print(f"Given node {v2} is not present in garph")
    else:
        # we need change in matrix from 0 to 1 
        #  Need to find index of v1 & v2 
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)

        graph[index1][index2] = 1
        graph[index2][index1] = 1

## undirected weighted graph 
def add_edge_cost(v1,v2,cost):
    # need to check if given nodes are present in graph 
    if v1 not in nodes:
        print(f"Given node {v1} is not present in garph")
    elif v2 not in nodes:
        print(f"Given node {v2} is not present in garph")
    else:
        # we need change in matrix from 0 to 1 
        #  Need to find index of v1 & v2 
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)

        graph[index1][index2] = cost
        graph[index2][index1] = cost


## directed weighted graph

def add_edge_weight_cost(v1,v2,cost):
    # need to check if given nodes are present in graph 
    if v1 not in nodes:
        print(f"Given node {v1} is not present in garph")
    elif v2 not in nodes:
        print(f"Given node {v2} is not present in garph")
    else:
        # we need change in matrix from 0 to 1 
        #  Need to find index of v1 & v2 
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)

        graph[index1][index2] = cost
        #graph[index2][index1] = cost

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"), end=" ")
        print()

nodes = [] ## all vertices are store to nodelist 
graph = []
node_count=0

print("Before adding a node ")
print(nodes)
add_node("A")
add_node("B")
add_node("C")
# add_edge('A','B')
# add_edge('C','B')

# add_edge_cost('A','B',20)
# add_edge_cost('C','B',10)


add_edge_weight_cost('A','B',20)
add_edge_weight_cost('C','B',10)


print("After node addition")
print(nodes)
print_graph()

# ['A', 'B', 'C']
# 0   20  0
# 20  0   10
# 0   10  0


# ['A', 'B', 'C']
# 0   20  0
# 0   0   0
# 0   10  0








