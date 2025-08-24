class BST:
    def __init__(self,key):
        self.key = key  # Node of binary tree contain a key/data and to other parameter which contain detail of left sub tree and right sub tree 
        self.lchild = None # When a node of bst is created value of left sub tree of that node is none. 
        self.rchild = None # Value for right sub tree is kept none when



    ## insert a node in Binary tree     
    def insert(self,data):
        # check if this is the  first node 

        if self.key is None:
            self.key = data
            return 
        
        ## check for duplicate value 
        if self.key == data:
            return 
        
        if self.key > data: # comparing value with root node is less then go to left child node 
            if self.lchild: # check if the lchild is none or not 
                self.lchild.insert(data)
        
            else: # if lchild is none then create a node and attach it to lchild 
                self.lchild = BST(data)

        elif self.key < data: # compare value and if data greatee then root node then search right child 
            if self.rchild:
                self.rchild.insert(data)

            else:
                self.rchild = BST(data)

    ## Search a node in Binary tree 

    def search(self, data):

        if self.key == data:
            print('Node found')
            return 
        
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('Node not found in BST..!')
                return
        
        elif self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('Node not found in BST..!')
                return
    
    ## Different way of traversal in binary tree 
    # pre-Order
    def preorder(self):
        print(f'{self.key}', end=' ')

        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    # In-Order
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(f'{self.key}', end=' ')

        if self.rchild:
            self.rchild.inorder()
    
    # post-Order 
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(f'{self.key}', end=' ')

    
    ## Node deletion from BST 
    
    def delete(self,data):
        if self.key is None:
            print('Tree is Empty..!')
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print('Given Node to delete not found in BST')

        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print('Given Node not found in BST to delete ..!')
        
        else:
            
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp 
            
            if self.rchild is None:
                temp = self.lchild
                self = None 
                return temp 
            
            node = self.rchild

            while node.lchild: # to find the smallest value in the right child subtree there we checking left side of right subtree
                node = node.lchild
            
            self.key = node.key

            self.rchild=self.rchild.delete(node.key)

        return self



                
        



my_tree = BST(20)     

for x in [15,10,5,3,12,14,25,35,30,50,90,45,75,80]:
    my_tree.insert(x)

my_tree.search(12)
my_tree.search(35)
my_tree.search(33)
my_tree.preorder()
print('-------In order ----------',end='\n')
my_tree.inorder()
print('-------post order ----------',end='\n')
my_tree.postorder()





#######################################################################################################################

# A Binary Search Tree (BST) is a node-based binary tree data structure which has the following properties:
# 1. The left subtree of a node contains only nodes with keys lesser than the node’s key.
# 2. The right subtree of a node contains only nodes with keys greater than the node’s key.
# 3. The left and right subtree each must also be a binary search tree.
# 4. There must be no duplicate nodes.

