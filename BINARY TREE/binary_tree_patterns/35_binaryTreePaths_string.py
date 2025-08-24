#Binary Tree Paths (easy)

#Given the root node of a binary tree, return all unique paths from the root node to the leaf node in any order.


# Input: root = [1,2,3,null,null,4,5]

# Expected Output: ["1->2", "1->3->4", "1->3->5"]
# Justification: The binary tree has one root-to-leaf path for the left child (1->2) and two for the right child, branching into 4 and 5 respectively.

# Input: root = [5,3,6,2,4,null,null,1]

# Expected Output: ["5->3->2->1", "5->3->4", "5->6"]
# Justification: There are three paths leading to leaf nodes: one through the left subtree down to 1, another through the left subtree to 4, and one path through the right subtree to 6.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []
        #self.curr_path=''
         

    def binaryTreePath(self,root):
        self.get_binary_tree_path(root, "")
        return self.res 

    def get_binary_tree_path(self, node, curr_path):

        if not node:
            return
        
        curr_path += str(node.val)

        if not node.left and not node.right:
            self.res.append(curr_path)
            return 
        
        curr_path += '->'

        self.get_binary_tree_path(node.left, curr_path)
        self.get_binary_tree_path(node.right, curr_path)


# Example usage
root = TreeNode(8)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right = TreeNode(9)

solution = Solution()
print(solution.binaryTreePath(root))  # Output: 18

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)
solution2 = Solution()
print("Example 2:", solution2.binaryTreePath(root2))

root3 = TreeNode(2)
root3.right = TreeNode(3)
root3.right.right = TreeNode(4)
root3.right.right.right = TreeNode(5)
solution3 = Solution()
print("Example 3:", solution3.binaryTreePath(root3))

