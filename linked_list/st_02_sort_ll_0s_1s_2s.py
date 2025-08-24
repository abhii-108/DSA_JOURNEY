#Sort a linked list of 0s, 1s and 2s
#Given a linked list of 0s, 1s and 2s, The task is to sort the list in non-decreasing order.


#Input: 1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL
# Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL

# Input: 1 -> 1 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 1 -> 1 -> 2 -> NULL 


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def sorting(head):
    # Edge case to check if head & head.next is empty or not 

    if not head or not head.next:
        return head 

    zero_head = Node(-1)
    one_head = Node(-1)
    two_head = Node(-1)

    zero = zero_head
    one = one_head
    two = two_head

    curr = head 
    while curr:
        next_node = curr.next
        curr.next = None

        if curr.data == 0 :
            zero.next = curr
            zero = zero.next 
        
        elif curr.data == 1:
            one.next = curr
            one = one.next 
        
        elif curr.data == 2:
            two.next = curr 
            two = two.next 
        
        curr = next_node
    

    head = zero_head.next or one_head.next or two_head.next 

    if zero_head.next :
        zero.next = one_head.next  if one_head.next else two_head.next 
    
    if one_head.next:
        one.next = two_head.next 

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
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(0)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)
    head.next.next.next.next.next.next = Node(0)

    print_list(head)
    sorted_head = sorting(head)
    print_list(sorted_head)