class BST:
    def __init__(self, key):
        # Each node in the BST has three attributes:
        self.key = key      # The value/data of the node.
        self.lchild = None  # A reference to the left child node (initially None).
        self.rchild = None  # A reference to the right child node (initially None).

    ## Insert a node in the Binary Search Tree
    def insert(self, data):
        # Hint: This method recursively finds the correct position to insert the new data.

        # If the tree is empty, the new data becomes the root.
        if self.key is None:
            self.key = data
            return

        # If the data is the same as the current node's key, we do nothing (no duplicates allowed).
        if self.key == data:
            return

        # If the data to insert is less than the current node's key, go to the left subtree.
        if self.key > data:
            # If a left child exists, recursively call insert on it.
            if self.lchild:
                self.lchild.insert(data)
            # If no left child exists, create a new BST node and attach it.
            else:
                self.lchild = BST(data)
        # If the data to insert is greater than the current node's key, go to the right subtree.
        else:
            # If a right child exists, recursively call insert on it.
            if self.rchild:
                self.rchild.insert(data)
            # If no right child exists, create a new BST node and attach it.
            else:
                self.rchild = BST(data)

    ## Search for a node in the Binary Search Tree
    def search(self, data):
        # Hint: This method returns True if the node is found, otherwise False.

        # If the current node's key matches the data, we've found it.
        if self.key == data:
            return True

        # If the data is smaller, search in the left subtree.
        if self.key > data:
            # If a left child exists, continue the search there. Otherwise, it's not in the tree.
            if self.lchild:
                return self.lchild.search(data)
            else:
                return False
        # If the data is larger, search in the right subtree.
        else:
            # If a right child exists, continue the search there. Otherwise, it's not in the tree.
            if self.rchild:
                return self.rchild.search(data)
            else:
                return False

    ## Tree Traversal Methods
    # Hint: Traversal is a process to visit all the nodes of a tree.

    # Pre-order Traversal: Root -> Left -> Right
    def preorder(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    # In-order Traversal: Left -> Root -> Right
    # Hint: For a BST, in-order traversal visits nodes in ascending order.
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=' ')
        if self.rchild:
            self.rchild.inorder()

    # Post-order Traversal: Left -> Right -> Root
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=' ')


    ## Node Deletion from BST
    def delete(self, data, curr_root_key):
        # Hint: This is the most complex operation. It handles three cases for the node to be deleted:
        # 1. The node is a leaf (no children).
        # 2. The node has one child.
        # 3. The node has two children.
        
        if self.key is None:
            print('Tree is Empty!')
            return None

        # Recursively find the node to delete. The return value of the recursive call
        # updates the parent's child link (lchild or rchild).
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr_root_key)
            else:
                print('Given Node is not present in the tree')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr_root_key)
            else:
                print('Given Node is not present in the tree')
        else: # We found the node to delete!
            # Case 1: Node has 0 or 1 child.
            if self.lchild is None:
                temp = self.rchild
                # If we are deleting the root node with one child, we can't just return.
                # The root object itself needs its properties changed.
                if self.key == curr_root_key:
                    # If the root is deleted, we need to handle its replacement carefully.
                    # This case becomes tricky. A better design is to have a separate BST manager class.
                    # For this implementation, we will assume deletion logic is mainly for non-root nodes
                    # or requires reassigning the root variable outside the class.
                    # For simplicity, let's just return the new root.
                    return temp
                self = None # This node is now unlinked.
                return temp # The right child (or None) is returned to be linked to the parent.
            elif self.rchild is None:
                temp = self.lchild
                if self.key == curr_root_key:
                    return temp
                self = None
                return temp # The left child is returned to be linked to the parent.

            # Case 3: Node has two children.
            # We find the inorder successor (smallest node in the right subtree).
            node = self.rchild
            while node.lchild:
                node = node.lchild
            
            # Copy the key of the inorder successor to this node.
            self.key = node.key
            # Recursively delete the inorder successor from the right subtree.
            self.rchild = self.rchild.delete(node.key, curr_root_key)
            
        return self
    

# Helper function to print a visual separator
def show_section(title):
    print("\n" + "="*20)
    print(f" {title}")
    print("="*20)

# --- Test Case 1: Tree Creation & Traversal ---
show_section("1. Tree Creation")
root = BST(10) # Create a root node
# Insert a list of numbers
list1 = [5, 20, 3, 7, 15, 30]
for num in list1:
    root.insert(num)

print("Pre-order Traversal:", end=" ")
root.preorder() # Expected: 10 5 3 7 20 15 30
print("\nIn-order Traversal (sorted):", end=" ")
root.inorder() # Expected: 3 5 7 10 15 20 30
print("\nPost-order Traversal:", end=" ")
root.postorder() # Expected: 3 7 5 15 30 20 10

# --- Test Case 2: Searching ---
show_section("2. Searching")
print(f"Is 7 in the tree? {root.search(7)}")   # Expected: True
print(f"Is 99 in the tree? {root.search(99)}") # Expected: False

# --- Test Case 3: Deletion Scenarios ---
show_section("3. Deletion")

# Edge Case A: Delete a leaf node (e.g., 3)
print("\nDeleting a leaf node (3)...")
root.delete(3, root.key)
print("In-order after deleting 3:", end=" ")
root.inorder() # Expected: 5 7 10 15 20 30

# Edge Case B: Delete a node with one child (e.g., 15, after we add 18)
root.insert(18)
print("\n\nIn-order before deleting 15:", end=" ")
root.inorder()
print("\nDeleting node 15 (has one child, 18)...")
root.delete(15, root.key)
print("In-order after deleting 15:", end=" ")
root.inorder() # Expected: 5 7 10 18 20 30

# Edge Case C: Delete a node with two children (e.g., 20)
print("\n\nDeleting node 20 (has two children)...")
root.delete(20, root.key)
print("In-order after deleting 20:", end=" ")
root.inorder() # Expected: 5 7 10 18 30 (30 is the successor of 20)

# Edge Case D: Delete the root node
show_section("4. Deleting the Root")
print("Current root key:", root.key) # Expected: 10
print("Deleting root node (10)...")
# When deleting the root, you must re-assign the root variable
root = root.delete(10, root.key)
print("New root key:", root.key) # Expected: 18 (inorder successor of 10)
print("In-order after deleting old root:", end=" ")
root.inorder() # Expected: 5 7 18 30

# Edge Case E: Deleting from an empty/non-existent tree
show_section("5. Edge Cases")
empty_tree = BST(None)
empty_tree.delete(10, None) # Expected: Tree is Empty!

print("\nAttempting to delete a non-existent node (99)...")
root.delete(99, root.key) # Expected: Given Node is not present...
print("In-order remains unchanged:", end=" ")
root.inorder()