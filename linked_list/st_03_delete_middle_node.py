## delete the middle of a node 
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def delet_node_middle(head):
    if not head or not head.next:
        return head 
    
    prev = None 
    slow = head 
    fast = head

    while fast.next and fast.next.next: ## for odd middle 
        prev = slow
        slow = slow.next 
        fast = slow.next.next 

    prev.next = slow.next

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
    sorted_head = delet_node_middle(head)
    print_list(sorted_head)


