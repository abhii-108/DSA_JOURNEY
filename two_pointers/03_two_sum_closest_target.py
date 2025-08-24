#Two Sum Closest to Target: Find a pair whose sum is closest to the target.
# Input: arr[] = [10, 30, 20, 5], target = 25
# Output: [5, 20]
# Explanation: Out of all the pairs, [22, 30] has sum = 25 which is closest to 25.

# Input: arr[] = [5, 2, 7, 1, 4], target = 10
# Output: [2, 7]
# Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence,[2, 7] has maximum absolute difference and closest to target.

# Input: arr[] = [10], target = 10
# Output: []
# Explanation: As the input array has only 1 element, return an empty array.


def two_sum_closest_prod(arr,target):
    #Handling edge case for array size smaller then 1
    if len(arr) < 1:
        return []
    
    ## We have to sort the array 
    arr.sort()
    min_diff = float('inf')
    op_ixd = [-1,-1]
    left, right = 0, len(arr) - 1 

    while left < right:
        curr_sum = arr[left] + arr[right]

        # compare the current min with pervious min
        if abs(curr_sum - target) < min_diff:
            op_ixd = [arr[left], arr[right]]
            min_diff = abs(curr_sum - target)

        elif abs(curr_sum - target) == 0:
            return [arr[left], arr[right]]
        

        if abs(curr_sum - target) == min_diff:
            if (arr[right] - arr[left]) >  (op_ixd[1] - op_ixd[0]):
                op_ixd = [arr[left], arr[right]]

        
        if curr_sum <= target:
            left += 1
        else:
            right -= 1

    return op_ixd


print(two_sum_closest_prod([5,2,7,1,4],10))          
        















#########################################################################################

def two_sum_closest(arr,target):
    # edge case condition if arr len is less 1 or less 
    if len(arr) <= 1:
        return []
    
    # now we have to sort the array for using two pointer 
    arr.sort()

    # Now we will define two pointers left and right which will iterate over array 
    left , right = 0 , len(arr)-1

    # we will define min diff value to positive infinity 
    min_diff = float('inf') 

    # define variable which will be used to return the output 
    closest_pair = []

    # Now we will iterate over array using our left and right pointer and make a condition that left should not crossover right 
    while left < right:
        # Get current sum of min and max value of array which is present at left and right pointer of array 
        curr_sum = arr[left] + arr[right]
        curr_diff = abs(curr_sum - target)

        if curr_diff < min_diff:
            min_diff = curr_diff
            closest_pair = [arr[left], arr[right]]

            if curr_sum < target:
                left += 1
            else:
                right -= 1
        else:
            return [arr[left],arr[right]]
    
    return closest_pair


   

# print(two_sum_closest([10, 30, 20, 5],25))
# print(two_sum_closest([5, 2, 7, 1, 4],10))
# print(two_sum_closest([5],10))


##################################### 