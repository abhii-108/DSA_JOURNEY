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