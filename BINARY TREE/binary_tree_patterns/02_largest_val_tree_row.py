#Find Largest Value in Each Tree Row (medium)
# Given the root of a binary tree, return an array containing the largest value in each row of the tree (0-indexed).
# Example 1
# Input: root = [1, 2, 3, 4, 5, null, 6]
# Expected Output: [1, 3, 6]
# Justification:
# The first row contains 1. The largest value is 1.
# The second row has 2 and 3, and the largest is 3.
# The third row has 4, 5, and 6, and the largest is 6.

# Example 2
# Input: root = [7, 4, 8, 2, 5, null, 9, null, 3]
# Expected Output: [7, 8, 9, 3]

# Justification:
# The first row contains 7, and the largest value is 7.
# The second row has 4 and 8, and the largest is 8.
# The third row has 2, 5, and 9, and the largest is 9.
# The fourth row has 3, and the largest is 3.

from collections import deque 
class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 


def large_value_tree_row(root):
    
    if not root:
        return []
    
    q = deque([root])

    res = []

    while q:
        q_len = len(q)
        max_row_val = float('-inf')  # or q[0].key

        for _ in range(q_len):

            node = q.popleft()
            max_row_val = max(max_row_val, node.key)

            if node.lchild:
                q.append(node.lchild)
            
            if node.rchild:
                q.append(node.rchild)

        res.append(max_row_val)

    return res 
my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)

#  # Example 2
# root2 = TreeNode(7)
# root2.lchild = TreeNode(4)
# root2.rchild = TreeNode(8)
# root2.lchild.lchild = TreeNode(2)
# root2.lchild.rchild = TreeNode(5)
# root2.rchild.rchild = TreeNode(9)
# root2.lchild.lchild.rchild = TreeNode(3)

# output2 = large_value_tree_row(root2)
# print("Example 2 Output:", output2)  # Expected Output: [7, 8, 9, 3]


print(large_value_tree_row(my_tree))