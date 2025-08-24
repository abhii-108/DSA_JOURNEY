#Bitonic Point - Maximum in Increasing Decreasing Array

# Given an array arr[] of integers which is initially strictly increasing and then strictly decreasing, the task is to find the bitonic point, that is the maximum value in the array. 

# Note: Bitonic Point is a point in bitonic sequence before which elements are strictly increasing and after which elements are strictly decreasing.

# Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
# Output: 8
# Explanation: 8 is the maximum element in the array.

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 50
# Explanation: 50 is the maximum element in the array.

# Input: arr[] = [120, 100, 80, 20, 0]
# Output: 120
# Explanation: 120 is the maximum element in the array.


def bitonic_point(arr):

    n = len(arr)

    if n == 0 or arr[0] > arr[1]:
        return arr[0]
    
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    

    left = 1 
    right = n-2 


    while left <= right:

        mid = left + (right - left) // 2

        if (arr[mid] > arr[mid-1]) & (arr[mid] > arr[mid+1]):
            return arr[mid]
        
        elif arr[mid] < arr[mid+1]:
            left = mid +1 

        else:
            right = mid - 1
        
    return arr[right]



print(bitonic_point([1, 2, 4, 5, 7, 8, 3]))


print(bitonic_point([10, 20, 30, 40, 50]))
print(bitonic_point([120, 100, 80, 20, 0]))
