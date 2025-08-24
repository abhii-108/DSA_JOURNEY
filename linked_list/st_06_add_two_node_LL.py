## Addition of two node in a linked list 

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def addition(head1, head2):

    tmp1 = head1 
    tmp2 = head2 

    dummy = Node(-1)
    curr = dummy
    carry = 0 
    
    while (tmp1 is not None) or (tmp2 is not None):
        sum = 0
        if tmp1:
            sum += tmp1.data 
            tmp1 = tmp1.next 
        
        if tmp2:
            sum += tmp2.data 
            tmp2 = tmp2.next 
        
        sum += carry
        print(sum)
        newNode = Node(sum%10)
        #
        carry = sum // 10
        curr.next = newNode
        curr = curr.next
        
            

    return dummy.next 


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
    

    head2 = Node(9)
    head2.next = Node(9)
    head2.next.next = Node(2)
    head2.next.next.next = Node(8)

    print_list(head)
    print_list(head2)
    sorted_head = addition(head,head2)
    print_list(sorted_head)


    