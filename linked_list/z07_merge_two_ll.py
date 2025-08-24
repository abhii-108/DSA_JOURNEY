#Merge a linked list into another linked list at alternate positions


# #Input: head1: 1->2->3 , head2: 4->5->6->7->8
# Output: head1: 1->4->2->5->3->6 , head2: 7->8

# Input: head1: 10->12->21 , head2: 3->1->4
# Output: head1: 10->3->12->1->21->4, head2: <empty>

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 


def merge(head1, head2):

    p1 = head1 
    p2 = head2

    while p1 and p2 :

        next_p1 = p1.next 
        next_p2 = p2.next 
     
         
        p1.next = p2 
        if next_p1:
            p2.next = next_p1


        # if next_p1.next is None and next_p2.next is not None:
        #     p1.next = p2 
        #     break
        # elif next_p1.next is not None and next_p2 is None :


        p1 = next_p1 
        p2 = next_p2
    
    return head1 


    
def print_list(node):
    while node is not None:
        print(node.data, end="-->")
        node = node.next
    print()

if __name__ == "__main__":

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)

    # Creating second linked list 4->5->6->7->8
    head2 = Node(4)
    head2.next = Node(5)
    head2.next.next = Node(6)
    head2.next.next.next = Node(7)
    head2.next.next.next.next = Node(8)

    # Store first and second head points in array
    ar = merge(head1, head2)
    print_list(ar)
    #print_list(ar[1])       

