# ZigZag Tree Traversal

# Given a binary tree, the task is to find the zigzag level order traversal of the tree. 
# In zig zag traversal starting from the first level go from left to right for odd-numbered levels and right to left for even-numbered levels.


from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def zig_zag(root):
    if not root:
        return []

    queue = deque([root])

    #flag 
    lefttoright = True
    
    result = []

    while queue:
        curr_res = deque() ## for saving the level op so that we can use appendleft Use a deque for curr_res as well for O(1) appends to both ends
        queue_len = len(queue)

        for _ in range(queue_len):

            curr_node = queue.popleft()

            if lefttoright:
                # Add to the right for left-to-right levels
                curr_res.append(curr_node.data)
            else:
                # Add to the left for right-to-left levels
                curr_res.appendleft(curr_node.data)

        
            # Enqueue children for the next level
            if curr_node.left:
                queue.append(curr_node.left)
            
            if curr_node.right:
                queue.append(curr_node.right)

        # Convert deque to list and append to result
        result.append(list(curr_res)) ## to convert deque into list 

        
        # if lefttoright == False:
        #     curr_res.reverse()
        #     result.append(curr_res)
            
        # else:
        #     result.append(curr_res)
        
        lefttoright = not lefttoright
    
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
    root.right.right = Node(3)

    print(zig_zag(root))