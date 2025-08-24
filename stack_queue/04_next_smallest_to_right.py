from collections import deque

def nearest_smallest_right(arr):

    stack = deque()
    op = [0] * len(arr)

    for i in range(len(arr)-1, -1, -1):

        if len(stack) == 0:
            op[i] = -1
        
        elif (len(stack)!=0) and (arr[i] > stack[-1]):
            op[i] = stack[-1]

        
        elif (len(stack) != 0) and (arr[i] <= stack[-1]):
            
            while (len(stack) != 0) and (arr[i] <= stack[-1]):
                #print(f'inside while value of i is {arr[i]}')
                stack.pop()
                

            if len(stack) == 0:
                op[i] = -1
            else:
                op[i] = stack[-1]
        
        stack.append(arr[i])
    
    return op
    

print(nearest_smallest_right([4,5,2,10,8]))
