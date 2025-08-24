# Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), peek() and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must have a time complexity of O(1). 


# Input: queries = [push(2), push(3), peek(), pop(), getMin(), push(1), getMin()]
# Output: [3, 2, 1] 

class special_stack:
    def __init__(self):
        self.p_stack=[]
        self.support_stack=[]


    def getMin(self):
        if len(self.support_stack) == 0:
            return -1 
        else:
            return self.support_stack[-1]
    
    def push(self, data):
        if (len(self.p_stack) == 0 ) or (self.support_stack[-1] >= data):
            self.support_stack.append(data)
        self.p_stack.append(data)
    
    def pop(self):

        if (self.p_stack[-1] == self.support_stack[-1]):            
            self.support_stack.pop()
        self.p_stack.pop()

    def isEmpty(self):
        return len(self.p_stack) == 0

    def peek(self):
        return self.support_stack[-1]
    
if __name__ == '__main__':
    stack = special_stack()
    
    stack.push(18)
    stack.push(19)
    print(stack.getMin())
    stack.push(29)
    print(stack.getMin())
    stack.push(15)
    stack.push(16)
    stack.push(1)
    #print(stack.peek())
    print(stack.getMin())
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.getMin())


############################################################################
    
# class SpecialStack:
#     """
#     A stack implementation that supports standard stack operations (push, pop, peek, isEmpty)
#     and an additional getMin() operation, all with O(1) time complexity.
#     It achieves this by using an auxiliary stack to store minimums encountered so far.
#     """
#     def __init__(self):
#         """
#         Initializes the SpecialStack.
#         self.p_stack: The primary stack where all elements are stored.
#         self.support_stack: The auxiliary stack that stores the minimum elements.
#                              It always stores elements in non-increasing order.
#         """
#         self.p_stack = []        # Main stack to store all elements.
#         self.support_stack = []  # Auxiliary stack to keep track of current minimums.

#     def getMin(self):
#         """
#         Returns the minimum element currently in the stack.
#         Hint: The minimum element is always at the top of the support_stack.
#         Time Complexity: O(1)
#         """
#         if self.isEmpty():
#             # Hint: Handle empty stack case for getMin gracefully.
#             # Returning a sentinel value like -1 or raising an error is common.
#             print("Error: Stack is empty, no minimum element.")
#             return -1
#         else:
#             return self.support_stack[-1]

#     def push(self, data):
#         """
#         Pushes an element onto the stack.
#         Hint: Always push to p_stack. Only push to support_stack if 'data'
#         is less than or equal to the current minimum (or if support_stack is empty).
#         Time Complexity: O(1)
#         """
#         self.p_stack.append(data) # Always add data to the primary stack.

#         # If support_stack is empty OR the incoming 'data' is less than or
#         # equal to the current minimum (top of support_stack), then push 'data'
#         # onto the support_stack. This ensures support_stack always has the minimum
#         # at its top and correctly tracks minimums. The 'equal to' part is crucial
#         # for handling duplicate minimums correctly during pop operations.
#         if not self.support_stack or data <= self.support_stack[-1]:
#             self.support_stack.append(data)

#     def pop(self):
#         """
#         Removes and returns the top element from the stack.
#         Hint: Pop from p_stack. If the popped element is also the current minimum,
#         then pop from support_stack as well.
#         Time Complexity: O(1)
#         """
#         if self.isEmpty():
#             # Hint: Handle popping from an empty stack.
#             print("Error: Cannot pop from an empty stack.")
#             return None # Or raise an IndexError
        
#         popped_element = self.p_stack.pop() # Pop from the primary stack.

#         # If the element popped from the primary stack is the current minimum
#         # (i.e., it matches the top of the support_stack), then also pop from
#         # the support_stack. This maintains the invariant that support_stack's
#         # top is always the current minimum.
#         if popped_element == self.support_stack[-1]:
#             self.support_stack.pop()
        
#         return popped_element # Return the popped element

#     def isEmpty(self):
#         """
#         Checks if the stack is empty.
#         Time Complexity: O(1)
#         """
#         return len(self.p_stack) == 0

#     def peek(self):
#         """
#         Returns the top element of the primary stack without removing it.
#         Hint: Access the last element of p_stack.
#         Time Complexity: O(1)
#         """
#         if self.isEmpty():
#             print("Error: Stack is empty, no element to peek.")
#             return None
#         return self.p_stack[-1]

# # --- Test Cases ---
# if __name__ == '__main__':
#     print("--- Test Case 1: Basic Operations ---")
#     stack1 = SpecialStack()
#     stack1.push(18)
#     stack1.push(19)
#     print(f"Current min: {stack1.getMin()} (Expected: 18)") # 18
#     stack1.push(29)
#     print(f"Current min: {stack1.getMin()} (Expected: 18)") # 18
#     stack1.push(15)
#     stack1.push(16)
#     stack1.push(1)
#     print(f"Current min: {stack1.getMin()} (Expected: 1)") # 1
#     print(f"Top element: {stack1.peek()} (Expected: 1)") # 1

