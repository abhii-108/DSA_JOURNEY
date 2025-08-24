#Let's tackle "Path Sum III" (LeetCode 437). This problem is a more complex variation where the paths don't have to start at the root or end at a leaf. They can start and end at any node in the tree.
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathsum(root, targetSum):
    
    if not root:
        return 0 
    
    count = dfs(root, targetSum)

    count += pathsum(root.left, targetSum)
    count += pathsum(root.right, targetSum)
    
    return count 

def dfs(node, targetSum):
    if not node:
        return 0 
    
    count = 0 

    if node.val == targetSum:
        count += 1
    
    count += dfs(node.left, targetSum - node.val)
    count += dfs(node.right, targetSum - node.val)

    return count


############################## o(n) solution ####################

def haspathsum(root, target):
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1


    def dfs(node, curr_sum):
        if not node:
            return 0 
        
        curr_sum += node.val 

        count = prefix_sum_count.get(curr_sum - target, 0)

        prefix_sum_count[curr_sum] += 1


        count += dfs(node.left, curr_sum)
        count += dfs(node.right, curr_sum)

        ## for backtracking 

        prefix_sum_count[curr_sum] -= 1

        return count 
    

    return dfs(root,0)


###################################

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
root1.right = TreeNode(-3)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(2)
root1.left.left.left = TreeNode(3)
root1.right.right = TreeNode(11)
root1.left.right.left = TreeNode(-2)
root1.left.right.right = TreeNode(1)



print(f'{pathsum(my_tree,53)}')

print(f'{pathsum(root3,22)}')


print(f'{pathsum(root1,8)}')

print(f'{haspathsum(root1,8)}')