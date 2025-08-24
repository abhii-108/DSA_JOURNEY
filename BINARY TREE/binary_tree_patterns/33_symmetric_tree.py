#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Intuition
# To check if a binary tree is symmetric, we need to compare its left subtree and right subtree. To do this, we can traverse the tree recursively and compare the left and right subtrees at each level. If they are symmetric, we continue the traversal. Otherwise, we can immediately return false.

# Approach
# We can define a recursive helper function that takes two nodes as input, one from the left subtree and one from the right subtree. The helper function returns true if both nodes are null, or if their values are equal and their subtrees are symmetric.

# Complexity
# Time complexity:The time complexity of the algorithm is O(n), where n is the number of nodes in the binary tree. We need to visit each node once to check if the tree is symmetric.
# Space complexity:
# The space complexity of the algorithm is O(h), where h is the height of the binary tree. In the worst case, the tree can be completely unbalanced, and the recursion stack can go as deep as the height of the tree.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    if not root:
        return True
    
    def isMirror(left_subtree, right_subtree):
        if not left_subtree and not right_subtree:
            return True
        
        if not left_subtree or not right_subtree:
            return False 
        
        return (left_subtree.val == right_subtree.val) and isMirror(left_subtree.left, right_subtree.right) and isMirror(left_subtree.right, right_subtree.left)
    

    return isMirror(root.left, root.right)


my_tree = TreeNode(8)
my_tree.left = TreeNode(3)
my_tree.right = TreeNode(10)
my_tree.left.left = TreeNode(1)
my_tree.left.right = TreeNode(6)
my_tree.left.right.left = TreeNode(4)
my_tree.left.right.left.right = TreeNode(7)
my_tree.right.right = TreeNode(14)
my_tree.right.right.left = TreeNode(13)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)


print(isSymmetric(my_tree))

print(isSymmetric(root1))

print(isSymmetric(root3))