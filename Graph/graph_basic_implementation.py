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

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()

nodes = [] ## all vertices are store to nodelist 
graph = []
node_count=0

print("Before adding a node ")
print(nodes)
add_node("A")
add_node("B")
print("After node addition")
print(nodes)
print_graph()










