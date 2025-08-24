#One Traversal to Rule Them All
#Here's a simple way to remember Preorder, Inorder, and Postorder traversals in a single pass using one stack. Think of it as giving each node 3 lives (Pre, In, Post)!

# State 1 = Preorder (Root → Left → Right)
# State 2 = Inorder (Left → Root → Right)
# State 3 = Postorder (Left → Right → Root)
class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 


def allTraversal(root):
    if not root:
        return []
    
    stack = [(root,1)]

    pre = []
    ino = []
    post = []

    while stack:

        node , state = stack.pop()

        if state == 1:
            pre.append(node.key)
            stack.append((node,2))
            if node.lchild:
                stack.append((node.lchild,1))

        
        elif state == 2:
            ino.append(node.key)
            stack.append((node,3))
            if node.rchild:
                stack.append((node.rchild,1))
        
        else:
            post.append(node.key)


    return pre, ino, post 

# my_tree = TreeNode(10)

# my_tree.lchild = TreeNode(20)
# my_tree.rchild = TreeNode(30)
# my_tree.lchild.lchild = TreeNode(15)
# my_tree.lchild.rchild = TreeNode(23)
# my_tree.lchild.lchild.lchild = TreeNode(18)
# my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
# my_tree.rchild.lchild = TreeNode(33)
# my_tree.rchild.rchild = TreeNode(35)


my_tree = TreeNode(1)
my_tree.lchild = TreeNode(2)
my_tree.rchild = TreeNode(3)
my_tree.lchild.lchild = TreeNode(4)
my_tree.lchild.rchild = TreeNode(5)
my_tree.rchild.lchild = TreeNode(6)
my_tree.rchild.rchild = TreeNode(7)

pre_order, in_order, post_order = allTraversal(my_tree)
print(f'Pre-order {pre_order}')
print(f'In-order {in_order}')
print(f'Post-order {post_order}')