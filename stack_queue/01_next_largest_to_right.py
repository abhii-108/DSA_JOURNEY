# from collections import deque

# def nearest_greater_right(arr):

#     stack = deque()
#     op = [0] * len(arr)

#     for i in range(len(arr)-1, -1, -1):

#         if len(stack) == 0:
#             op[i] = -1
        
#         elif (len(stack)!=0) and (arr[i]< stack[-1]):
#             op[i] = stack[-1]

        
#         elif (len(stack) != 0) and (arr[i] >= stack[-1]):
            
#             while (len(stack) != 0) and (arr[i] >= stack[-1]):
#                 #print(f'inside while value of i is {arr[i]}')
#                 stack.pop()
                

#             if len(stack) == 0:
#                 op[i] = -1
#             else:
#                 op[i] = stack[-1]
        
#         stack.append(arr[i])
    
#     return op
    

# print(nearest_greater_right([1,3,2,4]))
# print(nearest_greater_right([1,3,0,0,1,2,4]))

##########################################################

from collections import deque  # Like a special list that's good for stacks

def nearest_greater_right(arr):
    stack = deque()  # This will help us track the "next bigger numbers"
    op = [0] * len(arr)  # This is our answer list (same size as input)

    # We start from the RIGHT side and move to the LEFT
    for i in range(len(arr) - 1, -1, -1):

        # If stack is empty, no greater number to the right
        if len(stack) == 0:
            op[i] = -1
        
        # If top of the stack is greater than current element
        elif arr[i] < stack[-1]:
            op[i] = stack[-1]

        # If current element is greater or equal to what's on top of stack
        else:
            # Pop everything smaller or equal to arr[i]
            while len(stack) != 0 and arr[i] >= stack[-1]:
                stack.pop()

            # After popping, check if anything is left in stack
            if len(stack) == 0:
                op[i] = -1  # Nothing greater to the right
            else:
                op[i] = stack[-1]  # This is the next greater element
        
        # Push current element onto the stack
        stack.append(arr[i])
    
    return op

print(nearest_greater_right([1,3,2,4]))
print(nearest_greater_right([1,3,0,0,1,2,4]))
# print(nearest_greater_right([1,3,0,0,1,2,4]))
