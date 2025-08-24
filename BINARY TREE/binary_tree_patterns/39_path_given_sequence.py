#Check if there is a root to leaf path with given sequence

#Given a binary tree and an array, the task is to find if the given array sequence is present as a root-to-leaf path in given tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def check_path(node, arr, index):

    # check if node is empty and also check if this node depth is greater then size(len) of arrary
    if not node or index >= len(arr):
        return False 
    
    ## Now check value 

    if node.val != arr[index]:
        return False 
    
    if not node.left and not node.right and (index == len(arr)-1) :
        return True 
    

    return check_path(node.left, arr, index+1) or check_path(node.right, arr, index+1)
        



root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(8)



#print(solution.maxPathSum(root))  # Output: 408

arr = [5, 2, 4, 8]

if check_path(root, arr, 0):
    print("True")
else:
    print("False")