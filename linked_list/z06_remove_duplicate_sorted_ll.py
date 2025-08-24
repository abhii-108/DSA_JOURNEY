# Detect Loop or Cycle in Linked List

# Input: head: 1 -> 3 -> 4 -> 3
# Output: true
# Input: head: 1 -> 8 -> 3 -> 4 -> NULL 
# Output: false

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 


def removeDuplicates(head):
    #code here
    
    if head is None:
        return None
    
    if head.next is None:
        return head 
    
    ### Apporach using single pointer 
    # curr = head 
    
    # while curr.next:
        
    #     if curr.data == curr.next.data:
    #         print('yes')
    #         curr.next = curr.next.next
    #     else:
    #         curr = curr.next 
                
    ## approach using 2 point 

    slow_ptr = head 
    fast_ptr = head.next 

    while fast_ptr is not None:
        if slow_ptr.data == fast_ptr.data:
            #print('here')
            slow_ptr.next = fast_ptr.next
            fast_ptr = fast_ptr.next
        else:
            slow_ptr = slow_ptr.next 
            fast_ptr = fast_ptr.next 

    return head 
def print_list(node):
    while node is not None:
        print(node.data, end="-->")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(5)
  
    # Create a loop
    #head.next.next.next = head.next
    #print(removeDuplicates(head))
    head = removeDuplicates(head)
    print_list(head)
    # if detect_loop(head):
    #     print("true")
    # else:
    #     print("false")        

