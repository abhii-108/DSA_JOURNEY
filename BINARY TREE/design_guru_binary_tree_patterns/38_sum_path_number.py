#Sum of Path Numbers 

#Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.

#The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxSum = 0 
        self.max_sum_arr = []

    
    def maxPathSum(self,root):
        
        self.findMaxSum(root,0)
        for x in self.max_sum_arr:
            self.maxSum += x
        return self.maxSum 
    
    def findMaxSum(self, node, curr_sum):

        #base case 
        curr_sum = curr_sum * 10 + node.val 

        if not node.left and not node.right:
            self.max_sum_arr.append(curr_sum) 
        
        if node.left:
            self.findMaxSum(node.left, curr_sum)
        if node.right:
         self.findMaxSum(node.right, curr_sum)
    

# Example usage
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)


solution = Solution()
print(solution.maxPathSum(root))  # Output: 408
