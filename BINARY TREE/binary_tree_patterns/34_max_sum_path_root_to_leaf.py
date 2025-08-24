# Given a binary tree where each node contains an integer, return the maximum sum obtained by following any path from the root node to a leaf node.

# The path must start at the root and end at a leaf.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    
    def maxPathSum(self,root):
        
        self.findMaxSum(root,0)
        return self.maxSum
    
    def findMaxSum(self, node, curr_sum):

        if not node:
            return
        
        curr_sum += node.val 

        if not node.left and not node.right:
            self.maxSum = max(self.maxSum, curr_sum)

        
        self.findMaxSum(node.left, curr_sum)
        self.findMaxSum(node.right, curr_sum)
    

# Example usage
root = TreeNode(8)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right = TreeNode(9)

solution = Solution()
print(solution.maxPathSum(root))  # Output: 18
