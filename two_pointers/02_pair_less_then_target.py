#Count Pairs With Sum Less Than Target
# Given an array arr[] and an integer target, the task is to find the count of pairs whose sum is strictly less than given target.

# Input: arr[] = [7, 2, 5, 3], target = 8
# Output: 2 
# Explanation: There are 2 pairs with sum less than 8: (2, 5) and (2, 3). 

# Input: arr[] = [5, 2, 3, 2, 4, 1], target = 5
# Output: 4
# Explanation: There are 4 pairs whose sum is less than 5: (2, 2), (2, 1), (3, 1) and (2, 1).

# Input: arr[] = [2, 1, 8, 3, 4, 7, 6, 5], target = 7
# Output: 6
# Explanation: There are 6 pairs whose sum is less than 7: (2, 1), (2, 3), (2, 4), (1, 3), (1, 4) and (1, 5).

def pair_count_less_sum(arr,target):
    #Edge case if array size is less then or equal to 1
    if len(arr) <= 1:
        return []
    
    arr.sort() ## Sorting the array for using two pointer technique 

    left, right = 0 , len(arr)-1

    pair_count = 0 

    while left < right:

        pair_sum = arr[left] + arr[right]

        if pair_sum < target:
            pair_count = pair_count + (right - left)
            # Incrementing both left and right pointer as we have counted all the possible pair which will be less then target sum. 
            left += 1 
            right -= 1 
            # writing while condition for left pointer if duplicate value are present then we have to skip it 
            while left < right and arr[left] == arr[left - 1]:
                left += 1 
            
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        else:
            right -= 1 

    return pair_count

print(pair_count_less_sum([5, 2, 3, 2, 4, 1],5))
print(pair_count_less_sum([2, 1, 8, 3, 4, 7, 6, 5],7))

#[1,2,3,2,1,2]

