class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

############## using subtraction method ############## single function only 
def pathsum(root, targetsum):
    if not root:
        return False
    
    if root.left is None and root.right is None:
        return root.val == targetsum
    
    curr_sum = targetsum - root.val 

    return (pathsum(root.left, curr_sum) or pathsum(root.right, curr_sum))

############## using Addition method having helper function ############## 
def haspathsum(root, targetsum):

    def dfs(node, curr_sum):

        if not node:
            return False
        
        curr_sum += node.val
        if node.left is None and node.right is None:
            return targetsum == curr_sum
        

        return (dfs(node.left, curr_sum) or  dfs(node.right, curr_sum))
    
    return dfs(root, 0)


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



print(f'{pathsum(my_tree,53)}')

print(f'{pathsum(root1,15)}')


print(f'{haspathsum(my_tree,53)}')

print(f'{haspathsum(root1,15)}')