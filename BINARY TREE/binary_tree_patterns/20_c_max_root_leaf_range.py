# #Root-to-Leaf Range Tracking
# ##For each leaf node, compute the difference (max_value_in_path - min_value_in_path). Return the maximum difference across all leaves.


# To solve the problem of finding the maximum difference between the maximum and minimum values in any root-to-leaf path, we can use a depth-first search (DFS) approach. The key steps are:

# DFS Traversal: Traverse the tree from the root to each leaf node.

# Track Min and Max: For each node visited in the current path, update the current minimum and maximum values encountered so far.

# Leaf Node Check: When a leaf node is reached, compute the difference between the maximum and minimum values in the path and update the global maximum difference if this difference is larger.

# Recursive Processing: Continue processing left and right subtrees recursively, propagating the current minimum and maximum values.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def max_root_to_leaf_range(root):
    if not root:
        return 0 
    
    max_diff = 0 

    def dfs(node, curr_min, curr_max):
        nonlocal max_diff
        new_min = min(curr_min, node.val)
        new_max = max(curr_max, node.val)


        if not node.left and not node.right:
            max_diff = max(max_diff, new_max-new_min)
            return

        
        if node.left:
            dfs(node.left,new_min, new_max)
        
        if node.right:
            dfs(node.right, new_min, new_max)

    dfs(root, root.val, root.val)

    return max_diff


root3 = TreeNode(2)
root3.left = TreeNode(1)
root3.right = TreeNode(3)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)




print(f'{max_root_to_leaf_range(root3)}')

print(f'{max_root_to_leaf_range(root1)}')