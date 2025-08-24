#  Count Good Nodes in Binary Tree

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.


# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.


# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def count_good_node(root):
    if not root:
        return 0 
    
    if not root.left and not root.right:
        return 1
 
    def dfs(node, curr_max):
        nonlocal count
        #Base case 
        if not node:
            return
        
        if node.val >=curr_max:
            count[0] += 1
            curr_max = node.val
     
        dfs(node.left, node.val)

        dfs(node.right, node.val) 

    count = [0]
    dfs(root,root.val)
    return count[0]



root3 = TreeNode(1)
root3.left = TreeNode(2)
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



print(f'{count_good_node(root3)}')

print(f'{count_good_node(root1)}')
print('---------')
print(f'{count_good_node(my_tree)}')