# Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: root = [2,1,3]
# Output: true

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isvalid_bst(root):
    
    def valid(node, left, right):

        if not node:
            return True
        
        if not(node.val < right and node.val > left ):
            return False 
        
        return (valid(node.left, left, node.val) and  valid(node.right, node.val, right))
    

    return valid(root, float('-inf'), float('inf'))



root3 = TreeNode(2)
root3.left = TreeNode(1)
root3.right = TreeNode(3)


root1 = TreeNode(5)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)




print(f'{isvalid_bst(root3)}')

print(f'{isvalid_bst(root1)}')