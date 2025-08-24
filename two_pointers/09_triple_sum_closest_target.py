# Triplet Sum Closest to Target: Find a triplet [a, b, c] whose sum is closest to a given target.

# Input: arr[] = [-1, 2, 2, 4], target = 4
# Output: 5
# Explanation: All possible triplets


# Input: arr[] = [1, 10, 4, 5], target = 10
# Output: 10
# Explanation: All possible triplets



def triple_sum_close(arr,target):
    #Edge case if len less then 3 
    if len(arr) < 3:
        return []

    arr.sort()
    res = 0
    min_diff = float('inf')
    # declare variable n which will store the lenght of array 
    n = len(arr)

    for i in range(0,n-2):
        
        left = i+1
        right = n-1

        while left < right:

            curr_sum = arr[i] + arr[left] + arr[right]

            if abs(curr_sum - target) < min_diff:
                min_diff = abs(curr_sum - target)
                res = curr_sum 
            
            elif abs(curr_sum - target) == min_diff:
                res = max(res,curr_sum)
            
            if curr_sum > target:
                right -= 1
            else:
                left += 1

    return res 

print(triple_sum_close([-1, 2, 2, 4],4))









