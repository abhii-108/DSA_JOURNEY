#Iterative Inorder Traversal in Binary Tree 
#Inorder Traversal Order: Left → Root → Right

##Key Insight: Use a stack to simulate recursion. Traverse leftmost first, then process nodes, then handle right subtrees.

class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None

def inorderTraversal(root):

    if not root:
        return []
    
    result = []
    stack = []

    current = root 

    while current or stack:
        # Traverse to deepest left node
        while current:
            stack.append(current)
            current = current.lchild
        
        # Process the node (leftmost)
        current = stack.pop()
        result.append(current.key)

        # Move to right subtree
        current = current.rchild

    return result


my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)


print(inorderTraversal(my_tree))