#Delete all occurrences of a given key in a doubly linked list
# Given a doubly linked list and a key x. The problem is to delete all occurrences of the given key x from the doubly linked list.

class Node: 
    def __init__(self,data): 
        self.data = data 
        self.next = None
        self.prev = None

def delAllOccurOfGivenKey(head,x):
    if not head:
        return None

    slow = None
    curr = head 
    #fast = head.next 


    # while curr:

    #     if curr.data == x:

    #         if curr == head:
    #             head = curr.next 
    #             if head:
    #                 head.prev = None
    #             curr = head 
    #             if curr:
    #                 fast = curr.next 
    #             else:
    #                 fast = None
    #         else:
    #             if slow:
    #                 slow.next = curr.next
    #             if fast: 
    #                 fast.prev = slow               
                
    #             curr = fast 
    #             if fast:
    #                 fast = fast.next
        
            
    #     else:
    #         slow = curr 
    #         curr = fast
    #         if fast:
    #             fast = fast.next
    #     #print_list(curr)
        
      
    #     #fast = fast.next if fast.next else None

    ########### This one if perfect self solution ############ 
    while curr:

        ## setting the fast not to next of curr node 
        fast = curr.next 
        # if slow:
        #     #print(f'start of LL --> {print_list(head)}')
        
        ## check if curr node data is matching to the given value 
        if curr.data == x :
            #First condition kind of edge case where we need to check if the give value is present in head of node 
            if head == curr:
                #print("head == curr")
                head = curr.next  # if head has given value then move head to next node 
                curr = head # Move current node also to head 
                curr.prev = slow   # and set curr node or head prev to None which is the slow value 
            else:
                # General case where given value is present at rest of the location in Double linked list 
                slow.next = fast ## Set the value of slow node next pointer to fast.
                if fast: ## if fast pointer is pointing to None then we cannot set fast.prev 
                    fast.prev = slow 
                curr = fast  ## we can move our current node to fast to exit out of loop . >> this will help to exit from loop 
        else:
            # Condition where current node != given value (x) then we have to do increment. 
            slow = curr
            curr = fast
            #print("outer else")
            #print(f'slow->{slow.data} curr-->{curr.data}')

    
    return head 



            
def print_list(node):
    while node:
        print(node.data, end="-->")
        node = node.next
    print()
if __name__ == "__main__":
  
    # creation of first list: 10 -> 15 -> 30
    head1 = Node(35)
    head1.next = Node(10)
    head1.next.next = Node(35)
    head1.next.next.next = Node(20)
    head1.next.next.next.next = Node(35)
    head1.next.next.next.next.next = Node(35)


    #print_list(head1)
    intersectionPoint = delAllOccurOfGivenKey(head1, 35)
    
    print_list(intersectionPoint)
   