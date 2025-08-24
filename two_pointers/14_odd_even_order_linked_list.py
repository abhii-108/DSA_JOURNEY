#Segregate even and odd nodes in LinkedList
# Problem Statement : Segregate even and odd nodes in LinkedList

# Given a LinkedList of integers. Modify the LinkedList in such a way that in Modified LinkedList all the even numbers appear before all the odd numbers in LinkedList.

# Also, note that the order of even and odd numbers should remain the same. 

# Examples:

# Example 1:
# Input: 1→2→3→4→5→6→Null
# Output: 2→4→6→1→3→5→Null
# Explanation : 
# Odd Nodes in LinkedList are 1,3,5 and 
# Even Nodes in LinkedList are 2,4,6
# In Modified LinkedList all even Nodes comes before 
# all Odd Nodes. So Modified LinkedList looks like 
# 2→4→6→1→3→5→Null. Order of even and odd Nodes is 
# maintained in modified LinkedList.

# Example 2:
# Input: 1→3→5→Null
# Output: 1→3→5→Null
# Explantion: As there are no Even Nodes in LinkedList, 
# The Modified LinkedList is same as Original LinkedList.

# Example 3:
# Input: 2→4→6→8→Null
# Output: 2→4→6→8→Null
# Explanation: As there are no Odd Nodes in LinkedList, 
# The Modified LinkedList is same as Original LinkedList.

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

def even_odd(head):
    if head.next is None:
        return head 
    
    odd = head 
    even = head.next 
    even_head = head.next 

    while even is not None and even.next is not None:
        odd.next = odd.next.next 
        even.next = even.next.next 
        print(f' odd->{odd.data}')
        print(f' even->{even.data}')

        odd = odd.next 
        even = even.next 
    
    odd.next = even_head

    return head 


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

result = even_odd(head)


printlist(result)