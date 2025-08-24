## We need to find diameter of binary tree 

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def diameter(root):
    max_diameter = 0 

    def height(node):
        nonlocal max_diameter

        if not node:
            return 0 
        
        left_ht = height(node.left)
        Right_ht = height(node.right)

        current_diameter = left_ht + Right_ht
        max_diameter = max(max_diameter, current_diameter)

        return max(left_ht,Right_ht) + 1


    print(f'height of BT is {height(root)}')
    return max_diameter



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

    print(f'diameter of BT IS {diameter(root)}')