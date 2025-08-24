# #Boundary Traversal of binary tree
# Given a binary tree, the task is to find the boundary nodes of the binary tree Anti-Clockwise starting from the root.


# The boundary includes:

# left boundary (nodes on left excluding leaf nodes)
# leaves (consist of only the leaf nodes)
# right boundary (nodes on right excluding leaf nodes)
# The left boundary is defined as the path from the root to the left-most leaf node (excluding leaf node itself).
# The right boundary is defined as the path from the root to the right-most leaf node (excluding leaf node itself).

# Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def left_boundary(node,result):
    if not node:
        return 
    
    if node.left or node.right:
        result.append(node.val)

    if node.left:
        left_boundary(node.left, result)
    elif node.right:
        left_boundary(node.right, result)


def leaves(node,result):
    if not node:
        return 

    if not node.left and not node.right:
        result.append(node.val)

    leaves(node.left, result)
    leaves(node.right, result)


def right_boundary(node, result):
    if not node:
        return 

    if node.right:
        right_boundary(node.right, result)
    elif node.left:
        right_boundary(node.left, result)

    ## backtracking of recursion also check this not a leave node 
    if node.left or node.right:
        result.append(node.val)




def boundary_traversal(root):
    if not root:
        return root
    result = []
    if root.left or root.right:
        result.append(root.val)

    left_boundary(root.left, result)

    leaves(root, result)

    right_boundary(root.right, result)

    return result


root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)

my_tree = TreeNode(8)
my_tree.left = TreeNode(3)
my_tree.right = TreeNode(10)
my_tree.left.left = TreeNode(1)
my_tree.left.right = TreeNode(6)
my_tree.left.right.left = TreeNode(4)
my_tree.left.right.left.right = TreeNode(7)
my_tree.right.right = TreeNode(14)
my_tree.right.right.left = TreeNode(13)


print(boundary_traversal(my_tree))