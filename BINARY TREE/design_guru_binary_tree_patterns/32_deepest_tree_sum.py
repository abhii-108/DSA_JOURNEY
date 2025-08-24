#Deepest Leaves Sum
## Given the root of a binary tree, return the sum of values of its deepest leaves.

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19


# We can do a simple Depth-First Traversal on the Tree. We can obviously do one dfs traversal and find the depth of the deepest level and in the second dfs pass, we will add only those nodes that are on the deepest level. But we don't actually need two passes. This can be done in just one DFS pass.

# We maintain sum which will store sum of values of deepest level nodes till now and deepest which will store the depth or level of the deepest nodes. There will be following cases available to us where current Node is -

# Not a Leaf Node - Traverse the left and right node of the current node.
# A Leaf Node - This case will have 3 sub-cases possible -
# depth > deepest - If current node is the deepest node observed till now, reset the sum to current node value and set deepest = depth.
# depth == deepest - The current node is part of the deepest nodes observed till now. Add current root value to sum.
# depth < deepest - This node is not the deepest node. Just ignore this node.
# A NULL Node - We can't traverse any further. So just return.
# Lastly, we will return the sum accumulated till now. The finaly value stored in sum will contain only the sum of value of the nodes (leaves) at deepest level. The implementation of this is given below -

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deepest_leave_sum(root):
    if not root:
        return 0 
    deepest = 0 
    sum = 0 

    def dfs(node, depth):
        nonlocal deepest
        nonlocal sum 

        if not node:
            return 0 
        
        if not node.left and not node.right:
            # case 1 
            if depth == deepest:
                sum += node.val 
            
            elif depth > deepest:
                sum = node.val
                deepest = depth

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
        return sum 
    
    return dfs(root, 0)


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
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)


print(deepest_leave_sum(my_tree))

print(deepest_leave_sum(root1))

print(deepest_leave_sum(root3))