# #Queue - Linked List Implementation

# we maintain two pointers, front and rear. The front points to the first item of the queue and rear points to the last item.

# enQueue(): This operation adds a new node after the rear and moves the rear to the next node.
# deQueue(): This operation removes the front node and moves the front to the next node.

# Create a class Node with data members integer data and Node* next
# A parameterized constructor that takes an integer x value as a parameter and sets data equal to x and next as NULL
# Create a class Queue with data members Node front and rear
# Enqueue Operation with parameter x:
# Initialize Node* temp with data = x
# If the rear is set to NULL then set the front and rear to temp and return(Base Case)
# Else set rear next to temp and then move rear to temp
# Dequeue Operation:
# If the front is set to NULL return(Base Case)
# Initialize Node temp with front and set front to its next
# If the front is equal to NULL then set the rear to NULL
# Delete temp from the memory


class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None 

    
    def isEmpty(self):
        
        return self.front is None 
    

    def enqueue(self, x):
        new_node = Node(x)

        if self.isEmpty():
            self.rear = new_node
            self.front = new_node
            return

        self.rear.next = new_node

        self.rear = new_node
        self.printQueue()

    
    def dequeue(self):
        if self.isEmpty():
            return
        

        self.front = self.front.next 

        if self.front is None:
            self.rear = None
        
        self.printQueue()

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        queue_string = "Current Queue: "
        while temp is not None:
            queue_string += str(temp.data) + " "
            temp = temp.next
        print(queue_string)


q = Queue()

# Enqueue elements into the queue
q.enqueue(10)
q.enqueue(20)

# Dequeue elements from the queue
q.dequeue()
q.dequeue()

# Enqueue more elements into the queue
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

# Dequeue an element from the queue
q.dequeue()