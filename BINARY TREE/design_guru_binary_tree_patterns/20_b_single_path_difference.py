# Single Path Difference
# Question: Calculate the maximum absolute difference between any two adjacent nodes in a root-to-leaf path


# To solve this problem, we need to calculate the maximum absolute difference between any two adjacent nodes in any root-to-leaf path of a binary tree. The solution involves traversing each path from the root to a leaf node while tracking the absolute differences between consecutive nodes and updating the maximum difference encountered.


# Problem Analysis: The task is to find the maximum absolute difference between adjacent nodes (parent and child) in any path from the root to a leaf. The solution requires examining every parent-child pair along all root-to-leaf paths.

# Intuition: By performing a depth-first search (DFS), we can traverse each path from the root to the leaves. For each node (except the root), we compute the absolute difference between the node's value and its parent's value. The maximum of these differences across all paths is our result.

# Algorithm Selection: DFS is suitable here because it allows us to explore each path completely before backtracking. During traversal, we maintain a global maximum difference that gets updated whenever a larger absolute difference is found.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def max_adjacent_difference(root):
    if not root:
        return 0 
    
    max_diff = 0 

    def dfs(node, parent_val):
        nonlocal max_diff

        if parent_val:
            max_diff = max(max_diff, abs(node.val - parent_val))

        if node.left:
            dfs(node.left, node.val)
        if node.right:
            dfs(node.right, node.val)

    dfs(root,None)

    return max_diff


root3 = TreeNode(2)
root3.left = TreeNode(1)
root3.right = TreeNode(3)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)




print(f'{max_adjacent_difference(root3)}')

print(f'{max_adjacent_difference(root1)}')