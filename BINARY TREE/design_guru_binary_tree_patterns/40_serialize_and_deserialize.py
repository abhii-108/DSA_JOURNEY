# Serialize and Deserialize a Binary Tree

# Serialization is performed to store a tree in an array so that it can be later restored and deserialization is reading the tree back from the array.

# Given a binary tree, the task is to complete the functions:

# serialize(): stores the tree into an array arr[] and returns the array.
# deSerialize(): deserializes the array to the tree and returns the root of the tree.

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def serialize(self, root):
        res = [] # initially store result in an array 

        def dfs(node):

            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return ",".join(res)

    
    def deserialize(self, data):
        val = data.split(',') # split the array 
        self.i = 0 # Global index position

        def dfs():
            
            if val[self.i] == 'N':
                self.i += 1 
                return None
            
            node = TreeNode(int(val[self.i]))

            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node 
        
        return dfs()

def printLevelOrder(root):
    if root is None:
        print("N ", end="")
        return

    queue = deque([root])
    non_null = 1

    while queue and non_null > 0:
        curr = queue.popleft()

        if curr is None:
            print("N ", end="")
            continue
        non_null -= 1

        print(curr.val, end=" ")
        queue.append(curr.left)
        queue.append(curr.right)
        if curr.left:
            non_null += 1
        if curr.right:
            non_null += 1

def preorder(root):
    if root is None:
        print("N ", end="")
        return

    print(f'{root.val} ', end="")

    preorder(root.left)
    preorder(root.right)



root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(8)




ser_der = Solution()


# Create a hard coded tree
#       10
#     /    \
#    20    30
#  /   \
# 40  60
root2 = TreeNode(10)        
root2.left = TreeNode(20)        
root2.right = TreeNode(30)       
root2.left.left = TreeNode(40)
root2.left.right = TreeNode(60) 
root2.right.right = TreeNode(70)       

arr = ser_der.serialize(root)
res = ser_der.deserialize(arr)

preorder(res)
print('---------------')
arr2 = ser_der.serialize(root2)
res2 = ser_der.deserialize(arr2)

preorder(res2)