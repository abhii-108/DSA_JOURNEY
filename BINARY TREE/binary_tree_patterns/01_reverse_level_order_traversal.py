from collections import deque 
class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 


def reversed_levelOrder(root):

    if not root:
        return []
    

    q = deque([root])
    res = []

    while q:

        q_len = len(q)

        for _ in range(q_len):

            node = q.popleft()

            res.append(node.key)

            if node.rchild:
                q.append(node.rchild)

            if node.lchild:
                q.append(node.lchild)

    print(res)
    return [ res[i] for i in range(len(res)-1, -1, -1)] 


my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)


print(reversed_levelOrder(my_tree))