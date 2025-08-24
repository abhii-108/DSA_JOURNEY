# Detect Loop or Cycle in Linked List

# Input: head: 1 -> 3 -> 4 -> 3
# Output: true
# Input: head: 1 -> 8 -> 3 -> 4 -> NULL 
# Output: false

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
 

def detect_loop(head):

    if head is None or head.next is None:
        return -1 
    
    slow_pointer = head 
    fast_pointer = head 

    while fast_pointer is not None:
        slow_pointer = slow_pointer.next 

        if fast_pointer.next is None:
            return "No loop is detected"
        
        fast_pointer = fast_pointer.next.next 

        if fast_pointer == slow_pointer:
            return "Loop detected"

    return "No loop detected..!"

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
  
    # Create a loop
    #head.next.next.next = head.next
    print(detect_loop(head))
    # if detect_loop(head):
    #     print("true")
    # else:
    #     print("false")        

