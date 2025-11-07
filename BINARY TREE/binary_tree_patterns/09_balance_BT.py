# Determine if a binary tree is height-balanced.

# A binary tree is considered height-balanced if, for each node, the difference in height between its left and right subtrees is no more than one.
# Input:
#     3
#    / \
#   9  20
#      / \
#     15  7
# Expected Output: true
# Justification: Every node in the tree has a left and right subtree depth difference of either 0 or 1.
# Input:
#         1
#       /   \
#      2     2
#     / \   / \
#    3   3 3   3
#   / \       / \
#  4   4     4   4
# Expected Output: true

class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 


def balance_tree(root):

    def dfs (node):

        if not node:
            return 0 
        
        left = dfs(node.lchild)
        right = dfs(node.rchild)


        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1 
        
        return 1 + max(left, right)
    

    return dfs(root) != -1 


def isBalanced(root):

    def dfs2(node):
        if not node:
            return [True, 0] # if there are no node then it is balance and height is 0 
        
        left2 = dfs2(node.lchild)
        right2 = dfs2(node.right)

        #case1 - difference between left and right subtree for there height 
        #case 2 & 3 check if any of the subtree is false or not.. This will only become false due to case 1 and will get carried till root 
        # 
        balance = (abs(left2[1] - right2[1]) <= 1) and left2[0] and right2[0] 

        return [balance, 1+max(left2[1], right2[1])]
    
    return dfs2(root)[0]

my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)


print(balance_tree(my_tree))