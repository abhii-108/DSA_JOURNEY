#Input: Doubly Linked List = 1 <-> 2 <-> 3 -> NULL 
# Output: Reversed Doubly Linked List = 3 <-> 2 <-> 1 -> NULL

# Input: Doubly Linked List = 1 ->NULL 
# Output: Reversed Doubly Linked List = 1 ->NULL 


class Node:
    def __init__(self,data):
        self.data = data 
        self.nref = None 
        self.pref = None 

def reverse(head):

    if head is None:
        return -1 
    
    old = None
    curr = head 
    

    while curr is not None:
        next = curr.nref 
        curr.nref = old 
        curr.pref = next 
        old = curr 
        curr= next 
        
    
    return old 



def print_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.nref
    print()

if __name__ == "__main__":
  
    # Create a hard-coded doubly linked list:
    # 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    head.nref = Node(2)
    head.nref.pref = head
    head.nref.nref = Node(3)
    head.nref.nref.pref = head.nref
    head.nref.nref.nref = Node(4)
    head.nref.nref.nref.pref = head.nref.nref

    print("Original Linked list")
    print_list(head)
    head = reverse(head)
    print("\nReversed Linked list")
    print_list(head)