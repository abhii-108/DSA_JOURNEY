#Find the Smallest Divisor Given a Threshold
#You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'. Your task is to find the smallest positive integer divisor, 
#such that upon dividing all the elements of the given array by it, the sum of the division's result is less than or equal to the given threshold value

# Example 1:
# Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
# Result: 3
# Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
# The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor.
# Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer


import math

def helper(arr,mid):
    
    sum = 0 

    for i in arr:
        sum += math.ceil(i/mid)
    
    return sum

def smallest_divisor(arr, N, limit):
    # This is one of the edge case lets say there are only 6 element in array and given threshold is 2 if we divide each element of array by max val present in array
    # then its sum will always be less then threshold
    if N > limit: # N is length of array 
        return -1 
    

    left = 1 
    right = max(arr)

    res = -1


    while left <= right:
        
        mid = left + (right - left) // 2

        if helper(arr,mid) <= limit:
            res = mid 
            right = mid - 1
        else:
            left = mid + 1

    return res 


print(smallest_divisor([1,2,3,4,5],5,8))

