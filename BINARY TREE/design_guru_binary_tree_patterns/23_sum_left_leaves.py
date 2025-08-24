# Sum of Left Leaves (easy)
# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node that does not have any child nodes, and a left leaf is a leaf that is the left child of its parent.

# Examples
# Example 1:
# Input: root = [3,5,10,null,null,8,7]

# Expected Output: 13
# Justification: The leaf nodes are 5, 8, and 7, but only 5 and 8 are left leaf nodes. So, sum of left leaf nodes are 5 + 8 = 13.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Method to collect leaf nodes using DFS

    def sum_leave(self, root):
        self.sum = 0 # List to store leaf nodes
        
    

        def findLeavesDFS(node, is_left):
            if not node:
                return

            if not node.left and not node.right and is_left:
                self.sum += node.val
                return 
            
            findLeavesDFS(node.left, True )
            findLeavesDFS(node.right, False )
        
        findLeavesDFS(root, False)  # Helper method to perform DFS
        return self.sum

    

        

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


one = Solution()
print(f'{one.sum_leave(root1)}')

# print(f'{count_good_node(root1)}')
# print('---------')
# print(f'{count_good_node(my_tree)}')

print(f'{one.sum_leave(my_tree)}')