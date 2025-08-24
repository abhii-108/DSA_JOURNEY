# Implement a stack using singly linked lis
# To implement a stack using a singly linked list, we need to ensure that all operations follow the LIFO (Last In, First Out) principle. This means that the most recently added element is always the first one to be removed. In this approach, we use a singly linked list, where each node contains data and a reference (or link) to the next node.

# To manage the stack, we maintain a top pointer that always points to the most recent (topmost) node in the stack. The key stack operations—push, pop, and peek can be performed using this top pointer

# Stack Operations
# push(): Insert a new element into the stack (i.e just insert a new element at the beginning of the linked list.)
# pop(): Return the top element of the Stack (i.e simply delete the first element from the linked list.)
# peek(): Return the top element.
# display(): Print all elements in Stack.


class node:
    def __init__(self,data):
        self.data = data 
        self.nref = None 


class Llqueue:
    def __init__(self):
        self.head = None 

    
    #push method 
    def push(self,data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.nref = self.head 
        self.head = new_node
    
    def pop(self):
        if self.head is None:
            return 
        temp = self.head.data
        self.head = self.head.nref
        return temp 

    def peek(self):
        
        return self.head.data 
    
    def display(self):
        if self.head is None:
            return 
        
        curr = self.head 

        while curr is not None:
            print(f'{curr.data}', end=' ')
            curr = curr.nref 

        return 

if __name__ == "__main__":


    my_stack = Llqueue()
    my_stack.push(4)
    my_stack.push(5)
    my_stack.push(6)
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(220)
    my_stack.display()
    print( end='\n')
    print('---------', end='\n')
    print(my_stack.peek())
    print('---------', end='\n')
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print('---------', end='\n')
    my_stack.display()

  

            
        

        