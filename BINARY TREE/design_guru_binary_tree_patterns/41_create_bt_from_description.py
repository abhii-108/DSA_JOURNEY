# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.


# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]

from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes =  {}
        children = set()

        for par, child, is_left in descriptions:
            children.add(child)
            if par not in nodes:
                nodes[par] = TreeNode(par)
            
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if is_left:
                nodes[par].left = nodes[child]
            else:
                nodes[par].right = nodes[child]
            

        for p, c, l in descriptions:

            if p not in children:
                return nodes[p]




def preorder(root):
    if root is None:
        #print("N ", end="")
        return

    print(f'{root.val} ', end="")

    preorder(root.left)
    preorder(root.right)


descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
tree_from_desc = Solution()
tree = tree_from_desc.createBinaryTree(descriptions)


preorder(tree)

# arr2 = ser_der.serialize(root2)
# res2 = ser_der.deserialize(arr2)

# preorder(res2)