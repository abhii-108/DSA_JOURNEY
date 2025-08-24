from collections import deque


def nearest_greater_left(arr):

    stack = deque()
    op = [0] * len(arr)

    for i in range(0, len(arr)):

        if len(stack) == 0:
            op[i] = -1
        
        elif arr[i] < stack[-1]:
            op[i] = stack[-1]

        else:
            while (len(stack) !=0) and (arr[i] >= stack[-1]):
                stack.pop()
            
            if len(stack) == 0 :
                op[i] = -1
            else:
                op[i] = stack[-1]

        stack.append(arr[i])
    
    return op 

print(nearest_greater_left([1,3,2,4]))
print(nearest_greater_left([1,3,0,0,1,2,4]))

        

#################################################################


# from collections import deque  # deque is a fast and flexible list used like a stack

# def nearest_greater_left(arr):
#     stack = deque()          # This will store candidates for "greater on the left"
#     op = [0] * len(arr)      # This will store our final answers (same length as input)

#     for i in range(0, len(arr)):  # Go from left to right in the list

#         if len(stack) == 0:
#             op[i] = -1  # No one to the left, so answer is -1
        
#         elif arr[i] < stack[-1]:  # Top of the stack is greater than current value
#             op[i] = stack[-1]

#         else:
#             # Keep removing smaller or equal numbers — they can't help us anymore
#             while (len(stack) != 0) and (arr[i] >= stack[-1]):
#                 stack.pop()
            
#             if len(stack) == 0:
#                 op[i] = -1  # No greater element found to the left
#             else:
#                 op[i] = stack[-1]  # Found one that is greater
        
#         # Always push current number to stack so it's available for next items
#         stack.append(arr[i])
    
#     return op  # Final result
