# Deepest Leaves Sum (medium)

# Given a root node of the binary tree, return the sum of all values located at the deepest leaves of a binary tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Method to collect leaf nodes using DFS

    def deepest_leaf_sum(self, root):
        self.curr_level=0
        self.sum = 0

   

        def findLeavesDFS(node, level):
            if not node:
                return 

            if not node.left and not node.right :

                # if level > self.curr_level:
                #     self.curr_level = level
                #     self.sum = node.val
                
                # elif level == self.curr_level:
                #     self.sum += node.val

                ############## OR #######################
                if self.curr_level == 0: # this is first time we got leaf node we will set its value 
                    self.curr_level = level 
                    self.sum = node.val
                elif self.curr_level != level and self.curr_level < level:
                        self.curr_level = level
                        self.sum = node.val 
                else:
                    self.sum += node.val


                
            
            findLeavesDFS(node.left, level+1) 
 
            findLeavesDFS(node.right, level+1)
        
        findLeavesDFS(root, 0)  

        return self.sum 
       
    

        

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)

root2 = TreeNode(0)
root2.left = TreeNode(1)
root2.right = TreeNode(5)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(20)

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.right = TreeNode(1) 
root.right.left = TreeNode(1) 
root.right.right = TreeNode(1)



one = Solution()
print(one.deepest_leaf_sum(root1))

two = Solution()
print(two.deepest_leaf_sum(root2))
