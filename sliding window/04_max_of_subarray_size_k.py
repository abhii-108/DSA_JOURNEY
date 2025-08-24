# #Sliding Window Maximum (Maximum of all subarrays of size K)
# Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k. The output should be an array of maximum values corresponding to each contiguous subarray.

# Input: arr[] = [5, 1, 3, 4, 2, 6], k = 1
# Output: [5, 1, 3, 4, 2, 6]
# Explanation: When k = 1, each element in the array is its own subarray, so the output is simply the same array.

# Input: arr[] = [1, 3, 2, 1, 7, 3], k = 3
# Output: [3, 3, 7, 7]

from collections import deque

def maxOfSubarrays(arr,k):
    mq = deque()
    (i,j) =(0,0)
    op = []

    while j < len(arr):

        while (len(mq) != 0) and (arr[j] > mq[0]): ## here we are checking with the latest element on the queue i.e [-1]
            mq.popleft()  # we are removing all the element from the queue which are smaller then arr[j] 

        mq.appendleft(arr[j])
        
        if (j-i+1) < k :
            j += 1
        
        elif (j-i+1) == k:
            #op.append(mq[0])

            op.append(mq[-1])

            if arr[i] == mq[-1]:
                #mq.popleft()
                mq.pop()
            i += 1
            j += 1
            
        
    return op 


print(maxOfSubarrays([1, 3,2, 1, 7, 3],3))         #[3, 3, 7, 7] if duplicate value in array then while condition is changed >= to > 
print(maxOfSubarrays([9,8,7,6], 4))                 # [9] (k = n)
print(maxOfSubarrays([3,2,1,0], 2))                 # [3,2,1] 
print(maxOfSubarrays([1,1,1,1], 2))                # [1,1,1] (all duplicates)
print(maxOfSubarrays([10, 5, 2, 7, 8, 7],3))
print(f"1 Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 8, Output: {maxOfSubarrays([1, 3, -1, -3, 5, 3, 6, 7], 8)}")
print(f"Input: arr = [9, 7, 2, 4, 6, 8, 2, 1, 5], k = 4, Output: {maxOfSubarrays([9, 7, 2, 4, 6, 8, 2, 1, 5], 4)}")

# from collections import deque

# def maxOfSubarrays(arr, k):
#     """
#     Finds the maximum element in every contiguous subarray of size k.
#     This uses a sliding window approach with a monotonic decreasing deque.

#     Args:
#         arr (list): The input list of numbers.
#         k (int): The size of the subarray (window).

#     Returns:
#         list: A list containing the maximum element for each subarray of size k.
#     """
#     n = len(arr)

#     # Hint: Handle edge cases where k is invalid or array is empty.
#     if k <= 0:
#         return [] # Invalid window size.
#     if n == 0:
#         return [] # Empty array.
#     if k > n:
#         # Hint: If k is larger than array length, return max of entire array
#         # if only one window is considered, or empty list if no such window exists.
#         # For 'all subarrays of size K', if K > N, no such subarray exists.
#         return [] 
#         # Alternatively, if the problem implies just one result for the whole array:
#         # return [max(arr)] if n > 0 else []

#     # mq (monotonic deque): Stores indices of elements in the current window.
#     # It maintains elements in decreasing order of their values.
#     # The front of the deque (mq[0]) will always store the index of the maximum
#     # element in the current window.
#     mq = deque()
    
#     # Pointers for the sliding window: i for start, j for end.
#     i = 0
#     j = 0
    
#     # op (output list): Stores the maximums of each window.
#     op = []

#     # --- Sliding Window Logic ---
#     # Hint: 'j' expands the window, 'i' shrinks it from the left.
#     while j < n:
#         # 1. Removal of elements smaller than arr[j] from deque's back
#         # Hint: Maintain monotonic decreasing order in mq.
#         # If arr[j] is greater than or equal to elements at deque's back,
#         # those elements can no longer be the maximum in any future window
#         # that includes arr[j]. So, pop them.
#         while mq and arr[j] >= arr[mq[-1]]: # Compare current element with value at index stored in deque's back
#             mq.pop() # Remove index of smaller/equal element from back of deque

#         # 2. Add current element's index to deque
#         # Hint: Always add the current element's index to the deque.
#         mq.append(j) # Add current element's index to the deque's back

