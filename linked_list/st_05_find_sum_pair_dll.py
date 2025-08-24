# Find all Pairs with given Sum in sorted DLL
# Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to the given value x in sorted order.

#EG 1->2->4->5->6->8->9

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None

def sum_pair_dll(head,target):
    #check edge case of head
    if not head:
        return -1 
    
    #since array is sorted we need to find the last node also to use two pointer approach. 

    tmp = head 
    counter = 1
    while tmp.next:
        tmp = tmp.next
        counter += 1

    # initializing the left and right pointer 
    right = tmp 
    right_cnt = counter
    left = head 
    left_cnt = 1 
    op = []

    while left_cnt < right_cnt :
        curr_sum = left.data + right.data 

        if curr_sum == target:
            op.append((left.data , right.data))
            left = left.next 
            left_cnt += 1
            right = right.prev
            right_cnt -= 1
            
        
        elif curr_sum < target:
            left = left.next
            left_cnt += 1
        else:
            right = right.prev 
            right_cnt -= 1

    return op 

def print_list(node):
    while node:
        print(node.data, end="<-->")
        node = node.next
    print()

if __name__ == "__main__":

    # head1 = Node(1)
    # head1.next = Node(2)
    # head1.next.next = Node(3)

    # Creating second linked list 4->5->6->7->8
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next


    print_list(head)
    op = sum_pair_dll(head,5)
    print(op)


    # sorted_head = sum_pair_dll(head,4)
    # print_list(sorted_head)
    





