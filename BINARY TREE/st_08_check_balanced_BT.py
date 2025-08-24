#Balanced Binary Tree or Not

#Given a binary tree, determine if it is height-balanced. 
#A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree.

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isBalanced(root):

    def checkbalance(node):
        # Base condition 
        if not node :
            return 0 

        left_ht = checkbalance(node.left)
        right_ht = checkbalance(node.right)

        if left_ht == -1 or right_ht == -1 or (abs(left_ht - right_ht) > 1):
            return -1 
        

        return max(left_ht,right_ht) + 1

    return checkbalance(root) > 0




################ Variations #######################
    

def isBalanced2(root):

    def dfs(node):
        #base condition 
        
        if not node:
            return [True, 0]
        
        left_ht = dfs(node.left)
        right_ht = dfs(node.right)

        balance = (left_ht[0] and right_ht[0]
                   and (abs(left_ht[1] - right_ht[1]) <= 1))
        
        return [balance, max(left_ht[1],right_ht[1]) + 1]
    
    return dfs(root)[0]









if __name__ == "__main__":
  
    # Representation of the input tree:
    #     12
    #    /  \
    #   8   18
    #  / \
    # 5   11
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.right.right = Node(28) ## new node added 
    root.right.right.right = Node(38) ## new node added 
    root.left.left = Node(5)
    root.left.right = Node(11)
    root.left.right.right = Node(13) ## new node added 

    print(f'Check if BT is Balanced :- {isBalanced(root)}')

    print(f'Check if BT is Balanced2 :- {isBalanced2(root)}')






