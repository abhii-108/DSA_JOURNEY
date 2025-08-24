#Given a Binary Tree, the task is to print the left view of the Binary Tree. The left view of a Binary Tree is a set of leftmost nodes for every level.

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


### SHow all the node value if we are observing tree from it's left side 
        
def left_view(root):
    #base case 
    if not root:
        return None 
    
    q = deque([root])

    res_left = []

    while q:
        ## initalize value of left first node to null 
        final_left_val = None 
        queue_len = len(q)

        for _ in range(queue_len):

            node = q.popleft()
            ## we need only the left node so the first node which is pop is same level we need only it's data. rest we can skip. 
            if final_left_val is None:
                final_left_val = node.val
                res_left.append(node.val)

            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return res_left

### SHow all the node value if we are observing tree from it's left side 
   
def right_view(root):
    if not root:
        return
    
    q = deque([root])

    res_right = []


    while q:
        final_right_val = None 
        queue_len = len(q)

        for _ in range(queue_len):

            node = q.popleft()

            final_right_val = node.val 

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
        
        res_right.append(final_right_val)
    
    return res_right



def top_view(root):
    if not root:
        return []
    
    q = deque([(root,0)])  # adding root , horizontal level (from top range will be from - to + )
    # for left side we have to subtract the value, for right side we have to do addition 

    top_res = {}
    min_range = 0 
    max_range = 0  
    while q:

        len_q = len(q)
        final_top_val = None 

        for x in range(len_q):
            
            node, h_level = q.popleft()
            min_range = min(min_range, h_level)
            max_range = max(max_range, h_level)

            if h_level not in top_res:
                top_res[h_level] = node.val 
            
            if node.left:
                q.append((node.left, h_level-1))
            if node.right:
                q.append((node.right, h_level+1))

        
    return [top_res[x] for x in range(min_range, max_range+1)]
        

def bottom_view(root): 
    if not root:
        return

    q = deque([(root, 0)])        # adding root , horizontal level (from top range will be from - to + )

    bottom_res = {}
    min_range = 0 
    max_range = 0 

    while q:

        q_len = len(q)

        node, pos = q.popleft()
        min_range = min(min_range, pos)
        max_range = max(max_range, pos)

        bottom_res[pos] = node.val 

        if node.left:
            q.append((node.left, pos-1))
        if node.right:
            q.append((node.right, pos+1))


    return [bottom_res[x] for x in range(min_range, max_range+1)]









root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)

my_tree = TreeNode(8)
my_tree.left = TreeNode(3)
my_tree.right = TreeNode(10)
my_tree.left.left = TreeNode(1)
my_tree.left.right = TreeNode(6)
my_tree.left.right.left = TreeNode(4)
my_tree.left.right.left.right = TreeNode(7)
my_tree.right.right = TreeNode(14)
my_tree.right.right.left = TreeNode(13)



print(f'{left_view(root3)}')

print(f'{left_view(root1)}')

print(f'{left_view(my_tree)}')

print('------RIght view ---')
print(f'{right_view(root3)}')

print(f'{right_view(root1)}')

print(f'{right_view(my_tree)}')


print('------top_view view ---')
print(f'{top_view(root3)}')

print(f'{top_view(root1)}')

print(f'{top_view(my_tree)}')


print('------bottom_view view ---')
print(f'{bottom_view(root3)}')

print(f'{bottom_view(root1)}')

print(f'{bottom_view(my_tree)}')