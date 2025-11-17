## Populating Next Right Pointers in Each Node II
# Need to connect each node to its "next right" neighbor

#Given a root of the binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

# op should be like this if we iterate it 
# 1 -> null
# 2 -> 3 -> null
# 4 -> 5 -> 7 -> null

from collections import deque 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


def level_order_sibling(root):

    if not root:
        return
    
    q = deque([root])

    while q :
        q_len = len(q)
        prev_node = None 

        for _ in range(q_len):
            curr_node = q.popleft()

            if prev_node:
                prev_node.next = curr_node
            
            prev_node = curr_node 

            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)

    return root 


def all_level_order_sibling(root):

    if not root:
        return
    
    q = deque([root])
    prev_node = None 
    while q :
        q_len = len(q)
        
        curr_node = q.popleft()

        if prev_node:
            prev_node.next = curr_node
        
        prev_node = curr_node 

        if curr_node.left:
            q.append(curr_node.left)
        if curr_node.right:
            q.append(curr_node.right)

    return root 
    

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

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)

current_level_node  = level_order_sibling(my_tree)
all_level_node = all_level_order_sibling(root1)

# Loop through each level
while current_level_node:
    # 'current_node' is a temporary pointer to iterate through the current level's nodes.
    current_node = current_level_node
    
    # Loop through all nodes on the current level using the 'next' pointer
    while current_node:
        print(f"{current_node.val} -> ", end="")
        current_node = current_node.next
    
    print("null") # Indicate the end of the level
    
    # Move to the next level by finding the first node of the next level
    current_level_node = current_level_node.left if current_level_node.left else current_level_node.right


## all_level_order_sibling
print('------------- OP of all_level_order_sibling -----------------')
current_node = all_level_node
while current_node:
    print(f"{current_node.val} -> ", end="")
    current_node = current_node.next
print("null")



# Here is a step-by-step plan for the BFS approach:

# Initialize a queue: Start with a queue containing the root node.

# Process level by level: Use a while loop that continues as long as the queue isn't empty. Inside the loop, get the size of the queue to know how many nodes are on the current level.

# Connect nodes: Use a for loop to iterate size times, processing one node at a time. Keep track of the previous_node from the same level.

# Dequeue and connect: Dequeue the current_node. If there's a previous_node (meaning it's not the first node on the level), set its next pointer to the current_node. Then, update the previous_node to the current_node.

# Enqueue children: Add the left and right children of the current_node to the queue for the next level's processing.

# This method guarantees that each node is connected to its right sibling, and the last node on each level correctly points to None. This approach works for all binary trees, not just perfect ones.