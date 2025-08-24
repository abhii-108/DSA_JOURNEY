# First negative in every window of size k

# Given an array arr[]  and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.

# Note: If a window does not contain a negative integer, then return 0 for that window.

# Input: arr[] = [-8, 2, 3, -6, 10] , k = 2
# Output: [-8, 0, -6, -6]
# Input: arr[] = [12, -1, -7, 8, -15, 30, 16, 28] , k = 3
# Output: [-1, -1, -7, -15, -15, 0] 


from collections import deque 


def first_negative_subarry(arr,k):

    my_queue = deque()

    i = 0 # left pointer or start of the window
    j = 0 # Right pointer or End of window 

    op=[] 

    while j < len(arr):

        if arr[j] < 0:
            my_queue.appendleft(arr[j])  ## use appendleft method to add element to the left normal append will add value to right and it will be the top element. 
            #print(my_queue[-1])

        if (j-i+1) < k:
            
            j += 1

        elif (j-i+1) == k :

            if len(my_queue) != 0 :
                print(f'{my_queue} value add in op {my_queue[-1]}')
                op.append(my_queue[-1])
            else:
                op.append(0)
                
            
            if len(my_queue) != 0 and arr[i] == my_queue[-1]:
                my_queue.pop()
            
            i += 1
            j += 1
    
    return op 

print(first_negative_subarry([-8, 2, 3, -6, 10],2))
print(first_negative_subarry([12, -1, -7, 8, -15, 30, 16, 28],3))
