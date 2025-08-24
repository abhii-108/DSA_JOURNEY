#Boundary traversal involves visiting the nodes along the boundary of the tree in a specific order:

# Left Boundary (excluding leaf nodes).

# Leaf Nodes (visited from left to right).

# Right Boundary (excluding leaf nodes, visited from right to left).


# To perform a boundary traversal, we'll implement three separate functions that will collect the nodes for each part of the boundary, and then combine them in the correct order.

# print_left_boundary(node, result): Traverses down the left side of the tree. We'll add nodes to our result list as we go, but we need to stop before adding leaf nodes to avoid duplicates since leaves are handled separately.

# print_leaves(node, result): Performs a standard in-order traversal (or any traversal that visits leaves) and adds all leaf nodes to the result list.

# print_right_boundary(node, result): Traverses down the right side of the tree. Similar to the left boundary, we'll add nodes, but in reverse order. This means we'll typically append them after the recursive call returns, ensuring a bottom-up (right-to-left) order. We'll also exclude leaf nodes.

# The main boundary_traversal(root) function will orchestrate these calls.

import collections

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def print_left_boundary(node,result):
    if not node:
        return
    # If it's a non-leaf node, add its data
    # This ensures we don't add leaf nodes as part of the left boundary
    if node.left or node.right:
        result.append(node.data)
        print(result)

    # Traverse left if possible
    if node.left:
        print_left_boundary(node.left, result)

    # If no left child, go to the right child (e.g., if left branch ends, but right continues the boundary)
    elif node.right:
        print_left_boundary(node.right, result)

def print_leaves(node, result):

    if not node:
        return 
    
    # If it's a leaf node, add its data
    if not node.left and not node.right:
        result.append(node.data) 
        # No need to go further for a leaf
        return

    # Recurse for left and right children
    print_leaves(node.left, result)
    print_leaves(node.right, result)


def print_right_boundary(node, result):

    if not node:
        return 
    
    # Traverse right if possible
    if node.right:
        print_right_boundary(node.right, result)

    # If no right child, go to the left child (e.g., if right branch ends, but left continues the boundary)
    elif node.left:
        print_right_boundary(node.left, result)

    # Add node data after recursive calls
    # Exclude leaf nodes as they are handled by print_leaves
    if node.left or node.right:
        result.append(node.data)


def boundary_traversal(root):
    
    if not root:
        return []
    
    result = []

    if root.left or root.right:
        result.append(root.data)

    print_left_boundary(root.left, result)

    print_leaves(root, result)

    print_right_boundary(root.right, result)

    return result


if __name__ == "__main__":
    
    # create hard coded tree
    #       26
    #      /  \
    #     10   22
    #    / \  / \
    #   4  6  5  13
    #      /       \ 
    #     16        30
    root = Node(26)
    root.left = Node(10)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(13)
    root.left.right.left = Node(16)
    root.right.right.right = Node(30)


    print(boundary_traversal(root))
    # print(left_view(root))