#if given Two Trees are Identical or not

# The idea is to compare the root nodes' data and recursively verify that their left and right subtrees are identical. 
# Both trees must have the same structure and data at each corresponding node.

# If both trees are empty then return 1 (Base case)
# Else, If both trees are non-empty
    # Check data of the root nodes (r1->data == r2->data)
    # Check left subtrees recursively
    # Check right subtrees recursively
    # If the above three statements are true then return 1
# Else return 0 (one is empty and the other is not)

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isIdentical(root1, root2):

    #base conditions 
    if root1 is None and root2 is None:
        return True 
    
    if root1 is None or root2 is None:
        return False
    
    left = isIdentical(root1.left, root2.left)
    right = isIdentical(root1.right, root2.right)

    val_check = root1.data == root2.data

    if (left and right and val_check):
        return True 
    else:
        return False

if __name__ == "__main__":

    # Representation of input binary tree 1
    #        1
    #       / \
    #      2   3
    #     /
    #    4
    r1 = Node(1)
    r1.left = Node(2)
    r1.right = Node(3)
    r1.left.left = Node(4)

    # Representation of input binary tree 2
    #        1
    #       / \
    #      2   3
    #     /
    #    4
    r2 = Node(1)
    r2.left = Node(2)
    r2.right = Node(3)
    r2.left.left = Node(4)
    r2.left.left.right = Node(10)

    if isIdentical(r1, r2):
        print("Yes")
    else:
        print("No")