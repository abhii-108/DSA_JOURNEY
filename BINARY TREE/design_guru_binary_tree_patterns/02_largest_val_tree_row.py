from collections import deque 
class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 


def large_value_tree_row(root):
    
    if not root:
        return []
    
    q = deque([root])

    res = []

    while q:
        q_len = len(q)
        max_row_val = float('-inf')  # or q[0].key

        for _ in range(q_len):

            node = q.popleft()
            max_row_val = max(max_row_val, node.key)

            if node.lchild:
                q.append(node.lchild)
            
            if node.rchild:
                q.append(node.rchild)

        res.append(max_row_val)

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


print(large_value_tree_row(my_tree))