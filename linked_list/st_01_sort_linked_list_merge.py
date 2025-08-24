#To sort a linked list using merge sort, follow these steps:

# Base Case: If the list is empty or has only one node, return it as is.

# Split the List: Use the slow-fast pointer technique to find the middle node. The slow pointer moves one step at a time, while the fast pointer moves two steps. When the fast pointer reaches the end, the slow pointer will be at the middle.

# Break the List: Split the list into two halves by setting the next pointer of the node before the middle to None.

# Recursive Sort: Recursively apply merge sort to both halves.

# Merge Sorted Halves: Merge the two sorted halves by comparing nodes and linking them in ascending order


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def create_linked_list(arr):
    """Create a linked list from array"""
    dummy = Node(None)
    current = dummy
    for val in arr:
        current.next = Node(val)
        current = current.next
    linked_list_to_list(dummy.next)
    return dummy.next

def linked_list_to_list(head):
    """Convert linked list to Python list"""
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

# def getmid(head):
     
    

#     return slow 

def merge(left, right):
    ## create a dummy Node 

    dummy = Node(-1)
    curr = dummy 

    while left is not None and right is not None:
        if left.data < right.data:
            curr.next = left 
            left = left.next
            print('inside left small')
        else:
            curr.next = right
            right = right.next
            print('inside right big')
        curr = curr.next
        
    if left:
        curr.next = left 
    else:
        curr.next = right
    
    return dummy.next




def merge_sort_ll(head):
    if head is None or head.next is None:
        return head
    
    #mid = getmid(head)
    slow = head 
    fast = head.next 

    while fast and fast.next :
        slow = slow.next 
        fast = fast.next.next 

    right_head = slow.next 
    slow.next = None 
    # print_list(right_head)
    # print_list(head)
    

    left_partition = merge_sort_ll(head)
    right_partition = merge_sort_ll(right_head)

    return merge(left_partition,right_partition)




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
    head = Node(4)
    head.next = Node(9)
    head.next.next = Node(7)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(6)
    head.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next = Node(10)

    # Store first and second head points in array
    # ar = remove_node(head, 4)
    print_list(head)
    sorted_head = merge_sort_ll(head)
    print_list(sorted_head)
    #print_list(ar[1])      


# my_ll = Node(15)
# my_ll.next = Node(2)
# my_ll.next.next = Node(1)
# my_ll.next.next.next = Node(3)
# my_ll.next.next.next.next = Node(7)

# head = Node(10)
# head.next = Node(3)
# head.next.next = Node(2)
# head.next.next.next = Node(1)
# head.next.next.next.next = Node(9)
# head.next.next.next.next.next = Node(5)
# head.next.next.next.next.next.next = Node(7)

# sorted_head = merge_sort_ll(head)
# print(print_list(head))
# result = linked_list_to_list(sorted_head)
# print(f" {result} ")
# Test Cases
# test_inputs = [
#     [5],         # Test Case 2
#     [2, 1],      # Test Case 3
#     [5, 4, 3, 2, 1],  # Test Case 4
#     [3, 1, 4, 2, 2, 5]  # Test Case 5
# ]

# # expected_outputs = [
# #     [],
# #     [5],
# #     [1, 2],
# #     [1, 2, 3, 4, 5],
# #     [1, 2, 2, 3, 4, 5]
# # ]

# for i in range(len(test_inputs)):
#     head = create_linked_list(test_inputs[i])
#     sorted_head = merge_sort_ll(head)
#     result = linked_list_to_list(sorted_head)
#     #assert result == expected_outputs[i], f"Test {i+1} failed: {result} != {expected_outputs[i]}"
#print(f"Test {result} passed!")