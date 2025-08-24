class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def min_root_leaf_sum(root):

    if not root:
        return float('inf')
    
    if (root.left is None) and (root.right is None):
        return root.val 
    
    leftsum = min_root_leaf_sum(root.left)
    rightsum = min_root_leaf_sum(root.right)

    return root.val + min(leftsum, rightsum)



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

root3 = TreeNode(8)
root3.left = TreeNode(40)
root3.right = TreeNode(12)
root3.right.left = TreeNode(10)
root3.right.right = TreeNode(18)
root3.right.left.left = TreeNode(2)

root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(20)


print(f'{min_root_leaf_sum(my_tree)}')

print(f'{min_root_leaf_sum(root1)}')