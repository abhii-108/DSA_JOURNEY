####### circular queue using Linked List #############

class Node:
    def __init__(self, newdata):
        self.data = newdata
        self.next = None

class CircularQueueL:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size = 0 


    def enqueue_l(self, data):
        newNode = Node(data)

        if self.front is None:
            self.front = newNode
        else:
            self.rear.next = newNode

        self.rear = newNode
        self.rear.next = self.front 

        self.size += 1
       

    def dequeue_l(self):

        if self.front == self.rear:
            return -1
        
        temp = self.front
        self.front = self.front.next
        self.rear.next = self.front
        self.size -= 1

        return temp.data 
    
    def getFront(self):
        front = self.front
        if self.front is None:
            return -1
        
        return front.data
    
    def getRear(self):
        rear = self.rear
        if self.rear is None:
            return -1
        
        return rear.data
    

    def isEmpty_L(self):

        if self.size == 0:
            return True 
        return False
    
    def getSize(self):
        return self.size 
    

if __name__ == '__main__':
    q = CircularQueueL()
    q.enqueue_l(10)
    print(f'{q.getFront()}, {q.getRear()}')
    q.enqueue_l(20)
    print(q.getFront(), q.getRear())
    q.enqueue_l(30)
    print(q.getFront(), q.getRear())
    q.enqueue_l(40)
    print(q.getFront(), q.getRear())
    q.dequeue_l()
    print(q.getFront(), q.getRear())
    q.dequeue_l()
    print(q.getFront(), q.getRear())
    q.enqueue_l(50)
    print(q.getFront(), q.getRear()) 
    








