# Check if all leaves are at same level

# Given a Binary Tree, check if all leaves are at same level or not. 

# The idea is to first find the level of the leftmost leaf and store it in a variable leafLevel. Then compare level of all other leaves with leafLevel, if same, return true, else return false. We traverse the given Binary Tree in a Preorder fashion. An argument leaflevel is passed to all calls. The value of leafLevel is initialized as 0 to indicate that the first leaf is not yet seen yet. The value is updated when we find first leaf. Level of subsequent leaves (in preorder) is compared with leafLevel.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Method to collect leaf nodes using DFS

    def isSame(self, root):
        self.curr_level=0

   

        def findLeavesDFS(node, level):
            if not node:
                return True  ## This is important here ..... !! 

            if not node.left and not node.right :
                if self.curr_level == 0: # this is first time we got leaf node we will set its value 
                    self.curr_level = level 
                #print(f'{self.curr_level} --> {level}')
                return self.curr_level == level
                
            
            return (findLeavesDFS(node.left, level+1 ) and  findLeavesDFS(node.right, level+1 ))
        
        return findLeavesDFS(root1, 0)   
       
    

        

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
root2.right.right = TreeNode(7)

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.right = TreeNode(4) 
root.right.left = TreeNode(5) 
root.right.right = TreeNode(6)



one = Solution()
if (one.isSame(root1)):
    print("Leave at same level")
else:
    print("Leave Not at Same Level")


if (one.isSame(root)):
    print("Leave at same level")
else:
    print("Leave Not at Same Level")