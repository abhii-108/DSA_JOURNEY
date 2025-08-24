class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    ## Adding element in th queue
    def enqueue(self,data):
        if self.front is None: # checking if Queue is empty
            new_node = Node(data)
            self.front = new_node
            self.rear = new_node
            self.size += 1
            return
        ## If Queue is not empty 
        new_node = Node(data)
        self.rear.next = new_node
        self.rear = new_node 
        self.size += 1

    def dequeue(self):
        #we need to remove the first element from the queue 
        #First check if queue is empty or not 

        if self.front is None:
            return None

        temp = self.front
        self.front = temp.next

        ##Edge case if there was only 1 element 
        if self.front is None: 
            self.rear = None
        self.size -= 1
        return temp.data
    
    def peek(self):
        
        if self.front is None:
            return None

        return self.front.data
    
    def isEmpty(self):

        return self.front == 0 
    
    def getSize(self):

        return self.size
    


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(f"display the top element {queue.peek()}")
    print(f'size of my queue is {queue.getSize()}')

    
    
