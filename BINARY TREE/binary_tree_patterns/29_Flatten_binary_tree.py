# ## Flatten Binary Tree 

# To flatten a binary tree into a linked list in-place (where the linked list follows the pre-order traversal order), we use a reverse pre-order traversal (right subtree first, then left subtree, then root). This approach ensures that we build the linked list from the end backwards, avoiding lost references to nodes.

# Approach
# Reverse Pre-order Traversal: Traverse the tree in the order: right, left, root. This means we process the right subtree first, then the left subtree, and finally the current node.

# Global Pointer: Maintain a global variable prev that points to the last node processed in the flattened list. Initially, prev is None.

# Node Processing: For each node:

# Set its right pointer to prev (the last node processed).

# Set its left pointer to None.

# Update prev to the current node.

# This method efficiently flattens the tree without extra space, as it only uses recursion and a single global variable.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root:TreeNode) -> None:
        prev = None 

        def dfs(node):
            nonlocal prev 
            if not node:
                return
            
            dfs(node.right)
            dfs(node.left)
            
            node.right = prev
            node.left = None 
            prev = node 

        dfs(root)
        return root


def preorder(root):
    if root is None:
        #print("N ", end="")
        return

    print(f'{root.val} ', end="")

    preorder(root.left)
    preorder(root.right)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)



one = Solution()
tree=one.flatten(root1)

preorder(tree)
