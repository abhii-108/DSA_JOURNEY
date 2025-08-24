#Check if leaf traversal of two Binary Trees is same

#Leaf traversal is the sequence of leaves traversed from left to right. The problem is to check if the leaf traversals of two given Binary Trees are same or not.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Method to collect leaf nodes using DFS

    def isSame(self, root1, root2):
        res1 = []
        res2 = []

   

        def findLeavesDFS(node, list):
            if not node:
                return

            if not node.left and not node.right :
                list.append(node.val)
                return 
            
            findLeavesDFS(node.left, list )
            findLeavesDFS(node.right, list )
        
        findLeavesDFS(root1, res1)  
        findLeavesDFS(root2, res2)  

        return res1 == res2
       
    

        

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




one = Solution()
if (one.isSame(root1, root2)):
    print("Same")
else:
    print("Not Same")