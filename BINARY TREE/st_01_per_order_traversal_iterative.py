## Iterative Preorder Traversal in Binary Tree 

#Preorder Traversal Order: Root → Left → Right
#Key Insight: Use a stack to simulate recursion (LIFO property). Process nodes in reverse order: push right child first, then left child.



class TreeNode:
    def __init__(self,key):
        self.val = key
        self.lchild = None
        self.rchild = None


def perorderTravesal(root):

    if not root:
        return []
    
    # Initialize stack with root
    stack = [root]
    result = []

    while stack:

        node = stack.pop()  # Step 1: Visit root node
        result.append(node.val)

        # Push right child first (so left is processed next)
        if node.rchild:     # Step 3: Process right subtree later
            stack.append(node.rchild)
        
        if node.lchild:     # Step 2: Process left subtree next
            stack.append(node.lchild)

    
    return result
    

my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.lchild.rchild = TreeNode(23)


print(perorderTravesal(my_tree))
