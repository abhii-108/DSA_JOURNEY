#Level Order Traversal of a Binary Tree
#Level order traversal visits nodes level-by-level from left to right. Think of it as a Breadth-First Search (BFS) where we process nodes in the order they appear at each depth.

# Approach:
# Use a Queue:

# Start with the root node in a queue.

# Process nodes level-by-level: For each node, add its children to the queue.

# Track Levels:

# For each level, determine the number of nodes (queue size).

# Process all nodes at that level in a single iteration.

# Time Complexity: O(N) → Each node visited exactly once
# Space Complexity: O(N) → Queue stores all nodes at the widest level

from collections import deque

class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 

    
def levelOrder(root):

    if not root:
        return []
    

    result = []
    queue = deque([root])


    while queue:

        level_size = len(queue)
        current_level = []


        for _ in range(level_size):
            node = queue.popleft()
            
            current_level.append(node.key)

            if node.lchild:
                queue.append(node.lchild)
            
            if node.rchild:
                queue.append(node.rchild)

        result.append(current_level)

    return result


my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)


print(levelOrder(my_tree))
