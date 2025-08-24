
# Find Middle of the Linked List
# Input: linked list: 1->2->3->4->5
# Output: 3 
# Explanation: There are 5 nodes in the linked list and there is one middle node whose value is 3.


# Input: linked list = 10 -> 20 -> 30 -> 40 -> 50 -> 60
# Output: 40
# Explanation: There are 6 nodes in the linked list, so we have two middle nodes: 30 and 40, but we will return the second middle node which is 40.



class Node:
    def __init__(self,data):
        self.data = data 
        self.nref = None 

    
def find_middle(head):

    if head is None:
        return -1 
    #print(head.nref.data)
    slow_pointer = head 
    fast_pointer = head 

    while fast_pointer is not None and fast_pointer.nref is not None:
        #print(f'{slow_pointer.data}', end='-->')
        slow_pointer = slow_pointer.nref 
        
        #print(f'{fast_pointer.data}', end='---->')
        fast_pointer = fast_pointer.nref.nref

    return slow_pointer.data 

def main():

    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40 -> 50 -> 60
    head = Node(10)
    head.nref = Node(20)
    head.nref.nref = Node(30)
    head.nref.nref.nref = Node(40)
    head.nref.nref.nref.nref = Node(50)
    head.nref.nref.nref.nref.nref = Node(60)

    print(find_middle(head))

if __name__ == "__main__":
    main()