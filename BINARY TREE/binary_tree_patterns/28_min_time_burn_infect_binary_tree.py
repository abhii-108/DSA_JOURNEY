# ## find the minimum time required to infect the entire binary tree starting from a given node. The infection spreads to adjacent nodes (parent, left child, right child) every second. The solution involves:

# Tree to Graph Conversion: Convert the binary tree into an undirected graph to easily traverse in all directions (parent, left, right).

# BFS Traversal: Use BFS starting from the target node to simulate the spread of infection. Track the time taken to reach each node.

# Maximum Time: The answer is the maximum time taken to infect any node, which indicates when the entire tree is infected.

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountTime(self, root: TreeNode, start:int ) -> int:
        ## Build Tree graph 
        graph = defaultdict(list)
        st = [root]

        while st:
            node = st.pop()

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                st.append(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                st.append(node.right)
        
        # BFS from start node

        visited=set()
        visited.add(start)
        q = deque([(start,0)]) ## node, time 
        max_time=0 

        while q:
            
            node, time = q.popleft()
            max_time = max(max_time, time )

            for nb in graph[node]:
                if nb not in visited:
                    visited.add(nb)
                    q.append((nb, time+1))

        
        return max_time 


root2 = TreeNode(0)
root2.left = TreeNode(1)
root2.right = TreeNode(5)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(20)

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(21) 
root.left.right = TreeNode(12) 
root.right.left = TreeNode(13) 
root.right.right = TreeNode(16)
root.left.left.left = TreeNode(22) 
root.left.right.right = TreeNode(23) 
root.right.left.left = TreeNode(11) 
root.right.right.left = TreeNode(14)



one = Solution()
print(one.amountTime(root2, 5))

two = Solution()
print(two.amountTime(root,21))