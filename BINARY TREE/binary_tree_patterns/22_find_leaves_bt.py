# Finding the Leaves of Binary Tree
# Using the DFS Approach
# To use DFS approach, we start at the root node and traverse the tree by recursively visiting each child node. Whenever a node is found with no left or right child, it is identified as a leaf node and added to our result list. The recursion ensures that each path from the root to the leaf is explored completely before backtracking, making it a straightforward and effective way to identify all leaf nodes in the tree. This approach is efficient due to its simplicity and because it leverages the natural structure of the tree, reducing the need for additional data structures.

# Step-by-Step Algorithm
# Step 1: Start at the root node of the binary tree.
# Step 2: If the current node is null, return (base case for recursion).
# Step 3: Check if the current node is a leaf node (both left and right children are null).
# a. If yes, add it to the list of leaf nodes.
# Step 4: Recursively call the function for the left child of the current node.
# Step 5: Recursively call the function for the right child of the current node.
# Step 6: Continue until all nodes have been visited.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Method to collect leaf nodes using DFS

    def findLeafNodes(self, root):
        leafNodes = []  # List to store leaf nodes
        self.findLeavesDFS(root, leafNodes)  # Helper method to perform DFS
        return leafNodes
    

    def findLeavesDFS(self, node, leafNodes):
        if not node:
            return

        if not node.left and not node.right:
            leafNodes.append(node.val)
            return 
        
        self.findLeavesDFS(node.left, leafNodes)
        self.findLeavesDFS(node.right, leafNodes)

    

        

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
print(f'{one.findLeafNodes(root3)}')

# print(f'{count_good_node(root1)}')
# print('---------')
# print(f'{count_good_node(my_tree)}')

print(f'{one.findLeafNodes(my_tree)}')