#         # 3. Check window size and perform actions
#         # Hint: Expand window until its size is k.
#         if (j - i + 1) < k:
#             j += 1 # Window is still forming, just expand it.

#         # Hint: Once window size is k, process it.
#         elif (j - i + 1) == k:
#             # Current window is arr[i...j].
#             # The maximum element for this window is at the front of the deque.
#             # Hint: mq[0] contains the index of the maximum element. arr[mq[0]] is its value.
#             op.append(arr[mq[0]]) # Add the maximum of the current window to the result list.

#             # Remove element from the left (arr[i]) as window slides
#             # Hint: If the element leaving the window was the maximum (at mq[0]), remove it from deque.
#             if mq[0] == i: # Check if the maximum element's index matches the window's starting index.
#                 mq.popleft() # If yes, it's leaving the window, so remove it from the deque.

#             # Slide the window forward
#             i += 1 # Move window start
#             j += 1 # Move window end

#     return op

# # --- Test Cases ---
# print(f"Array: [1, 3, 2, 1, 7, 3], K: 3, Maxima: {maxOfSubarrays([1, 3, 2, 1, 7, 3], 3)}\nExpected: [3, 7, 7, 7]")
# print(f"Array: [10, 5, 2, 7, 8, 7], K: 3, Maxima: {maxOfSubarrays([10, 5, 2, 7, 8, 7], 3)}\nExpected: [10, 7, 8, 8]")
# print(f"Array: [1, 2, 3, 4, 5], K: 2, Maxima: {maxOfSubarrays([1, 2, 3, 4, 5], 2)}\nExpected: [2, 3, 4, 5]") # Monotonically increasing
# print(f"Array: [5, 4, 3, 2, 1], K: 3, Maxima: {maxOfSubarrays([5, 4, 3, 2, 1], 3)}\nExpected: [5, 4, 3]") # Monotonically decreasing
# print(f"Array: [1, 1, 1, 1, 1], K: 2, Maxima: {maxOfSubarrays([1, 1, 1, 1, 1], 2)}\nExpected: [1, 1, 1, 1]") # All equal
# print(f"Array: [4, 1, 3, 2, 5], K: 4, Maxima: {maxOfSubarrays([4, 1, 3, 2, 5], 4)}\nExpected: [4, 5]")
# print(f"Array: [1, 2, 3, 4, 5], K: 5, Maxima: {maxOfSubarrays([1, 2, 3, 4, 5], 5)}\nExpected: [5]") # K equals N

# # --- Edge Cases ---
# print(f"\n--- Edge Cases ---")
# print(f"Array: [], K: 3, Maxima: {maxOfSubarrays([], 3)}\nExpected: [] (Empty array)")
# print(f"Array: [1, 2, 3], K: 0, Maxima: {maxOfSubarrays([1, 2, 3], 0)}\nExpected: [] (Invalid K)")
# print(f"Array: [1, 2, 3], K: 5, Maxima: {maxOfSubarrays([1, 2, 3], 5)}\nExpected: [] (K > N)")
# print(f"Array: [7], K: 1, Maxima: {maxOfSubarrays([7], 1)}\nExpected: [7] (Single element array, K=1)")




###############################################################

# Program: Sliding Window Maximum
# Input: arr = [1, 3, 2, 1, 7, 3], k = 3
# Output: [3, 3, 7, 7]

# from collections import deque

# def maxOfSubarrays(arr, k):
#     # mq: A deque that stores elements from the current window.
#     # It's maintained in increasing order, so mq[-1] is the maximum.
#     mq = deque()
#     (i, j) = (0, 0)  # i: start of the window, j: end of the window
#     op = []          # op: list to store the maximums of each subarray

#     if k > len(arr) or k <= 0: # Handle edge case where k is invalid or larger than array length
#         return op

#     while j < len(arr):  # Iterate through the array with the 'j' pointer (end of window)

#         # Maintain deque: Remove elements from the left of mq that are smaller than arr[j].
#         # This ensures mq[0] is the smallest among the useful candidates after arr[j] is added.
#         # Essentially, elements in mq are kept in increasing order.
#         while (len(mq) != 0) and (arr[j] > mq[0]):
#             mq.popleft()  # Remove from the left (smallest end of sorted mq)

