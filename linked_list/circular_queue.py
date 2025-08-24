####### circular queue using Array #############

class CircularQueueA:
    def __init__(self,c):
        self.capacity = c
        self.arr = [0] * c
        self.front = 0
        self.size = 0

    
    def enqueue(self, data):
        if self.size == self.capacity:
            return 
        
        rear = (self.front + self.size) % self.capacity

        self.arr[rear] = data

        self.size += 1

    def dequeue(self):

        if self.size == 0:
            return -1
        temp = self.arr[self.front]
        self.front = (self.front+1) % self.capacity
        self.size -= 1
        return temp
    

    def getFront(self):

        if self.size == 0 :
            return -1
        return self.arr[self.front]


    def getRear(self):
        if self.size == 0:
            return -1 
        
        return self.arr[(self.front+self.size - 1) % self.capacity]

if __name__ == '__main__':
    q = CircularQueueA(4)
    q.enqueue(10)
    print(q.getFront(), q.getRear())
    q.enqueue(20)
    print(q.getFront(), q.getRear())
    q.enqueue(30)
    print(q.getFront(), q.getRear())
    q.enqueue(40)
    print(q.getFront(), q.getRear())
    q.dequeue()
    print(q.getFront(), q.getRear())
    q.dequeue()
    print(q.getFront(), q.getRear())
    q.enqueue(50)
    print(q.getFront(), q.getRear())            