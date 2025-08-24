## Iterative Post order Traversal (using two stack )

def postOrderTraversal(root):
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []

    while stack1:

        node = stack1.pop()
        stack2.append(node)

        if node.lchild:
            stack1.append(node.lchild)
        
        if node.rchild:
            stack1.append(node.rchild)

    result = []

    while stack2:
        result.append(stack2.pop().key)

    
    return result


# Iterative Postorder Traversal Using Single Stack (Python Solution)
# Postorder Traversal Order: Left → Right → Root
# Key Insight: Use a single stack with careful state tracking. We need to know if we're returning from the left or right subtree before processing a node.

# Approach:
# Initialize:
# Start with root node in stack
# Track current node and last visited node (prev)

# Traverse Left:
# Go as left as possible, pushing nodes

# Check Right Subtree:
# If right exists and hasn't been visited, move right

# Process Node:
# When no right subtree or right is processed, pop and record
# Mark current as processed (prev = node)
# Reset current to avoid reprocessing

def postOrdeTraversal2(root):
    if not root:
        return []
    
    stack = []
    result = []
    current = root 

    prev = None 

    while current or stack:
        # Traversal to the deepest left node 

        while current:
            stack.append(current)
            current = current.lchild 

        # Peek top of stack without popping 
        top = stack[-1]


        #if right exist and not processed then go to right 
        if top.right and top.right != prev :
            current = top.right

        else:
            result.append(top.key)
            prev = top 
            stack.pop()

    return result




