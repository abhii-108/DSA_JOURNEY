#Instead of just checking if a path with the target sum exists, we need to find and return all such paths.

# DFS Traversal with Backtracking: Use depth-first search to explore all root-to-leaf paths.

# Path Tracking: Maintain the current path and current sum while traversing.

# Leaf Check: When reaching a leaf node, check if the current sum matches targetSum.

# Backtracking: After processing a node, remove it from the current path to backtrack
# Backtracking: After each recursive call returns, we "backtrack" by removing the current node's value from the path. This is a crucial step that allows us to explore other branches of the tree without carrying over incorrect path information.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathsum(root : TreeNode, targetsum: int) -> list[list[int]]:
    result = [] 

    def dfs(node, curr_sum, curr_path):

        if not node:
            return
        
        curr_sum += node.val 
        curr_path.append(node.val)

        if not node.left and not node.right and curr_sum == targetsum:
            result.append(list(curr_path))

        
        dfs(node.left, curr_sum, curr_path)
        dfs(node.right, curr_sum, curr_path)

        curr_path.pop()

    dfs(root, 0, [])
    return result

        

            

my_tree = TreeNode(10)
my_tree.left = TreeNode(20)
my_tree.right = TreeNode(30)
my_tree.left.left = TreeNode(15)
my_tree.left.right = TreeNode(23)
my_tree.left.left.left = TreeNode(18)
my_tree.left.left.right = TreeNode(19)
my_tree.left.left.left.left = TreeNode(28)
my_tree.left.left.left.right = TreeNode(25)
my_tree.right.left = TreeNode(33)
my_tree.right.right = TreeNode(35)

root3 = TreeNode(5)
root3.left = TreeNode(4)
root3.right = TreeNode(8)
root3.left.left = TreeNode(11)
root3.left.left.left = TreeNode(7)
root3.left.left.right = TreeNode(2)
root3.right.left = TreeNode(13)
root3.right.right = TreeNode(4)
root3.right.right.left = TreeNode(5)
root3.right.right.right = TreeNode(1)

root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(20)



print(f'{pathsum(my_tree,53)}')

print(f'{pathsum(root3,22)}')


# print(f'{haspathsum(my_tree,53)}')

# print(f'{haspathsum(root1,15)}')