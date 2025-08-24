#Lowest Common Ancestor in Binary Search Tree

# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lowestCommonAncestor(root,p,q):

    curr = root 

    while curr:
        if p > curr.data and q > curr.data:
            curr = curr.right

        elif p < curr.data and q < curr.data:
            curr = curr.left 

        else:
            return curr.data 




if __name__ == "__main__":
    # Creating a sample symmetric binary tree
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(13)
    root.right.right = Node(18)

    op_node = lowestCommonAncestor(root,4,5)
    print(f'LCA is {op_node}')

