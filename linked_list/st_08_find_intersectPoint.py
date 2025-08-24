# Intersection point of two Linked Lists

# Given two singly linked lists that merge into a single Y-shaped list. T
# The two lists initially have distinct paths but eventually converge at a common node, forming a Y-shape, the task is to find and return the node where the two lists merge.

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def intersectPoint(head1, head2):
    if not head1 or not head2 :
        return None

    tmp1 = head1 
    tmp2 = head2 

    while tmp1 != tmp2:
        if tmp1:
            tmp1 = tmp1.next 
        else:
            tmp1 = head2
        
        if tmp2:
            tmp2 = tmp2.next 
        else:
            tmp2 = head1

    if tmp1 :
        return tmp1.data
    else:
        return None


def print_list(node):
    while node:
        print(node.data, end="-->")
        node = node.next
    print()
if __name__ == "__main__":
  
    # creation of first list: 10 -> 15 -> 30
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)
    head1.next.next.next = Node(35)
    head1.next.next.next.next = Node(45)

    # creation of second list: 3 -> 6 -> 9 -> 15 -> 30
    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)

    # 15 is the intersection point
    head2.next.next.next = head1.next.next

    intersectionPoint = intersectPoint(head1, head2)
    print_list(head1)
    print_list(head2)
    if not intersectionPoint:
        print("-1")
    else:
        print(intersectionPoint)


    head3 = Node(3)
    head3.next = Node(6)

    head4 = Node(8)
    head4.next = Node(9)

    intersectionPoint2 = intersectPoint(head3, head4)
    print_list(head3)
    print_list(head4)
    if not intersectionPoint:
        print("-1")
    else:
        print(intersectionPoint2)


##################################################################################
        
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

def intersectPoint(head1, head2):
    # If either list is empty, no intersection possible
    if not head1 or not head2:
        return None
    
    # Initialize two pointers at the heads of both lists
    tmp1 = head1 
    tmp2 = head2 
    
    # Continue traversing until both pointers meet
    while tmp1 != tmp2:
        # If tmp1 has next node, move forward
        if tmp1.next:
            tmp1 = tmp1.next 
        # Otherwise, jump to start of second list
        else:
            tmp1 = head2
        
        # If tmp2 has next node, move forward
        if tmp2.next:
            tmp2 = tmp2.next 
        # Otherwise, jump to start of first list
        else:
            tmp2 = head1
    
    # After meeting point:
    if tmp1:  # If meeting point is a valid node
        return tmp1.data  # Return intersection data
    else:
        return None  # No intersection found