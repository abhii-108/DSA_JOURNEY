
class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 


def diameter(root):

    # Use a list to pass the max_diameter by reference max_diameter = [0]
    max_diameter = 0

    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0
        

        left_ht = dfs(node.lchild)
        right_ht = dfs(node.rchild)

        current_diameter = left_ht + right_ht
        max_diameter = max(max_diameter,current_diameter)

        return 1 + max(left_ht, right_ht)
    

    dfs(root)

    return max_diameter


my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)



print(diameter(my_tree))