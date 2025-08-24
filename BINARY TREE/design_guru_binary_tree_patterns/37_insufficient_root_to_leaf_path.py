# Insufficient Nodes in Root to Leaf Paths
# Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

# A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

# A leaf is a node with no children.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
def sufficient_subset(root, limit):

    def dfs(node, curr_sum, limit):

        # base condition 
        if not node.left and not node.right:
            if curr_sum + node.val >= limit:
                return True
            return False
        
        curr_sum += node.val 

        left_ret = False 
        right_ret = False 

        if node.left:
            left_ret = dfs(node.left, curr_sum, limit)
        
        if node.right:
            right_ret = dfs(node.right, curr_sum, limit)

        
        if node.left == False:
            node.left = None
        if node.right == False:
            node.right = None 

        return left_ret or right_ret 
    
    ret_val = dfs(root, 0, limit)

    if ret_val == False:
        return None 
    
    return root 
            

# Example usage
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(1)
root.right.left = TreeNode(17)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(3)
root.right.right.left = TreeNode(5)



print(sufficient_subset(root,22))  # Output: 16
