##Delete Nth node from the end of the given linked list
#Given a linked list and an integer N, the task is to delete the Nth node from the end of the given linked list.


# Input: 2 -> 3 -> 1 -> 7 -> NULL, N = 1 
# Output: 2 3 1
# Explanation: The created linked list is: 2 3 1 7 
# The linked list after deletion is: 2 3 1

# Input: 1 -> 2 -> 3 -> 4 -> NULL, N = 4 
# Output: 2 3 4
# Explanation: The created linked list is: 1 2 3 4 
# The linked list after deletion is: 2 3 4 

# Input: 5 -> 3 -> 8 -> 6 -> NULL, N = 2 
# Output: 5 3 6
# Explanation: The created linked list is: 5 3 8 6
# The linked list after deletion is: 5 3 6 

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def del_node_n(head,n):
    if not head or n == 0:
        return head 
    
    prev = None 
    slow = head 
    fast = head 

    for i in range(n):
        fast = fast.next 

    while fast:
        prev = slow
        slow = slow.next 
        fast = fast.next 
    
    # check if prev is pointing at some node then only modify it next pointer 
    if prev:
        prev.next = prev.next.next 
    else: # if we want to delete first node then move head  
        head = head.next 


    return head 

def print_list(node):
    while node:
        print(node.data, end="-->")
        node = node.next
    print()

if __name__ == "__main__":

    # head1 = Node(1)
    # head1.next = Node(2)
    # head1.next.next = Node(3)

    # Creating second linked list 4->5->6->7->8
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(13)
    head.next.next.next.next.next.next = Node(15)

    print_list(head)
    sorted_head = del_node_n(head,1)
    print_list(sorted_head)


    # sorted_head = del_node_n(head,4)
    # print_list(sorted_head)
    
