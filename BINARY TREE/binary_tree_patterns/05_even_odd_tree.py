# A binary tree is named Even-Odd if it meets the following conditions:

# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

# Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# Output: true
# Explanation: The node values on each level are:
# Level 0: [1]
# Level 1: [10,4]
# Level 2: [3,7,9]
# Level 3: [12,8,6,2]
# Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

from collections import deque

class TreeNode:
    def __init__(self,key):     
        self.key = key 
        self.lchild = None
        self.rchild = None 

def even_odd(node):

    even = True

    q = deque([node])

    while q:

        if even:
            prev = float('-inf')
        else:
            prev = float('inf')

        
        q_len = len(q)

        for _ in range(q_len):

            node = q.popleft()

            if even: 
                if node.key % 2 == 0 or node.key <= prev:  # to check if value is even or less then prev 
                    return False
            else:
                if node.key % 2 == 1 or node.key >= prev: # to check if value is odd or greater then prev
                    return False 
            
            if node.lchild:
                q.append(node.lchild)
            if node.rchild:
                q.append(node.rchild)


            prev = node.key 
        even = not even 

    return True



my_tree = TreeNode(11)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(12)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(45)


print(even_odd(my_tree))