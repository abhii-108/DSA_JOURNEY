from collections import deque 

def nearest_smallest_left(arr):
    stack = deque()
    op = [0] * len(arr)

    for i in range(0, len(arr)):

        if len(stack) == 0:
            op[i] = -1
        
        elif arr[i] > stack[-1]:
            op[i] = stack[-1]

        else:
            while (len(stack) != 0) and (arr[i] <= stack[-1]):
                stack.pop()
            
            if len(stack) == 0:
                op[i] = -1
            else:
                op[i] = stack[-1]
        
        stack.append(arr[i])
    
    return op 

# print(nearest_smallest_left([1,3,2,4]))
# print(nearest_smallest_left([1,3,0,0,1,2,4]))

print(nearest_smallest_left([1, 3, 2, 4]))
# Output: [-1, 1, 1, 2]

print(nearest_smallest_left([1, 3, 0, 0, 1, 2, 4]))
# Output: [-1, 1, -1, -1, 0, 1, 2]

print(nearest_smallest_left([5, 4, 3, 2, 1]))
# Output: [-1, -1, -1, -1, -1]  # All decreasing, so no smaller lefts

print(nearest_smallest_left([2, 1, 2, 1, 2]))
# Output: [-1, -1, 1, -1, 1]  # Mix of ups and downs

print(nearest_smallest_left([4, 5, 6, 1, 2, 3]))