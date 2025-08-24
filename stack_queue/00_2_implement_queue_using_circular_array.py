#Circular Array Implementation of Queue

# A Circular Queue is a way of implementing a normal queue where the last element of the queue is connected to the first element of the queue forming a circle.

# The operations are performed based on the FIFO (First In First Out) principle. It is also called 'Ring Buffer'. In a normal Queue, we can insert elements until the queue becomes full. However once the queue becomes full, we can not insert the next element even if there is a space in front of the queue.

# Operations on Queue
# getFront: Get the front item from the queue.
# getRear: Get the last item from the queue.
# enqueue(value): To insert an element into the circular queue. In a circular queue, the new element is always inserted at the rear position. 
# dequeue(): To delete an element from the circular queue. In a circular queue, the element is always deleted from the front position.

# Implement Queue using Circular Array
# Initialize an array of size n, where n is the maximum number of elements that the queue can hold.
# Initialize three variables (size, capacity, and front.)
# Enqueue: To enqueue an element x into the queue, do the following:
# Check if size == capacity (queue is full), display "Queue is full".
# If not full: calculate rear = (front + size) % capacity and Insert value at the rear index. Increment size by 1.
# Dequeue: To dequeue an element from the queue, do the following:
# Check if size == 0 (queue is empty), display "Queue is empty".
# If not empty: retrieve the element at the front index and move front = (front + 1) % capacity. Also, decrement size by 1 and return the removed element.


class Queue:
    def __init__(self,c):
        self.capacity = c
        self.size = 0 
        self.front = 0 
        self.arr = [0] * c 

    
    def getFront(self):

        if self.size == 0 :
            return -1 
        
        return self.arr[self.front]
    
    def getRear(self):

        if self.size == 0 :
            return -1 
        
        rear = (self.front + self.size -1) % self.capacity
        return self.arr[rear]
    

    def enqueue(self,x):

        if self.size == self.capacity:
            return
        
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x 

        self.size += 1 

    
    def dequeue(self):
        if self.size == 0:
            return -1 
        
        res = self.arr[self.front]

        self.front = (self.front + 1 ) % self.capacity

        self.size -= 1

        return res 
    

if __name__ == '__main__':
    q = Queue(4)
    q.enqueue(10)
    print(q.getFront(), q.getRear()) # 10 10
    q.enqueue(20)
    print(q.getFront(), q.getRear()) #10 20
    q.enqueue(30)
    print(q.getFront(), q.getRear()) #10 30
    q.enqueue(40)
    print(q.getFront(), q.getRear()) #10 40
    q.dequeue()
    print(q.getFront(), q.getRear()) #20 40
    q.dequeue()
    print(q.getFront(), q.getRear()) #30 40
    q.enqueue(50)
    print(q.getFront(), q.getRear()) #30 50