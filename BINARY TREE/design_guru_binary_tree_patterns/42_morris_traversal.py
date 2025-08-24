# ## Morris Inorder Traversal

# Morris Traversal allows you to traverse a binary tree in-order without using recursion or a stack, achieving O(1) space complexity. It works by temporarily modifying the tree structure to create links to successors and then reverting these changes.

# Approach
# Threaded Binary Tree: Create temporary links (threads) from the rightmost node of a left subtree to its successor.

# Traversal without Extra Space: Use these threads to navigate the tree without recursion or a stack.

# In-order Processing: Process nodes when moving to the right after handling the left subtree.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        current = root

        while current:

            if not current.left:
                result.append(current.val)
                current = current.right
            
            else:
                predecessor = current.left 

                while predecessor.right and (predecessor.right !=  current):
                    predecessor = predecessor.right 

                
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left

                else:
                    result.append(current.val)
                    predecessor.right = None
                    current = current.right

        return result
    

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)



one = Solution()
print(one.inorderTraversal(root1))