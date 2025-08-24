# #Stack - Linked List Implementation

# #To implement a stack using a singly linked list, we follow the LIFO (Last In, First Out) principle by inserting and removing elements from the head of the list, where each node stores data and a pointer to the next node.

# #In the stack Implementation, a stack contains a top pointer. which is the "head" of the stack where pushing and popping items happens at the head of the list. The first node has a null in the link field and second node-link has the first node address in the link field and so on and the last node address is in the "top" pointer.

# The main advantage of using a linked list over arrays is that it is possible to implement a stack that can shrink or grow as much as needed.
# Using an array will put a restriction on the maximum capacity of the array which can lead to stack overflow. Here each new node will be dynamically allocated. so overflow is not possible.
# If we use built in dynamic sized arrays like vector in C++, list in Python or ArrayList in Java, we get automatically growing stack, but the worst case time complexity is not O(1) for push() and pop() as there might be a resizing step once in a while. With Linked List, we get worst case O(1).


# Stack Operations
# push(): Insert a new element into the stack (i.e just insert a new element at the beginning of the linked list.)
# pop(): Return the top element of the Stack (i.e simply delete the first element from the linked list.)
# peek(): Return the top element.
# display(): Print all elements in Stack.


class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None 

    
    def isEmpty(self):
        return self.head is None 
    
    def push(self, x ):
        
        new_node = Node(x)

        new_node.next = self.head 
        self.head = new_node 

    
    def pop(self):
        
        if self.isEmpty():
            return 
        
        self.head = self.head.next 
    
    def peek(self):

        if not self.isEmpty():
            return self.head.data 
        
        return float('-inf')
    
st = Stack()

st.push(11)
st.push(22)
st.push(33)
st.push(44)

print(st.peek())

st.pop()
st.pop()

print(st.peek())
