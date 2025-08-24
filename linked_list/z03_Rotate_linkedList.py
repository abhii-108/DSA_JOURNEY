# Input: linked list = 10 -> 20 -> 30 -> 40 -> 50, k = 4
# Output: 50 -> 10 -> 20 -> 30 -> 40

# Input: linked list = 10 -> 20 -> 30 -> 40, k = 6
# Output: 30 -> 40 -> 10 -> 20 


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 


def rotate(head,k):

    if head is None:
        return -1
    
    curr = head 
    node_count = 1
    #first we need to count the number of nodes in Linked List
    while curr.next is not None:
        node_count += 1
        curr = curr.next 

    curr.next = head ## here we have rotated the linked list by pointing the next of last node from none to start to node 
    
    if node_count < k:
        k = k % node_count 
    
    curr = head
    for i in range(1,k):
        curr = curr.next 
    
    newhead = curr.next 
    curr.next = None 
    print(newhead.data)

    return newhead 

def print_list(node):
    while node is not None:
        print(node.data, end="-->")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list: 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    head = rotate(head, 6)
    print_list(head)
