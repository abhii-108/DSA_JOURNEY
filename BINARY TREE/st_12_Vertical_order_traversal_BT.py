
from collections import deque, defaultdict
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def verticalOrder(root):

    if not root:
        return []
    
    queue = deque([(root,0)]) 

    min_col = 0 
    max_col = 0 

    cols = defaultdict(list)

    while queue:

        node, col = queue.popleft()

        min_col = min(min_col,col)
        max_col = max(max_col,col)

        cols[col].append(node.data)

        if node.left:
            queue.append((node.left, col - 1))

        if node.right:
            queue.append((node.right, col + 1))

    
    return [ cols[c] for c in range(min_col, max_col+1)]





if __name__ == "__main__":
    
    # create hard coded tree
    #       26
    #      /  \
    #     10   3
    #    / \  / \
    #   4  6 5   3
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(3)

    print(verticalOrder(root))