## Sort Array by Parity: Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers. 
## The relative order of the even and odd elements does not matter.

# Input: arr = [0, 1, 2, 3, 4]
# Output: arr = [0, 2, 4, 1, 3]
# Explanation: 0 2 4 are even and 1 3 are odd numbers. Please note that [2, 0, 4, 3, 1] or [4, 2, 0, 1, 3] are also valid outputs. We only need to make sure that all even elements are before all odd. 

# Input : arr = {1, 5, 11}
# Output : arr = {1, 5, 11}
# Explanation All numbers are odd

def sort_array_by_parity(arr):
    
    if len(arr) <= 1:
        return arr 
    # using fast and slow pointer technique 
    slow = 0 

    for fast in range(0, len(arr)):

        if arr[fast] % 2 == 0:
            temp = arr[slow]
            arr[slow] = arr[fast]
            if temp %2 != 0:
                arr[fast] = temp 
                

            slow += 1

    return arr

print(sort_array_by_parity([0, 1, 2, 3, 4,5,6,8,9,11]))
print(sort_array_by_parity([1, 5, 11]))


## another method is using two pointer left and right. Only difference will be the output position of even element will be at different place. 

def sort_array_by_parity2(arr):
    
    if len(arr) <= 1:
        return arr 
    
    # creating left and right pointer variable for traversal 

    left, right = 0 , len(arr) - 1

    while left <= right :

        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] %2 != 0:
            right -= 1

        else:
            #swapping the value if above both condition fail
            arr[left], arr[right] = arr[right], arr[left] 

    

    return arr

print(sort_array_by_parity2([0, 1, 2, 3, 4,5,6,8,9,11]))
print(sort_array_by_parity2([1, 5, 11]))

