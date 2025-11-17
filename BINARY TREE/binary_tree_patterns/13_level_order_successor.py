#To find the level order successor of a node with a given key, we can use a Breadth-First Search (BFS) traversal. 
#BFS explores the tree level by level, which is exactly the order needed for this problem.

#The strategy is to perform a standard BFS. We'll use a queue to store the nodes to be visited. 
#As we dequeue each node, we check if its value matches the given key. If we find the node, the very next node we dequeue will be its level order successor.

# Given a root of the binary tree and an integer key, find the level order successor of the node containing the given key as a value in the tree.

# The level order successor is the node that appears right after the given node in the level order traversal.

# Examples
# Example 1
# Input: root = [1, 2, 3, 4, 5], key = 3
# Output: 4
# Explanation: The level-order traversal of the tree is [1, 2, 3, 4, 5]. The successor of 3 in this order is 4.
# Example 2
# Input: root = [12, 7, 1, 9, null, 10, 5], key = 9
# Output: 10

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_successor(root, key):
    if not root:
        return None 
    
    q = deque([root])

    while q :
        curr_node = q.popleft()

        if curr_node.left:
            q.append(curr_node.left)

        if curr_node.right:
            q.append(curr_node.right)

        if curr_node.val == key:

            if q:
                op = q.popleft()
                return op.val 
            
            else:
                return None
    return None



my_tree = TreeNode(10)
my_tree.left = TreeNode(20)
my_tree.right = TreeNode(30)
my_tree.left.left = TreeNode(15)
my_tree.left.right = TreeNode(23)
my_tree.left.left.left = TreeNode(18)
my_tree.left.left.right = TreeNode(19)
my_tree.left.left.left.left = TreeNode(28)
my_tree.left.left.left.right = TreeNode(25)
my_tree.right.left = TreeNode(33)
my_tree.right.right = TreeNode(35)


print(f'{level_order_successor(my_tree, 18)}')