#     print("\n--- Test Case 2: Pop Operations ---")
#     print(f"Popped: {stack1.pop()}") # Pop 1
#     print(f"Current min: {stack1.getMin()} (Expected: 15)") # 15
#     print(f"Popped: {stack1.pop()}") # Pop 16
#     print(f"Current min: {stack1.getMin()} (Expected: 15)") # 15
#     print(f"Popped: {stack1.pop()}") # Pop 15
#     print(f"Current min: {stack1.getMin()} (Expected: 18)") # 18
#     print(f"Popped: {stack1.pop()}") # Pop 29
#     print(f"Current min: {stack1.getMin()} (Expected: 18)") # 18
#     print(f"Popped: {stack1.pop()}") # Pop 19
#     print(f"Current min: {stack1.getMin()} (Expected: 18)") # 18
#     print(f"Popped: {stack1.pop()}") # Pop 18
#     print(f"Current min: {stack1.getMin()} (Expected: -1 / Error)") # Error: Stack empty

#     print("\n--- Test Case 3: Empty Stack Behavior ---")
#     stack_empty = SpecialStack()
#     print(f"Is stack empty? {stack_empty.isEmpty()} (Expected: True)")
#     stack_empty.pop() # Error message
#     stack_empty.getMin() # Error message
#     print(f"Is stack empty? {stack_empty.isEmpty()} (Expected: True)")

#     print("\n--- Test Case 4: Duplicates and Monotonicity ---")
#     stack_dup = SpecialStack()
#     stack_dup.push(10)
#     stack_dup.push(5)
#     stack_dup.push(10) # 10 is not smaller than 5, so not pushed to support_stack
#     print(f"Current min: {stack_dup.getMin()} (Expected: 5)") # 5
#     stack_dup.push(3)
#     stack_dup.push(3) # Duplicate minimum, both pushed to support_stack
#     print(f"Current min: {stack_dup.getMin()} (Expected: 3)") # 3
#     print(f"Popped: {stack_dup.pop()}") # Pop 3
#     print(f"Current min: {stack_dup.getMin()} (Expected: 3)") # Still 3
#     print(f"Popped: {stack_dup.pop()}") # Pop 3
#     print(f"Current min: {stack_dup.getMin()} (Expected: 5)") # 5


# Maintain two stacks:

# p_stack (Primary Stack): This is your regular stack. All elements pushed by the user go here.
# support_stack (Auxiliary Stack / Min Stack): This stack stores elements that are potential minimums. It's designed such that its top element always represents the current minimum value in the p_stack.
# Let's examine how each operation works:

# __init__(self):

# Initializes both self.p_stack and self.support_stack as empty lists.
# push(self, data):

# Always push data to self.p_stack: This ensures that p_stack behaves like a normal stack.
# Logic for self.support_stack:
# If self.support_stack is empty, it means this is the very first element being pushed (or all previous elements were popped, and a new sequence begins). In this case, data is currently the minimum, so data is pushed onto self.support_stack.
# If self.support_stack is NOT empty, we compare data with the current minimum (which is self.support_stack[-1]).
# If data <= self.support_stack[-1] (i.e., data is smaller than or equal to the current minimum), then data becomes the new minimum or a duplicate minimum. In either case, it's a relevant minimum, so data is pushed onto self.support_stack.
# If data > self.support_stack[-1], then data is larger than the current minimum. It does not become a new minimum, so we do not push it onto self.support_stack. The existing minimum on support_stack remains valid.
# Why data <= self.support_stack[-1]? Using <= instead of < is crucial for correctly handling duplicate minimums. If you push 5, then 3, then another 3, and then pop() the first 3, you want the second 3 to still be considered the minimum. If you only pushed on <, you'd only store the first 3, and popping it would lead to incorrect getMin().
# pop(self):

# Check for empty stack: Essential safety check. If self.p_stack is empty, there's nothing to pop.
# Pop from self.p_stack: Get the element from the top of the main stack.
# Logic for self.support_stack:
# Compare the popped_element with the top of self.support_stack (self.support_stack[-1]).
# If popped_element == self.support_stack[-1], it means the element we just popped from p_stack was also the current minimum element being tracked by support_stack. Therefore, we must also pop() it from self.support_stack to reveal the previous minimum.
# If popped_element != self.support_stack[-1], it means the popped element was not the current minimum. The minimum tracked by support_stack is still valid, so we do nothing with support_stack.
# Returns the popped_element.
# getMin(self):

# Check for empty stack: If self.p_stack (and thus self.support_stack) is empty, there's no minimum.
# Return top of self.support_stack: By design, the top element of self.support_stack is always the current minimum in self.p_stack. This is an O(1) operation.
# isEmpty(self):

# Simply checks if self.p_stack is empty. The support_stack will be empty if and only if p_stack is empty.
# peek(self):

# Returns the top element of self.p_stack without removing it, just like a standard stack peek.