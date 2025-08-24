# #Remove every k-th node of the linked list
# Given a singly linked list, the task is to remove every kth node of the linked list. Assume that k is always less than or equal to the length of the Linked List.

# Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
# Output: 1 -> 3 -> 5 
# Explanation: After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 .

# Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
# Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
# Explanation: After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 


def remove_node(head, k):

    curr = head 
    temp = None 
    count = 0 

    while curr:
        count += 1

        if count % k == 0 :
            temp.next = curr.next 
        
        temp = curr 
        curr = curr.next 

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
    ar = remove_node(head, 4)
    print_list(ar)
    #print_list(ar[1])      