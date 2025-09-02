## Reorder Routes to Make All Paths Lead to the City Zero

# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

from collections import deque, defaultdict
from typing import List 


def minReorder(n: int, connections: List[List[int]]) -> int:

    forward_edge = defaultdict(list)
    backward_edge = defaultdict(list)
    ans = 0 
    visited = set()

    for x, y in connections:

        forward_edge[x].append(y)
        backward_edge[y].append(x)

    # print(forward_edge)
    # print(backward_edge) 

    def dfs(node, forward, backward,  visited):
        nonlocal ans
        visited.add(node)

        for x in forward[node]:
            #print(f'foward matrix {node} its value {x} current ans {ans}')
            if x not in visited:
                ans += 1 
                dfs(x, forward, backward, visited)
        
        for y in backward[node]:
            #print(f'backward matrix {node} its value {y} current ans {ans}')
            if y not in visited:
                #print(ans)
                dfs(y, forward, backward,visited)
        
        return ans 

    
    return dfs(0, forward_edge, backward_edge, visited) 
    

print(minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))

print(minReorder(5,[[1,0],[1,2],[3,2],[3,4]]))

print(minReorder(2,[[1,0],[2,0]]))