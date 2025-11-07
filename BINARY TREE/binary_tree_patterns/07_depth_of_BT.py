### depth of binary tree using BFS technique 

from collections import deque 

class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 

def depth_bfs(root):

    if not root:
        return 0
    
    q = deque([root])
    level = 0 

    while q :

        for _ in range(len(q)):

            node  = q.popleft()

            if node.lchild:
                q.append(node.lchild)
            if node.rchild:
                q.append(node.rchild)

        level += 1

    return level

def iterative_dfs(root):

    if not root:
        return 0 
    ## we use stack to store node & use pre-order iterative method 
    stack = [[root,1]]
    res = 0
    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)          
            stack.append([node.rchild, depth+1])
            stack.append([node.lchild, depth+1])

    return res 


def height_dfs(root):

    if not root:
        return 0 
    

    left = height_dfs(root.lchild)
    right = height_dfs(root.rchild)


    return 1+max(left,right)




my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.rchild = TreeNode(25)
# my_tree.rchild.lchild = TreeNode(33)
# my_tree.rchild.rchild = TreeNode(35)


print(depth_bfs(my_tree))
print(iterative_dfs(my_tree))
print(height_dfs(my_tree))