from collections import deque

class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 

def zigzag(root):
    pass 

    res = []
    lefttoright = True
    q = deque([root])

    while q:
        res_q = deque()
        q_len = len(q)

        for _ in range(q_len):

            node = q.popleft()

            if lefttoright:
                res_q.append(node.key)
            else:
                res_q.appendleft(node.key)
            

            if node.lchild:
                q.append(node.lchild)
            
            if node.rchild:
                q.append(node.rchild)

        res.append(list(res_q))
        lefttoright = not lefttoright
    
    return res

            



my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)


print(zigzag(my_tree))