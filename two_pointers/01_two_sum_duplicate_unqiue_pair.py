# 2 Sum - Count pairs with given sum

# Given an array arr[] of n integers and a target value, the task is to find the number of pairs of integers in the array whose sum is equal to target.

# Input: arr[] = {1, 5, 7, -1, 5}, target = 6
# Output:  3
# Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

# Input: arr[] = {1, 1, 1, 1}, target = 2
# Output:  6
# Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) and (1, 1).

# Input: arr[] = {10, 12, 10, 15, -1}, target = 125
# Output:  0

## Two Sum with Duplicates: Given a sorted array with duplicates, find all unique pairs that sum to the target.

def unique_pair(arr,target):
    # Edge case for array size less then 2 
    if len(arr) < 2:
        return []
    
    # we have to sort the array 
    arr.sort()

    # defining right and left pointers 
    left , right = 0, len(arr) - 1
    pair_op = []

    while left < right :

        sum = arr[left] + arr[right]

        if sum == target:
            pair_op.append((arr[left], arr[right]))

            left += 1
            right -= 1
            # To skip the duplicate value from left pointer, so that we get unique pair in output  
            while (left < right) and (arr[left] == arr[left-1]):
                left += 1
            
            # To skip the duplicate value from right pointer 
            while (left < right) and (arr[right] == arr[right + 1]):
                right += 1

        elif sum < target:
            left += 1
        else:
            right -= 1
        
    return pair_op

print(unique_pair([1, 1, 1, 1],2))

print(unique_pair([1,2,3,2,1,2],4))

print(unique_pair([1, 5, 7, -1, 5],6))
            
#Remove Duplicates