from collections import deque

class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 

def max_level_sum(root):

    if not root:
        return 0
    
    q = deque([root])

    res = float('-inf')

    while q :
        q_len = len(q)

        level_sum  = 0 

        for _ in range(q_len):

            node = q.popleft()

            level_sum += node.key 


            if node.lchild:
                q.append(node.lchild)

            if node.rchild:
                q.append(node.rchild)
        
        res = max(res,level_sum)

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


print(max_level_sum(my_tree))