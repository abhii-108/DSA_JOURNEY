#To find the level order successor of a node with a given key, we can use a Breadth-First Search (BFS) traversal. 
#BFS explores the tree level by level, which is exactly the order needed for this problem.

#The strategy is to perform a standard BFS. We'll use a queue to store the nodes to be visited. 
#As we dequeue each node, we check if its value matches the given key. If we find the node, the very next node we dequeue will be its level order successor.

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_successor(root, key):
    if not root:
        return None 
    
    q = deque([root])

    while q :
        curr_node = q.popleft()

        if curr_node.left:
            q.append(curr_node.left)

        if curr_node.right:
            q.append(curr_node.right)

        if curr_node.val == key:

            if q:
                op = q.popleft()
                return op.val 
            
            else:
                return None
    return None



my_tree = TreeNode(10)
my_tree.left = TreeNode(20)
my_tree.right = TreeNode(30)
my_tree.left.left = TreeNode(15)
my_tree.left.right = TreeNode(23)
my_tree.left.left.left = TreeNode(18)
my_tree.left.left.right = TreeNode(19)
my_tree.left.left.left.left = TreeNode(28)
my_tree.left.left.left.right = TreeNode(25)
my_tree.right.left = TreeNode(33)
my_tree.right.right = TreeNode(35)


print(f'{level_order_successor(my_tree, 18)}')
