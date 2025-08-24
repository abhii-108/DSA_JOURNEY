#Minimum/Maximum in Tree Paths

# we need to find the minimum and maximum values along every root-to-leaf path in a binary tree. The solution involves traversing each path from the root to a leaf node while keeping track of the minimum and maximum values encountered along the path. Once a leaf node is reached, the recorded minimum and maximum values for that path are added to their respective result lists.


# Problem Analysis: The task is to traverse each root-to-leaf path in a binary tree and record the minimum and maximum values encountered in each path. The results should be stored in two separate lists: one for minimum values and one for maximum values, corresponding to each path.

# Intuition: Using a depth-first search (DFS) approach, we can traverse each path from the root to the leaves. During the traversal, we maintain the current minimum and maximum values encountered so far in the path. When a leaf node is reached, the current minimum and maximum values for that path are added to the result lists.

# Algorithm Selection: DFS is suitable here because it allows us to explore each path completely before backtracking. For each node visited, we update the current minimum and maximum values. If the node is a leaf, we record these values.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_min_max_paths(root):
    min_list = []
    max_list = []

    if not root :
        return min_list, max_list
    
    def dfs(node, curr_min, curr_max):

        new_min = min(curr_min, node.val)
        new_max = max(curr_max, node.val)


        if not node.left and not node.right:
            min_list.append(new_min)
            max_list.append(new_max)
            return
        
        if node.left:
            dfs(node.left,new_min, new_max)
        
        if node.right:
            dfs(node.right, new_min, new_max)

    dfs(root, root.val, root.val)


    return min_list, max_list



root3 = TreeNode(2)
root3.left = TreeNode(1)
root3.right = TreeNode(3)


root1 = TreeNode(5)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)




print(f'{find_min_max_paths(root3)}')

print(f'{find_min_max_paths(root1)}')