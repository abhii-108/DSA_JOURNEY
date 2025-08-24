#Level Order Traversal of a Binary Tree
#Level order traversal visits nodes level-by-level from left to right. Think of it as a Breadth-First Search (BFS) where we process nodes in the order they appear at each depth.

# Approach:
# Use a Queue:

# Start with the root node in a queue.

# Process nodes level-by-level: For each node, add its children to the queue.

# Track Levels:

# For each level, determine the number of nodes (queue size).

# Process all nodes at that level in a single iteration.

# Time Complexity: O(N) → Each node visited exactly once
# Space Complexity: O(N) → Queue stores all nodes at the widest level

from collections import deque
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    
def right_view(root):

    if not root:
        return []
    

    result = []
    queue = deque([root])


    while queue:

        level_size = len(queue)
        current_level = None


        for _ in range(level_size):
            node = queue.popleft()
            
            current_level=node.data

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def left_view(root):

    if not root:
        return []
    

    result = []
    queue = deque([root])


    while queue:

        level_size = len(queue)
        current_level = None


        for _ in range(level_size):
            node = queue.popleft()
            
            # only change for left view
            if current_level is None:
                current_level=node.data
                print(current_level)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

            # current_level=node.data
            # if node.right:
            #     queue.append(node.right)
            
            # if node.left:
            #     queue.append(node.left)

        result.append(current_level)

    return result


if __name__ == "__main__":
    
    # create hard coded tree
    #       26
    #      /  \
    #     10   3
    #    / \    \
    #   4  6     3
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(3)
    root.left.right.left = Node(16)


    print(right_view(root))
    print(left_view(root))
