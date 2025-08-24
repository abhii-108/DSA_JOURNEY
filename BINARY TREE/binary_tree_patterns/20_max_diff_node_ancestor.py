# Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_diff_ancestor(root):
    if not root:
        return 0 
    
    diff = -1
    
    def dfs(node, min_val, max_val):
        nonlocal diff
        ## base condition
        if not node :
            return 
        
        min_val = min(min_val, node.val)
        max_val = max(max_val, node.val)

        diff = max(diff, abs(max_val - min_val)) 


        if node.left:
            dfs(node.left, min_val, max_val)

        if node.right:
            dfs(node.right, min_val, max_val)


    
    dfs(root, root.val, root.val)

    return diff 
        



root3 = TreeNode(2)
root3.left = TreeNode(1)
root3.right = TreeNode(3)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)

my_tree = TreeNode(8)
my_tree.left = TreeNode(3)
my_tree.right = TreeNode(10)
my_tree.left.left = TreeNode(1)
my_tree.left.right = TreeNode(6)
my_tree.left.right.left = TreeNode(4)
my_tree.left.right.left.right = TreeNode(7)
my_tree.right.right = TreeNode(14)
my_tree.right.right.left = TreeNode(13)



print(f'{max_diff_ancestor(root3)}')

print(f'{max_diff_ancestor(root1)}')
print('---------')
print(f'{max_diff_ancestor(my_tree)}')