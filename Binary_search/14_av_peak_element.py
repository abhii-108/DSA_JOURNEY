# Peak Element in Array

# Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak element if it is strictly greater than its adjacent elements. If there are multiple peak elements, return the index of any one of them.

# Note: Consider the element before the first element and the element after the last element to be negative infinity.

# Examples:

# `Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
# Output: 5
# Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].

# Input: arr[] = [10, 20, 15, 2, 23, 90, 80]
# Output: 1 or 5
# Explanation: arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6].

# Input: arr[] = [1, 2, 3]
# Output: 2
# Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element, so it has negative infinity to its right.

def peak_element(arr):
    if len(arr) < 1:
        return -1 
    n = len(arr)
    ## checking the first and 2nd element in array because we have to compare it with one element 
    if arr[0] > arr[1]:
        return 0 
    
    #checking the last and 2nd last element as we need to compare it with one element 
    if arr[n-1] > arr[n-2]:
        return n-1
    

    left = 1 
    right = n-2 

    while left <= right:
        # Find the mid pos 

        mid = left + (right-left)//2


        if (arr[mid] > arr[mid-1]) & (arr[mid] > arr[mid+1]):
            return mid 
        
        elif arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid - 1
    return mid 

print(peak_element([1, 2, 4, 5, 7, 8, 3]))
print(peak_element([10, 20, 15, 2, 23, 90, 80]))

#bitonic_point 