#All Nodes Distance K in Binary Tree

# Solution Overview (BFS)
# Here's how the two-step BFS process works in detail:

# Step 1: Building the Parent Map

# Create a dictionary, let's call it parent_map.

# Perform a DFS or BFS traversal starting from the root.

# For each node, if it has a left child, add an entry to the parent_map where the key is the child and the value is the parent. Do the same for the right child.

# Step 2: BFS from the Target Node

# Initialize a queue with the target node and its distance, which is 0. So the queue starts as [(target, 0)].

# Initialize a visited set and add the target node to it. This prevents you from going back to the target node.

# Loop as long as the queue is not empty.

# In each iteration, dequeue (current_node, distance).

# Check if the distance is equal to K. If it is, you've found a node at the correct distance, so add it to your results list.

# If the distance is less than K, you need to explore further:

# Explore the left child: If the current_node has a left child and it hasn't been visited, add it to the queue with a distance of distance + 1 and mark it as visited.

# Explore the right child: Do the same for the right child.

# Explore the parent: This is where the parent map comes in. Look up the parent of the current_node in your parent_map. If a parent exists and it hasn't been visited, add it to the queue with a distance of distance + 1 and mark it as visited.

# Once the BFS loop finishes, the result list will contain all the nodes at distance K from the target.

from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:

def distancek(root, target, k):

    parent_map = {}

    def build_parent_map(node, parent):
        if not node:
            return
        if parent:
            parent_map[node] = parent 
        
        build_parent_map(node.left, node)
        build_parent_map(node.right, node)

    build_parent_map(root, None)


    q = deque([(target, 0 )]) # target node ,  distance of target node is 0 

    visited = set([target])
    result = []

    while q:

        curr_node, dist = q.popleft()

        if dist == k :
            result.append(curr_node.val)
            continue

        ## for left child 
        if curr_node.left and curr_node.left not in visited:
            visited.add(curr_node.left)
            q.append((curr_node.left, dist + 1))
        
        ## for right child 
        if curr_node.right and curr_node.right not in visited:
            visited.add(curr_node.right)
            q.append((curr_node.right, dist+1))


        # for parent 
            
        if curr_node in parent_map and parent_map[curr_node] not in visited:  ## parent_map[curr_node]this will give the parent node of current node upward traversal. 
            parent = parent_map[curr_node]

            visited.add(parent)
            q.append((parent, dist+1))

    
    return result
    

my_tree = TreeNode(10)
my_tree.left = TreeNode(20)
my_tree.right = TreeNode(30)
my_tree.left.left = TreeNode(15)
my_tree.left.right = TreeNode(23)
my_tree.left.left.left = TreeNode(18)
my_tree.left.left.left.left = TreeNode(28)
my_tree.left.left.left.right = TreeNode(25)
my_tree.right.left = TreeNode(33)
my_tree.right.right = TreeNode(35)

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

#my_work = Solution
#print(f'{my_work.distancek(my_tree, my_tree.left.left, 2)}')

print(f'{distancek(my_tree, my_tree.left.left, 2)}')

print(distancek(root, root.left, 2))