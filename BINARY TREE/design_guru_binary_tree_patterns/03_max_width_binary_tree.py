from collections import deque 
class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 

def max_width(root):
    if not root:
        return None 
    
    res = 0 
    q = deque([(root,1,0)]) # node , number , level 

    prevlevel = 0 
    prenum = 1 

    while q:

        node, num, level = q.popleft()

        if level > prevlevel:
            prevlevel = level 
            prenum = num 

        res = max(res, num-prenum+1)

        if node.lchild:
            q.append((node.lchild, 2 * num, level+1))
        
        if node.rchild:
            q.append((node.rchild, 2 * num + 1, level + 1 ))

    return res 

my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
#my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
#my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)


print(max_width(my_tree))