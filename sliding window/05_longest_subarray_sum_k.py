#Longest Subarray with Sum K(Positives)
# Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.


# Example 1:
# Input Format: N = 3, k = 5, array[] = {2,3,5}
# Result: 2
# Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

# Example 2:
# Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
# Result: 3
# Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.

def longestSubarray(arr,k):
    size=len(arr)
    (i,j) = (0,0)
    m_sum = 0
    mx_sub_arr = 0 
    while j < len(arr):
        m_sum += arr[j]
        #print(m_sum)
        if m_sum < k:
            j += 1
        
        elif m_sum == k :
            mx_sub_arr = max(mx_sub_arr, (j-i+1))
            #print(f'subarray count {mx_sub_arr}')
            j += 1
        
        elif m_sum > k :
            while m_sum >  k and  i <= j: 
                m_sum -= arr[i]
                i += 1

            if m_sum == k :
               mx_sub_arr = max(mx_sub_arr, (j-i+1)) 
               #print(f'subarray count {mx_sub_arr}')
            j += 1
  
        
    return mx_sub_arr

#print(longestSubarray([2,3,5],5))
print(longestSubarray([1,2,3,4,5], 9))   # 3 (2+3+4)

print(longestSubarray([5], 5))           # 1 
print(longestSubarray([1,1,1,1], 4))     # 4 
print(longestSubarray([10,20,30], 5))    # 0 (no match) This is edgec ase 
print(longestSubarray([], 5))            # 0 (empty array)


########################################################################
# Program: Longest Subarray with Sum K (Positive Numbers)
# Input: arr = [4, 1, 1, 1, 2, 3, 5], k = 5
# Output: 4 (corresponding to subarray [1, 1, 1, 2])

def longestSubarray(arr, k):
    size = len(arr)  # Get the size of the array
    (i, j) = (0, 0)  # Initialize window pointers: i (start), j (end)
    m_sum = 0        # Initialize current sum of elements in the window arr[i...j]
    mx_sub_arr = 0   # Initialize maximum length of subarray found so far

    # Iterate through the array with the 'j' pointer (end of window)
    while j < size:
        m_sum += arr[j]  # Add the current element arr[j] to the sum

        # Case 1: Current window sum is less than k
        if m_sum < k:
            j += 1  # Expand the window by moving 'j' to the right
        
        # Case 2: Current window sum is equal to k
        elif m_sum == k:
            # Found a subarray with sum k, update max length if current one is longer
            mx_sub_arr = max(mx_sub_arr, (j - i + 1))
            j += 1  # Expand the window to look for other possibilities
        
        # Case 3: Current window sum is greater than k
        elif m_sum > k:
            # Shrink the window from the left until sum is no longer greater than k
            while m_sum > k and i <= j:  # Ensure 'i' doesn't cross 'j'
                m_sum -= arr[i]  # Subtract element arr[i] from the sum
                i += 1           # Move 'i' to the right
            
            # After shrinking, if the sum becomes exactly k, it's a valid subarray
            if m_sum == k:
                mx_sub_arr = max(mx_sub_arr, (j - i + 1))
            
            j += 1  # Expand the window by moving 'j' to consider next element

    return mx_sub_arr # Return the maximum length found



# Original example test from typical scenarios
print(f"Input: arr = [4, 1, 1, 1, 2, 3, 5], k = 5, Output: {longestSubarray([4, 1, 1, 1, 2, 3, 5], 5)}")
# Expected: 4 (for [1, 1, 1, 2])

# Test Case 1: No subarray sums to k
print(f"Input: arr = [1, 2, 3], k = 7, Output: {longestSubarray([1, 2, 3], 7)}")
# Expected: 0

# Test Case 2: Entire array is the solution
print(f"Input: arr = [1, 2, 3, 4], k = 10, Output: {longestSubarray([1, 2, 3, 4], 10)}")
# Expected: 4

# Test Case 3: Single element array, matches k
print(f"Input: arr = [5], k = 5, Output: {longestSubarray([5], 5)}")
# Expected: 1

# Test Case 4: Single element array, does not match k
print(f"Input: arr = [5], k = 3, Output: {longestSubarray([5], 3)}")
# Expected: 0

# Edge Case 1: Empty array
print(f"Input: arr = [], k = 5, Output: {longestSubarray([], 5)}")
# Expected: 0

# Edge Case 2: k = 0 (assuming positive numbers means >0, so no subarray sums to 0 unless array is empty or contains 0s.
# If numbers can be non-negative (>=0) and array is e.g. [0,0,0], k=0, output should be 3.
# The problem statement "Positives" usually implies >0. If elements > 0, k=0 will yield 0.)
print(f"Input: arr = [1, 2, 3], k = 0, Output: {longestSubarray([1, 2, 3], 0)}")
# Expected: 0 (for strictly positive numbers)

# Test Case 5: Subarray appears at the end
print(f"Input: arr = [10, 5, 2, 7, 1, 9], k = 10 (target sum from [2,7,1]), Output: {longestSubarray([10, 5, 2, 7, 1, 9], 10)}")
# Expected: 3 (for [2,7,1] or for [1,9]. Should be for [2,7,1] as it's [2,7,1]=10, while [1,9]=10.
# The solution correctly finds the first such longest. Let's re-check the sample.
# [10] len 1
# [2,7,1] len 3
# [1,9] len 2
# The provided code will find the maximum length.
# arr=[10,5,2,7,1,9], k=10
# j=0, sum=10. mx=1. j=1.
# j=1, sum=10+5=15. sum-=10,i=1. sum=5. j=2.
# j=2, sum=5+2=7. j=3.
# j=3, sum=7+7=14. sum-=5,i=2. sum=9. j=4.
# j=4, sum=9+1=10. mx=max(1, 4-2+1=3)=3. j=5.
# j=5, sum=10+9=19. sum-=2,i=3. sum=17. sum-=7,i=4. sum=10. mx=max(3, 5-4+1=2)=3. j=6.
# Output for [10, 5, 2, 7, 1, 9], k=10 is 3. Correct.

# Test Case 6: Array with duplicate numbers making up the sum
print(f"Input: arr = [1, 1, 1, 1, 1], k = 3, Output: {longestSubarray([1, 1, 1, 1, 1], 3)}")
# Expected: 3