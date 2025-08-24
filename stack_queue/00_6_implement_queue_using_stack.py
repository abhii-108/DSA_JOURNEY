# Queue using Stacks
# By Making Enqueue Operation Costly
# A queue can be implemented using two stacks. Let the queue be represented as q, and the stacks used for its implementation be s1 and s2.

# In this approach, the enqueue operation is made costly by transferring elements from stack1 to stack2 before adding the new element. This ensures that the elements in stack2 are in the correct order for dequeuing. The dequeue operation remains efficient, as it simply involves popping elements from stack2.
    
# enqueue(q, x): 

# While stack1 is not empty, push everything from stack1 to stack2.
# Push x to stack1 (assuming size of stacks is unlimited).
# Push everything back to stack1.
# dequeue(q): 

# If stack1 is empty then error.
# Pop an item from stack1 and return it.


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):

        while self.s1:
            self.s2.append(self.s1.pop())

        
        self.s1.append(data)

        while self.s2:
            self.s1.append(self.s2.pop())

    

    def dequeue(self):

        if not self.s1:
            return -1
        
        x = self.s1.pop()
        return x 
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())