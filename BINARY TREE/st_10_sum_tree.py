#given Binary Tree is Sum Tree
#Given a binary tree, the task is to check if it is a Sum Tree. A Sum Tree is a Binary Tree where the value of a node is equal to the sum of the nodes present in its left subtree and right subtree.
#An empty tree is Sum Tree and the sum of an empty tree can be considered as 0. A leaf node is also considered a Sum Tree.

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def is_sum_tree(root):

    #Base conditions 
    if not root:
        return 0 
    
    if root.left is None and root.right is None:
        return root.data 
    
    ls = is_sum_tree(root.left)

    if ls == -1:
        return -1 
    
    rs = is_sum_tree(root.right)

    if rs == -1:
        return -1 
    

    if ls + rs == root.data:
        return ls + rs + root.data 
    else:
        return -1 
    



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

    if is_sum_tree(root) != -1:
        print("True")
    else:
        print("False")