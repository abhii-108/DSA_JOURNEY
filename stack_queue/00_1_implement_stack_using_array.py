# #Stack using Array
######### Implementation using Fixed Sized Array ##############
# Stack is a linear data structure which follows LIFO principle. To implement a stack using an array, initialize an array and treat its end as the stack’s top. Implement push (add to end), pop (remove from end), and peek (check end) operations, handling cases for an empty or full stack.

# Step-by-step approach:

# Initialize an array to represent the stack.
# Use the end of the array to represent the top of the stack.
# Implement push (add to end), pop (remove from the end), and peek (check end) operations, ensuring to handle empty and full stack conditions.

# Push Operation in Stack:
# Adds an item to the stack. If the stack is full, then it is said to be an Overflow condition.

# Before pushing the element to the stack, we check if the stack is full .
# If the stack is full (top == capacity-1) , then Stack Overflows and we cannot insert the element to the stack.
# Otherwise, we increment the value of top by 1 (top = top + 1) and the new value is inserted at top position .
# The elements can be pushed into the stack till we reach the capacity of the stack.

# Pop Operation in Stack:
# Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.

# Before popping the element from the stack, we check if the stack is empty .
# If the stack is empty (top == -1), then Stack Underflows and we cannot remove any element from the stack.
# Otherwise, we store the value at top, decrement the value of top by 1 (top = top – 1) and return the stored top value.

# Top or Peek Operation in Stack:
# Returns the top element of the stack.

# Before returning the top element from the stack, we check if the stack is empty.
# If the stack is empty (top == -1), we simply print “Stack is empty”.
# Otherwise, we return the element stored at index = top .
# isEmpty Operation in Stack:
# Returns true if the stack is empty, else false.=

# Check for the value of top in stack.
# If (top == -1) , then the stack is empty so return true .
# Otherwise, the stack is not empty so return false .
# isFull Operation in Stack :
# Returns true if the stack is full, else false.

# Check for the value of top in stack.
# If (top == capacity-1), then the stack is full so return true .
# Otherwise, the stack is not full so return false.

class Stack:
    def __init__(self,cap):
        self.capacity = cap
        self.top = -1
        self.arr = [0] * cap

    
    def push(self, data):

        if self.top >= self.capacity - 1:
            print("Stack overflow")
            return
        
        self.top += 1
        self.arr[self.top] = data 
        return True

    
    def pop(self):
        if self.top < 0:
            print('stack underflow')
            return 0 
        
        popped = self.arr[self.top]
        self.top -= 1
        return popped 
    
    def peek(self):
        if self.top < 0:
            print("stack is empty")
        
        return self.arr[self.top]
    
    def isEmpty(self):
        return self.top < 0 
    

s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
print(s.pop(), "popped from stack")

print("Top element is:", s.peek())

print("Elements present in stack:", end=" ")
while not s.isEmpty():
    print(s.peek(), end=" ")
    s.pop()
