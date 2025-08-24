# from collections import deque


# def max_area_histogram(arr):
#     stack = deque()
#     op_nsl = [0] * len(arr)
#     op_nsr = [0] * len(arr)

#     ## First finding the nearest smallest index position to left of element

#     for i in range(0,len(arr)):

#         if len(stack) == 0:
#             op_nsl[i] = -1

#         elif stack[-1][1] < arr[i]:
#             op_nsl[i] = stack[-1][0]

#         else:
#             while (len(stack) != 0) and (stack[-1][1] >= arr[i]):
#                 stack.pop()
            
#             if len(stack) == 0:
#                 op_nsl[i] = -1
#             else:
#                 op_nsl[i] = stack[-1][0]

        
#         stack.append([i,arr[i]])
#     #print(f'OP_NSL --> {op_nsl}')
#     ## Empty stack to reduce
#     while len(stack) != 0:
#         stack.pop()

#     ## Second Find the nearest smallest index position to right element 
        
#     for i in range(len(arr)-1, -1, -1):

#         if len(stack) == 0:
#             op_nsr[i] = len(arr) 
        
#         elif stack[-1][1] < arr[i]:
#             op_nsr[i] = stack[-1][0]
        
#         else:
#             while (len(stack) != 0) and (stack[-1][1] >= arr[i]):
#                 stack.pop()
            
#             if len(stack) == 0:
#                 op_nsr[i] =  len(arr) 
#             else:
#                 op_nsr[i] = stack[-1][0]
        
#         stack.append([i,arr[i]])
#     #print(f'OP_NSR --> {op_nsr}')
#     max_area_hist = 0 

#     for i in range(0,len(arr)):

#         max_area_index = ((op_nsr[i] - op_nsl[i]) -1) * arr[i]
#         #print(f'({op_nsr[i]} - {op_nsl[i]} - 1 * {arr[i]}) --> {max_area_index}')
#         max_area_hist = max(max_area_index, max_area_hist)

#     return max_area_hist

    
    
# print(max_area_histogram([6,2,5,4,5,1,6]))


############################################ code with comments ############################
from collections import deque

def max_area_histogram(arr):
    stack = deque()
    op_nsl = [0] * len(arr)  # Stores indices of Nearest Smaller to Left
    op_nsr = [0] * len(arr)  # Stores indices of Nearest Smaller to Right

    ## 1️ Find nearest smaller to left (NSL)
    for i in range(0, len(arr)):
        if len(stack) == 0:
            op_nsl[i] = -1  # Nothing to the left
        elif stack[-1][1] < arr[i]:
            op_nsl[i] = stack[-1][0]  # Top of stack has smaller height
        else:
            while (len(stack) != 0) and (stack[-1][1] >= arr[i]):
                stack.pop()
            if len(stack) == 0:
                op_nsl[i] = -1             
            else:
                op_nsl[i] = stack[-1][0]
        stack.append([i, arr[i]])

    ## Clear the stack before reusing
    stack.clear()

    ## 2️ Find nearest smaller to right (NSR)
    for i in range(len(arr) - 1, -1, -1):
        if len(stack) == 0:
            op_nsr[i] = len(arr)  # Nothing to the right
        elif stack[-1][1] < arr[i]:
            op_nsr[i] = stack[-1][0]
        else:
            while (len(stack) != 0) and (stack[-1][1] >= arr[i]):
                stack.pop()
            if len(stack) == 0:
                op_nsr[i] = len(arr)
            else:
                op_nsr[i] = stack[-1][0]
        stack.append([i, arr[i]])

    ## 3️ Calculate max area
    max_area_hist = 0
    for i in range(0, len(arr)):
        max_area_index = (op_nsr[i] - op_nsl[i] - 1) * arr[i]  # Width between NSL and NSR
        print(f'({op_nsr[i]} - {op_nsl[i]} - 1 * {arr[i]}) --> {max_area_index}') ## for visualizing 
        max_area_hist = max(max_area_index, max_area_hist)

    return max_area_hist



print(max_area_histogram([6,2,5,4,5,1,6]))          # Output: 12
print(max_area_histogram([2, 4]))                   # Output: 4
print(max_area_histogram([5, 5, 5, 5]))             # Output: 20
print(max_area_histogram([5, 4, 3, 2, 1]))          # Output: 9
print(max_area_histogram([1]))                      # Output: 1 (edge case)
print(max_area_histogram([]))                       # Output: 0 (edge case)
