from collections import deque 

class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 

def min_depth_bfs(root):

    if not root:
        return 0 
    
    q = deque([(root, 1)])  ## node, depth
    while q :

        for _ in range(len(q)):

            node, depth = q.popleft()

            if not node.lchild and not node.rchild:
                return depth
            
            if node.lchild:
                q.append((node.lchild, depth+1))
            
            if node.rchild:
                q.append((node.rchild, depth+1))

        
    return depth

def min_depth_dfs(root):

    if not root :
        return 0  # Empty tree has depth 0
    
    # Leaf node: depth = 1
    if not root.lchild and not root.rchild:
        return 1
    
    # Only right child exists: min depth from left subtree
    if not root.lchild:
        return 1 + min_depth_dfs(root.rchild)

    # Only left child exists: min depth from right subtree
    if not root.rchild:
        return 1 + min_depth_dfs(root.lchild)
    
    # Both children exist: return min of both subtrees
    return 1 + min(min_depth_dfs(root.lchild), min_depth_dfs(root.rchild))

def min_depth_dfs2(root):

    if not root:
        return 0 
    

    left = min_depth_dfs2(root.lchild)
    right = min_depth_dfs2(root.rchild)


    return 1+min(left,right)    




my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)


print(min_depth_bfs(my_tree))
print('min depth using DFS ')
print(min_depth_dfs2(my_tree))