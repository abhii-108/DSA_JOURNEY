# You are given the root of a binary tree, where each node holds either a 0 or 1. Each path from the root to a leaf forms a binary number.

# For example, if the path is 1 -> 0 -> 1, then this could represent 101 in binary, which is 5 in decimal representation. You need to consider all these root-to-leaf paths, convert them to binary numbers and sum them.

# Return the total sum of all these binary numbers.

# The test cases are generated so that the answer fits in a 32-bits integer.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxSum = 0

    
    def sumRootToLeaf(self,root):
        
        self.findMaxSum(root,0)
        return self.maxSum
    
    def findMaxSum(self, node, curr_sum):

        if not node:
            return
        
        curr_sum = curr_sum * 2 + node.val  ## for binary we need this calculation

        if not node.left and not node.right:
            self.maxSum += curr_sum

        
        self.findMaxSum(node.left, curr_sum)
        self.findMaxSum(node.right, curr_sum)
    

# Example usage
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)


solution = Solution()
print(solution.sumRootToLeaf(root))  # Output: 16
