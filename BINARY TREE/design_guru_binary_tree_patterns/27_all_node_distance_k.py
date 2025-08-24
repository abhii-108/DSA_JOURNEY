#All Nodes Distance K in Binary Tree

# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.


from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        ans = []
        parent_child = {}

        def dfs(node):
            if not node:
                return
            
            if node.left:
                parent_child[node.left] = node 
            if node.right:
                parent_child[node.right] = node

            dfs(node.left)
            dfs(node.right)

        dfs(root)


        q = deque([(target, 0)])
        visited = {target}
        while q :

            curr_node,distance = q.popleft()
            # If we've reached the desired distance, add the node's value to the result
            if distance == k :
                ans.append(curr_node.val)
                # We can stop here and add any remaining nodes from the queue
                while q:
                    node, _ = q.popleft()
                    ans.append(node.val)
                return ans 
            
                    
            # Check neighbors: left, right, and parent
            if curr_node.left and curr_node.left not in visited:
                visited.add(curr_node.left)
                q.append((curr_node.left, distance+1))

            if curr_node.right and curr_node.right not in visited:
                visited.add(curr_node.right)
                q.append((curr_node.right, distance+1))

            # Parent (using our parent map)
 
            if curr_node in parent_child and parent_child[curr_node] not in visited:
                parent = parent_child[curr_node]
                visited.add(parent)
                q.append((parent, distance+1))
        
        return ans       


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)

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
root.left.right = TreeNode(1) 
root.right.left = TreeNode(1) 
root.right.right = TreeNode(1)
root.left.left.left = TreeNode(22) 
root.left.right.right = TreeNode(23) 
root.right.left.left = TreeNode(11) 
root.right.right.left = TreeNode(14)



one = Solution()
print(one.distanceK(root1,root1.left,1))

two = Solution()
print(two.distanceK(root,root.left,2))