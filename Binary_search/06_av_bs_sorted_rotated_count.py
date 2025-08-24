#Rotation Count in a Rotated Sorted array

## extra questions 
# Search in a Sorted and Rotated Array
# Check if an array is sorted and rotated using Binary Search

def rotated_count(arr):
    left, right = 0, len(arr)-1



    while left <= right:
        if arr[left] <= arr[right]:
            return left

        mid = left + (right - left) // 2
        next = (mid+1) % len(arr)
        prev = (mid-1+len(arr)) % len(arr)

        #print(f'prev -->{prev} mid-->{mid} next-->{next} ')

        if (arr[mid] <= arr[next]) and (arr[mid] <= arr[prev]):
            return mid 
        
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1  
        
    return 0


print(rotated_count([15, 18, 2, 3, 6, 12]))

print(rotated_count([7, 9, 11, 12, 15]))

print(rotated_count([4,5,6,7,0,1,2]))


#############################################################
# Program: Rotation Count in a Rotated Sorted Array

def rotated_count(arr):
    """
    Finds the number of times a sorted array has been rotated.
    This is equivalent to finding the index of the minimum element.

    Args:
        arr (list): A list of integers representing a rotated sorted array.

    Returns:
        int: The number of rotations (index of the minimum element).
             Returns 0 if the array is not rotated (already sorted).
    """

    n = len(arr)
    # Hint: Handle empty or single-element arrays immediately.
    # An array with 0 or 1 element cannot be rotated meaningfully.
    if n == 0:
        return 0
    if n == 1:
        return 0 # A single element array is considered 0 rotations.

    # Hint: Initialize left and right pointers for binary search.
    # 'left' is the start index, 'right' is the end index.
    left, right = 0, n - 1

    # Hint: Binary search loop condition.
    # The loop continues as long as left <= right to ensure all possibilities are checked.
    while left <= right:
        # Hint: If the subarray is already sorted (no rotation in this segment),
        # the minimum element is at 'left'. This handles the case where the
        # entire array is not rotated at all, or a sorted subsegment is found.
        if arr[left] <= arr[right]:
            return left # If this condition is met, 'left' points to the minimum element.

        # Hint: Calculate the middle index to divide the search space.
        # Using (right - left) // 2 avoids potential integer overflow for very large arrays.
        mid = left + (right - left) // 2

        # Hint: Calculate 'next' and 'prev' indices in a circular manner.
        # These are used to check if 'mid' is the minimum element (the "pivot").
        # 'next' is (mid + 1) % n for circular array.
        # 'prev' is (mid - 1 + n) % n for circular array to handle mid=0 case.
        next_idx = (mid + 1) % n
        prev_idx = (mid - 1 + n) % n

        # Hint: Check if 'mid' is the minimum element (the pivot point).
        # A minimum element will be smaller than both its 'next' and 'prev' neighbors.
        # This is the rotation point.
        if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
            return mid # 'mid' is the index of the minimum element, which is the rotation count.

        # Hint: Decide which half to search based on whether the 'mid' element
        # is in the left sorted part or the right sorted part.
        # If arr[mid] is greater than arr[left], it means the left half
        # (from 'left' to 'mid') is sorted, so the minimum must be in the right half.
        if arr[mid] >= arr[left]: # Current 'mid' is in the "left sorted part" (before the pivot)
            left = mid + 1 # So, discard left half and search in the right half.
        else: # arr[mid] < arr[left] implies 'mid' is in the "right sorted part" (after the pivot)
              # and the pivot must be in the left half including 'mid'.
            right = mid - 1 # So, discard right half and search in the left half.

    # Hint: This return is a fallback and generally should not be reached if the array
    # is guaranteed to be a rotated sorted array and non-empty.
    # It signifies 0 rotations if loop completes without finding a pivot (e.g., empty array or non-rotated handled by arr[left] <= arr[right]).
    return 0

# --- Test Cases ---

print("--- Test Cases ---")

# Test Case 1: Standard rotation
arr1 = [15, 18, 2, 3, 6, 12]
# Expected Output: 2 (min element is 2 at index 2)
print(f"Input: {arr1}")
print(f"Output: {rotated_count(arr1)}")
print("-" * 20)

# Test Case 2: Array not rotated (already sorted)
arr2 = [7, 9, 11, 12, 15]
# Expected Output: 0 (min element is 7 at index 0)
print(f"Input: {arr2}")
print(f"Output: {rotated_count(arr2)}") # This was the problematic case for your original code.
print("-" * 20)

# Test Case 3: Array rotated such that the minimum is at the end
arr3 = [3, 4, 5, 1, 2]
# Expected Output: 3 (min element is 1 at index 3)
print(f"Input: {arr3}")
print(f"Output: {rotated_count(arr3)}")
print("-" * 20)

# Test Case 4: Array with duplicates (can be tricky for finding specific element, but for min it's okay)
# Note: While this code finds the *first* minimum, if multiple minimums exist,
# it finds the index of one of them. For rotation count, it's just the index.
arr4 = [3, 3, 1, 2, 3]
# Expected Output: 2 (min element is 1 at index 2)
print(f"Input: {arr4}")
print(f"Output: {rotated_count(arr4)}")
print("-" * 20)

# Edge Case 1: Single element array
arr_e1 = [5]
# Expected Output: 0
print(f"Input (Edge Case 1 - Single element): {arr_e1}")
print(f"Output: {rotated_count(arr_e1)}")
print("-" * 20)

# Edge Case 2: Array with two elements, rotated
arr_e2 = [5, 1]
# Expected Output: 1
print(f"Input (Edge Case 2 - Two elements, rotated): {arr_e2}")
print(f"Output: {rotated_count(arr_e2)}")
print("-" * 20)

# Edge Case 3: Array with two elements, not rotated
arr_e3 = [1, 5]
# Expected Output: 0
print(f"Input (Edge Case 3 - Two elements, not rotated): {arr_e3}")
print(f"Output: {rotated_count(arr_e3)}")
print("-" * 20)

# Edge Case 4: All elements are the same
arr_e4 = [7, 7, 7, 7, 7]
# Expected Output: 0 (or 0 as it's considered not rotated)
print(f"Input (Edge Case 4 - All same elements): {arr_e4}")
print(f"Output: {rotated_count(arr_e4)}")
print("-" * 20)

print(rotated_count([4,5,6,7,0,1,2]))