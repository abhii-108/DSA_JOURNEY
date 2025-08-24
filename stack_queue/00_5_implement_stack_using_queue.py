# Implement Stack using Queues
# Using single queue and Recursion Stack


# Using only one queue and make the queue act as a Stack in modified way of the above discussed approach.

# Follow the below steps to implement the idea: 

# The idea behind this approach is to make one queue and push the first element in it. 
# After the first element, we push the next element and then push the first element again and finally pop the first element. 
# So, according to the FIFO rule of the queue, the second element that was inserted will be at the front and then the first element as it was pushed again later and its first copy was popped out. 
# So, this acts as a Stack and we do this at every step i.e. from the initial element to the second last element, and the last element will be the one that we are inserting and since we will be pushing the initial elements after pushing the last element, our last element becomes the first element.


from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()


    def push(self, data):

        s = len(self.q)

        self.q.append(data)

        for _ in range(s):
            self.q.append(self.q.popleft())

    
    def pop(self):

        if (not self.q):
            print("No element in stack")
        
        else:
            self.q.popleft()
    
    def top(self):
        if (not self.q):
            print("No element in stack")
        
        return self.q[0]
    
    def size(self):

        return len(self.q)
    
if __name__ == '__main__':
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print("current size: ", st.size())
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
    print("current size: ", st.size())