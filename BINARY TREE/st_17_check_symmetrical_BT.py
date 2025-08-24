# Symmetric Tree (Mirror Image of itself)

# Given a binary tree, the task is to check whether it is a mirror of itself.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSymmetric(root):

    def dfs(leftsub, rightsub):
        if not leftsub and not rightsub:
            return True 

        if not leftsub or not rightsub:
            return False
        

        return (leftsub.data == rightsub.data 
                and dfs(leftsub.left,rightsub.right)
                and dfs(leftsub.right, rightsub.left)
                )

    op= dfs(root.left, root.right)
    return op
if __name__ == "__main__":
    # Creating a sample symmetric binary tree
    #        1
    #       / \
    #      2   2
    #     / \ / \
    #    3  4 4  3
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    print(isSymmetric(root))