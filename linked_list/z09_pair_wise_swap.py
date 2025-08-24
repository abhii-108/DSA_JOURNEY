#Pairwise Swap Elements of a given Linked List

# Input : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL 
# Output : 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL

# Input : 1 -> 2 -> 3 -> 4 -> 5 -> NULL 
# Output : 2 -> 1 -> 4 -> 3 -> 5 -> NULL


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def swap_pair(head):

    if head.next is None:
        return head 
    
    p1 = head 
    p2 = head.next 

    while True:

        temp = p1.data  
        p1.data = p2.data 
        p2.data = temp 

        if p2.next and p2.next.next:
            p1 = p2.next
            p2 = p1.next 
        else:
            break 

    return head 



def print_list(node):
    while node is not None:
        print(node.data, end="-->")
        node = node.next
    print()

if __name__ == "__main__":

    # head1 = Node(1)
    # head1.next = Node(2)
    # head1.next.next = Node(3)

    # Creating second linked list 4->5->6->7->8
    head = Node(4)
    head.next = Node(5)
    head.next.next = Node(6)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(8)
    head.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next = Node(10)

    # Store first and second head points in array
    ar = swap_pair(head)
    print_list(ar)
    #print_list(ar[1])      