#         mq.appendleft(arr[j]) # Add current element arr[j] to the left of the deque.
#                               # mq will now be [arr[j], element >= arr[j], element >= previous, ...]
#                               # So, mq is sorted: mq[0] <= mq[1] <= ... <= mq[-1]

#         # If window size is less than k, expand the window
#         if (j - i + 1) < k:
#             j += 1
        
#         # If window size is equal to k, process the window
#         elif (j - i + 1) == k:
#             op.append(mq[-1]) # mq[-1] is the largest element in the current window's candidates

#             # Slide the window:
#             # If the element going out of the window (arr[i]) was the maximum (mq[-1]),
#             # remove it from the deque.
#             if arr[i] == mq[-1]:
#                 mq.pop()  # Removes from the right, where the maximum is stored

#             i += 1  # Move the start of the window forward
#             j += 1  # Move the end of the window forward
            
#     return op

# # Original Test Case
# print(f"Input: arr = [1, 3, 2, 1, 7, 3], k = 3, Output: {maxOfSubarrays([1, 3, 2, 1, 7, 3], 3)}")

# # Test Case 1: Increasing numbers
# print(f"Input: arr = [1, 2, 3, 4, 5], k = 2, Output: {maxOfSubarrays([1, 2, 3, 4, 5], 2)}")
# # Expected: [2, 3, 4, 5]

# # Test Case 2: Decreasing numbers
# print(f"Input: arr = [5, 4, 3, 2, 1], k = 2, Output: {maxOfSubarrays([5, 4, 3, 2, 1], 2)}")
# # Expected: [5, 4, 3, 2]

# # Test Case 3: All same numbers
# print(f"Input: arr = [1, 1, 1, 1, 1], k = 3, Output: {maxOfSubarrays([1, 1, 1, 1, 1], 3)}")
# # Expected: [1, 1, 1]

# # Test Case 4: Mixed numbers
# print(f"Input: arr = [9, 7, 2, 4, 6, 8, 2, 1, 5], k = 4, Output: {maxOfSubarrays([9, 7, 2, 4, 6, 8, 2, 1, 5], 4)}")
# # Expected: [9, 7, 6, 8, 8, 8] (Corrected: Max of [9,7,2,4] is 9. Max of [7,2,4,6] is 7. Max of [2,4,6,8] is 8. Max of [4,6,8,2] is 8. Max of [6,8,2,1] is 8. Max of [8,2,1,5] is 8.)
# # Let's re-verify output for [9, 7, 2, 4, 6, 8, 2, 1, 5], k=4
# # [9,7,2,4] -> 9
# # [7,2,4,6] -> 7
# # [2,4,6,8] -> 8
# # [4,6,8,2] -> 8
# # [6,8,2,1] -> 8
# # [8,2,1,5] -> 8
# # Expected: [9, 7, 8, 8, 8, 8] -- The original code output [3,3,7,7] was for [1,3,2,1,7,3], k=3
# # The provided solution's logic when run with [9, 7, 2, 4, 6, 8, 2, 1, 5], k=4 should be:
# # Output of maxOfSubarrays([9, 7, 2, 4, 6, 8, 2, 1, 5], 4) actually is [9, 7, 8, 8, 8, 8] - this is correct.

# # Edge Case 1: k = 1
# print(f"Input: arr = [1, 3, 2], k = 1, Output: {maxOfSubarrays([1, 3, 2], 1)}")
# # Expected: [1, 3, 2]

# # Edge Case 2: k = length of array
# print(f"Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 8, Output: {maxOfSubarrays([1, 3, -1, -3, 5, 3, 6, 7], 8)}")
# # Expected: [7]

# # Edge Case 3: Empty array
# print(f"Input: arr = [], k = 3, Output: {maxOfSubarrays([], 3)}")
# # Expected: []

# # Edge Case 4: k > length of array
# print(f"Input: arr = [1, 2], k = 3, Output: {maxOfSubarrays([1, 2], 3)}")
# # Expected: []

# # Edge Case 5: Array with negative numbers
# print(f"Input: arr = [-1, -3, -2, -5], k = 2, Output: {maxOfSubarrays([-1, -3, -2, -5], 2)}")
# # Expected: [-1, -2, -2]