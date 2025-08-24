#Maximum Depth of Binary Tree
# Given a binary tree, the task is to find the maximum depth of the tree. 
# The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def height(root):
    #Base condition 
    if not root:
        return 0 
    
    #recursive condition

    left_ht = height(root.left)
    right_ht = height(root.right)

    return max(left_ht,right_ht) + 1
    

if __name__ == "__main__":
  
    # Representation of the input tree:
    #     12
    #    /  \
    #   8   18
    #  / \
    # 5   11
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)
    root.left.right.right = Node(13) ## new node added 

    print(height(root))