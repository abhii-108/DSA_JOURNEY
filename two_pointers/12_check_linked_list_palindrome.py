# Palindrome Linked List

# Given a singly linked list. The task is to check if the given linked list is palindrome or not.
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

def reverse_ll(head):

    prev = None
    curr = head 
    

    while curr :
        next = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next 
        
        #if next.nref is not None :
    return prev



def isPalindrome(head):

    if head is None or head.next is None:
        return True 
    
    slow = head 
    fast = head 

    while fast.next and  fast.next.next:
        slow = slow.next 
        fast = fast.next.next 

    print(f'value of slow pointer is {slow.data}')
    head2 = reverse_ll(slow.next) ## reverse the second half of linked list 


    # Now 2nd half of linked list is reverse 

    first = head 
    second = head2 

    while second is not None:
        print(f'first_part {first.data} --> second part {second.data}')
        if (first.data != second.data):
            return False
        else:
            first = first.next 
            second = second.next 

    reverse_ll(head2)    
    return True 


if __name__ == "__main__":
  
    # Linked list : 1->2->3->2->1
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    result = isPalindrome(head)

    if result:
        print("true")
    else:
        print("false")  
    