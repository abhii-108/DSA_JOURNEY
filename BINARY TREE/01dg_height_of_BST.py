# Solution: Maximum Depth (or Height) of Binary Tree
# Given a root node of the binary tree, return the depth (or height) of a binary tree.

# The Depth of the binary tree refers to the number of nodes along the longest path from the root node to the farthest leaf node. If the tree is empty, the depth is 0.

class TreeNode:
    def __init__(self,key=None,lchild=None,rchild=None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild 

class Solution:
    def inorder(self,root):
        if root is None:
            return 
        
        if root.lchild:
            self.inorder(root.lchild)
        print(f'{root.key} ', end=" ")
        if root.rchild:
            self.inorder(root.rchild)

    def max_depth(self,root):
        if root is None:
            return -1
        
        else:
            left_height = self.max_depth(root.lchild)
            right_height = self.max_depth(root.rchild)

            return 1+max(left_height, right_height)



if __name__ == "__main__":
    solver = Solution()

    # Example 1
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    solver.inorder(root1)
    print(end='\n')
    print(f'-------height to tree------')
    print(solver.max_depth(root1))




###############################################################
    
#     The Golden Rule: Your Mental Checklist
# Base Case: What do I do at a None node? (This stops the recursion).
# Divide & Conquer (Recurse): What information do I need from my pure-left and pure-right subtrees? I'll assume my function magically solves it for them.
# left_result = solve(node.left)
# right_result = solve(node.right)
# Combine: Now that I have the results from my children, how do I solve the problem for the current node?
# Question 1: Diameter of a Binary Tree
# Problem Statement: Find the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Applying the Pattern:
# This is a classic! The trick is realizing that for any node, the longest path (the "diameter") is one of three things:

# The diameter of its left subtree.
# The diameter of its right subtree.
# The path that goes through the current node, which is (height of left subtree) + (height of right subtree).
# Our function needs to return the height of the current subtree, but it also needs to track the maximum diameter found anywhere. We'll use a non-local variable to keep track of the max diameter.

# Base Case: The height of a None node is 0.
# Recurse: Get the height of the left child (left_height) and the right child (right_height).
# Combine:
# Calculate the diameter at the current node: diameter = left_height + right_height.
# Update our global max_diameter if this new diameter is larger.
# Return the height of the tree at the current node, which is 1 + max(left_height, right_height).
# Python Solution:

# Python

def diameterOfBinaryTree(root):
    max_diameter = 0

    def height(node):
        nonlocal max_diameter
        # 1. Base Case
        if not node:
            return 0

        # 2. Recurse
        left_height = height(node.lchild)
        right_height = height(node.rchild)

        # 3. Combine
        # A. Update the max diameter found so far
        current_diameter = left_height + right_height
        max_diameter = max(max_diameter, current_diameter)

        # B. Return the height for the parent node's calculation
        return 1 + max(left_height, right_height)

    height(root)
    return max_diameter

# Question 2: Balanced Binary Tree
# Problem Statement: Determine if a binary tree is "height-balanced" — meaning the depth of the two subtrees of every node never differ by more than 1.

# Applying the Pattern:
# We can adapt our height function. Instead of just returning the height, it can return a special value (like -1) if it discovers an imbalance.

# Base Case: A None node is balanced and has a height of 0.
# Recurse: Get the "heights" from the left and right children.
# Combine:
# Check if either the left or right subtree has already reported an imbalance (returned -1). If so, this tree is also unbalanced. Pass -1 up.
# Check if the heights of the children differ by more than 1. If so, this node is unbalanced. Return -1.
# If all is good, return the actual height: 1 + max(left_height, right_height).
# Python Solution:

# Python

def isBalanced(root):
    def check_balance(node):
        # 1. Base Case
        if not node:
            return 0  # A null tree is balanced with height 0

        # 2. Recurse
        left_height = check_balance(node.lchild)
        right_height = check_balance(node.rchild)

        # 3. Combine (check for imbalances and return height)
        # If a subtree is unbalanced OR the current node is unbalanced
        if left_height == -1 or \
           right_height == -1 or \
           abs(left_height - right_height) > 1:
            return -1  # Signal an imbalance

        # Otherwise, return the actual height
        return 1 + max(left_height, right_height)

    return check_balance(root) > 0
# Question 3: Merge Two Binary Trees
# Problem Statement: Given two binary trees, merge them. The rule is: if two nodes overlap, the new node's value is the sum of their values. Otherwise, the non-null node is used.

# Applying the Pattern:
# The pattern is modified to take two nodes as input.

# Base Case: If one of the nodes is None, there's nothing to merge, so just return the other node.
# Recurse: Recursively merge the left children of both trees. Then merge the right children.
# Combine: Create a new node. Its value is node1.key + node2.key. Its left child is the result of the left-merge, and its right child is the result of the right-merge.
# Python Solution:
# (Assuming you have the BST class from our previous discussion)

# Python

def mergeTrees(t1, t2):
    # 1. Base Case
    if not t1:
        return t2
    if not t2:
        return t1

    # 3. Combine (done before recursion here - a pre-order approach)
    # Create a new node with the summed value
    merged_node = mergeTrees(t1.key + t2.key) ## issue here 

    # 2. Recurse
    # The new node's children are the result of merging the children
    merged_node.lchild = mergeTrees(t1.lchild, t2.lchild)
    merged_node.rchild = mergeTrees(t1.rchild, t2.rchild)

    return merged_node
# Question 4: Symmetric Tree
# Problem Statement: Check if a tree is a mirror image of itself (symmetric around its center).

# Applying the Pattern:
# This is a beautiful twist. You need a helper function that takes two nodes and checks if they are mirrors of each other. You start by calling it with the root's left and right children.

# Base Case:
# If both nodes are None, they are symmetric. return True.
# If one is None but the other isn't, they are not. return False.
# If their values don't match, they are not. return False.
# Recurse: The key insight! To be mirrors, node1's left child must mirror node2's right child, AND node1's right child must mirror node2's left child.
# Combine: Return the logical AND of the two recursive calls.
# Python Solution:

# Python

def isSymmetric(root):
    if not root:
        return True

    def isMirror(node1, node2):
        # 1. Base Case
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.key != node2.key:
            return False

        # 2 & 3. Recurse and Combine
        return isMirror(node1.lchild, node2.rchild) and \
               isMirror(node1.rchild, node2.lchild)

    return isMirror(root.lchild, root.rchild)
# Question 5: Subtree of Another Tree
# Problem Statement: Given two trees, s and t, check if t has the exact same structure and node values as a subtree of s.

# Applying the Pattern:
# This uses two functions and is a great example of combining patterns.

# A helper function isSameTree(s, t) that checks if two trees are identical.
# A main function isSubtree(s, t) that traverses s and, at each node, calls isSameTree to see if that node is the root of a subtree matching t.
# isSubtree(s, t) Pattern:
# Base Case: If s is None, we can't find t. return False.
# Recurse/Combine: The answer is True if (s and t are the same tree) OR (t is a subtree of s's left child) OR (t is a subtree of s's right child).
# Python Solution:

# Python

def isSameTree(s, t):
    if not s and not t:
        return True
    if not s or not t or s.key != t.key:
        return False
    return isSameTree(s.lchild, t.lchild) and isSameTree(s.rchild, t.rchild)

def isSubtree(s, t):
    # Base cases for the main traversal
    if not s:
        return False
    if not t:
        return True # An empty tree is a subtree of any tree

    # Check for a match at the current node, OR...
    if isSameTree(s, t):
        return True

    # ...recurse down to see if it's a subtree of the left OR right children.
    return isSubtree(s.lchild, t) or isSubtree(s.rchild, t)
