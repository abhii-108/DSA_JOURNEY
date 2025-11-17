## Give a BT, return sum of all node in BT usinf BFS technique 


from collections import deque 

class TreeNode:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None 

def sum_all_node(root):

    if not root:
        return 0 
    
    all_node_sum = 0 

    q = deque([root])

    while q :

        curr_node = q.popleft()

        all_node_sum += curr_node.key 


        if curr_node.lchild:
            q.append(curr_node.lchild)

        if curr_node.rchild:
            q.append(curr_node.rchild)

    return all_node_sum


################################# SUM NODE With EVEN GrandaParents (BFS) ########################
# Given the root of a binary tree, return the total sum of the values of all nodes that have a grandparent with an even number. If no such nodes exist, return 0.

# A grandparent of a node is defined as the parent of its parent, if both exist.

# Example 1:

# Input: root = [4, 2, 6, 3, 5, null, 8]
# Expected Output: 16
# Justification: Node values 3, 5, and 8 have 4 as their grandparent. Since 4 is even, their sum is 3 + 5 + 8 = 16
def sum_even_grandparent(root):

    if not root:
        return 0
    
    total_sum = 0 

    even_queue = deque([(root, None, None)]) ## root_node, parent_node, grandparentNode 

    while even_queue:

        curr_node, parent, grandparent = even_queue.popleft()

        if grandparent and grandparent.key % 2 == 0:
            total_sum += curr_node.key

        if curr_node.lchild:
            even_queue.append((curr_node.lchild, curr_node, parent))

        if curr_node.rchild:
            even_queue.append((curr_node.rchild, curr_node, parent))

    return total_sum


################################# SUM NODE With EVEN GrandaParents (DFS) ########################

def dfs(curr_node, parent, grandparent):

    if not curr_node:
        return 0
    total_sum = 0 
    if grandparent and grandparent.key % 2 == 0 :
        total_sum += curr_node.key 
    
    total_sum += dfs(curr_node.lchild, curr_node, parent)
    total_sum += dfs(curr_node.rchild, curr_node, parent)

    return total_sum

def sum_even_grandparent_dfs(root):
    if not root:
        return 0 
        

    return dfs (root, None, None)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def sumEvenGrandparent(self, root: TreeNode) -> int:
#         def dfs(current, parent, grandparent):
#             if not current:
#                 return 0
#             total = 0
#             if grandparent and grandparent.val % 2 == 0:
#                 total += current.val
#             total += dfs(current.left, current, parent)
#             total += dfs(current.right, current, parent)
#             return total
        
#         return dfs(root, None, None)


my_tree = TreeNode(10)

my_tree.lchild = TreeNode(20)
my_tree.rchild = TreeNode(30)
my_tree.lchild.lchild = TreeNode(15)
my_tree.lchild.rchild = TreeNode(23)
my_tree.lchild.lchild.lchild = TreeNode(18)
my_tree.lchild.lchild.lchild.rchild = TreeNode(25)
my_tree.rchild.lchild = TreeNode(33)
my_tree.rchild.rchild = TreeNode(35)



print(f' finding sum of binary tree  {sum_all_node(my_tree)}')


print(f' finding even node grandparent sum of binary tree  {sum_even_grandparent(my_tree)}')


print(f' finding even node grandparent sum of binary tree  DFS {sum_even_grandparent_dfs(my_tree)}')