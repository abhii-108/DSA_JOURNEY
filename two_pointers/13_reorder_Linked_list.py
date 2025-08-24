#Rearrange a given linked list in-place

# Given a singly linked list L0 -> L1 -> … -> Ln-1 -> Ln. 
# Rearrange the nodes in the list so that the newly formed list is : L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ... You are required to do this in place without altering the nodes' values. 

# Input:  1 -> 2 -> 3 -> 4
# Output: 1 -> 4 -> 2 -> 3  
# Explanation: Here n = 4, so the correct order is L0->L3->L1->L2

# Input:  1 -> 2 -> 3 -> 4 -> 5 
# Output: 1 -> 5 -> 2 -> 4 -> 3
# Explanation: Here n = 4, so the correct order is L0->L4->L1->L3->L2

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

def printlist(node):
    
    if node is None:
        return
    
    while node is not None:
        print(node.data, end=" ")
        node = node.next



def rearrange(head):
    #check if linked list is empty or not 
    if head is None or  head.next is None:
        return head
    

    # finding the mid of the linked list 
    slow = head 
    fast = head 

    while (fast.next and fast.next.next):
        slow = slow.next 
        fast = fast.next.next 

    second_head = slow.next ## setting the start of second linked list which we have to reverse 
    slow.next = None 

    ### Reverse 2nd half of linked list 
    prev = None 
    curr = second_head

    while curr:
        next = curr.next 
        
        curr.next = prev 
        prev = curr
        curr = next 
    ### reverse of linked list completed 
    ## new head for 2nd half of linked list will be the prev. 
    first , second = head, prev 

    while second:
        ## Save the next node details of both first and second linked list in temp
        tmp1,tmp2 = first.next, second.next 

        # rearrange linked list as per requirement
        first.next  = second
        second.next = tmp1 

        first = tmp1 
        second = tmp2 
    
    return head 

head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = rearrange(head)


printlist(result)



