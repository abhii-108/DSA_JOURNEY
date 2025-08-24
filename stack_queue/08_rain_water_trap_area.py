#Trapping Rain Water Problem - Tutorial with Illustrations

#Trapping Rainwater Problem states that given an array of n non-negative integers arr[] representing an elevation map where the width of each bar is 1, compute how much water it can trap after rain.

# Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
# Output: 10
# Explanation: The expected rainwater to be trapped is shown in the above image.

# Input: arr[] = [3, 0, 2, 0, 4]
# Output: 7
# Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

# Input: arr[] = [1, 2, 3, 4]
# Output: 0
# Explanation: We cannot trap water as there is no height bound on both sides



def rain_water_trap_area(arr):
    size = len(arr)
    lhb = [0] * size     # lhb[i] will store the highest bar to the left of i (including i)

    rhb = [0] * size     # rhb[i] will store the highest bar to the right of i (including i)

    # Fill in the first and last index with the height at that point
    lhb[0] = arr[0]
    rhb[size-1] = arr[size-1]

    # Fill in lhb from left to right
    # Fill in rhb from right to left
    i = 1
    j = size-2 

    while i < size and j >= 0:
        
        lhb[i] = max(lhb[i-1], arr[i])
        rhb[j] = max(rhb[j+1], arr[j])

        i += 1
        j -= 1
    
    # Now compute trapped water by using:
    # water at position i = min(lhb[i], rhb[i]) - arr[i]
        
    sum = 0 
    for x in range(0,size):
        sum += min(lhb[x], rhb[x]) - arr[x]
    
    return sum 

print(rain_water_trap_area([3, 0, 1, 0, 4, 0, 2]))
print(rain_water_trap_area([3, 0, 2, 0, 4]))
print(rain_water_trap_area([1, 2, 3, 4]))





# """
# Trapping Rainwater Calculator
# -----------------------------
# Problem: Calculate total rainwater trapped between bars given their heights.
# Algorithm: Dynamic Programming with Left/Right Boundary Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)
# """

# def rain_water_trap_area(elevation_map):
#     """Calculate trapped rainwater using boundary tracking"""
#     n = len(elevation_map)
#     if n < 3:  # Need at least 3 bars to trap water
#         return 0
    
#     # Initialize boundary arrays
#     left_max = [0] * n
#     right_max = [0] * n
#     total_water = 0

#     # Track maximum height from left
#     left_max[0] = elevation_map[0]
#     for i in range(1, n):
#         left_max[i] = max(left_max[i-1], elevation_map[i])
    
#     # Track maximum height from right
#     right_max[n-1] = elevation_map[n-1]
#     for i in range(n-2, -1, -1):
#         right_max[i] = max(right_max[i+1], elevation_map[i])
    
#     # Calculate water at each position
#     for i in range(n):
#         # Water level = min of left/right boundaries
#         water_level = min(left_max[i], right_max[i])
        
#         # Water trapped = level minus current height
#         water_here = water_level - elevation_map[i]
        
#         # Only add positive values
#         if water_here > 0:
#             total_water += water_here
    
#     return total_water


#######################################################################


# def rain_water_trap_area(arr):
#     """
#     Calculates the total amount of rainwater that can be trapped between buildings.

#     Args:
#         arr: A list of non-negative integers representing the height of buildings.

#     Returns:
#         The total amount of trapped rainwater.
#     """
#     size = len(arr)
#     # Hint: If the array has less than 3 elements, no water can be trapped.
#     if size < 3:
#         return 0

#     # lhb (left_highest_bar): Stores the maximum height of a bar to the left of the current bar, including itself.
#     lhb = [0] * size
#     # rhb (right_highest_bar): Stores the maximum height of a bar to the right of the current bar, including itself.
#     rhb = [0] * size

#     # Initialize the first element of lhb with the height of the first building.
#     lhb[0] = arr[0]
#     # Initialize the last element of rhb with the height of the last building.
#     rhb[size - 1] = arr[size - 1]

#     i = 1  # Pointer for iterating from left to right for lhb
#     j = size - 2  # Pointer for iterating from right to left for rhb

#     # Hint: Populate lhb and rhb arrays.
#     # lhb[i] will store the maximum height encountered from index 0 to i.
#     # rhb[j] will store the maximum height encountered from index (size-1) to j.
#     while i < size and j >= 0:
#         # Calculate the maximum height from the left up to the current index 'i'.
#         # It's either the previous max (lhb[i-1]) or the current building height (arr[i]).
#         lhb[i] = max(lhb[i - 1], arr[i])
#         # Calculate the maximum height from the right up to the current index 'j'.
#         # It's either the previous max (rhb[j+1]) or the current building height (arr[j]).
#         rhb[j] = max(rhb[j + 1], arr[j])

#         i += 1  # Move left pointer to the right
#         j -= 1  # Move right pointer to the left

#     sum_trapped_water = 0  # Initialize variable to store the total trapped water.

#     # Hint: Calculate trapped water at each position.
#     # The water trapped at a specific position 'x' is determined by the minimum of its left and right boundaries
#     # minus the height of the building at that position.
#     for x in range(0, size):
#         # Water at current position = min(max_left_height, max_right_height) - current_building_height
#         sum_trapped_water += min(lhb[x], rhb[x]) - arr[x]

#     return sum_trapped_water

# # --- Test Cases ---

# print(f"Input: [3, 0, 1, 0, 4, 0, 2], Output: {rain_water_trap_area([3, 0, 1, 0, 4, 0, 2])}")  # Expected: 8
# print(f"Input: [3, 0, 2, 0, 4], Output: {rain_water_trap_area([3, 0, 2, 0, 4])}")      # Expected: 7
# print(f"Input: [1, 2, 3, 4], Output: {rain_water_trap_area([1, 2, 3, 4])}")          # Expected: 0 (Monotonically increasing)
# print(f"Input: [4, 3, 2, 1], Output: {rain_water_trap_area([4, 3, 2, 1])}")          # Expected: 0 (Monotonically decreasing)
# print(f"Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], Output: {rain_water_trap_area([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])}") # Expected: 6
# print(f"Input: [], Output: {rain_water_trap_area([])}")                             # Expected: 0 (Edge case: empty array)
# print(f"Input: [5], Output: {rain_water_trap_area([5])}")                           # Expected: 0 (Edge case: single element array)
# print(f"Input: [5, 5], Output: {rain_water_trap_area([5, 5])}")                       # Expected: 0 (Edge case: two elements)
# print(f"Input: [0, 0, 0, 0, 0], Output: {rain_water_trap_area([0, 0, 0, 0, 0])}")     # Expected: 0 (All zeros)
# print(f"Input: [7, 0, 0, 0, 7], Output: {rain_water_trap_area([7, 0, 0, 0, 7])}")     # Expected: 21 (Large pool)


# Here's a detailed breakdown:

# Initialization and Edge Cases:

# size = len(arr): Get the number of buildings.
# if size < 3: return 0: This is a crucial edge case. If there are fewer than three buildings, no water can be trapped. You need at least two "walls" and a "dip" in between.
# Creating lhb (Left Highest Bar) Array:

# lhb = [0] * size: Create an array of the same size as arr, initialized with zeros. This array will store the maximum height of a building encountered so far from the left, up to the current index (inclusive).
# lhb[0] = arr[0]: The first element of lhb is simply the height of the first building, as there's nothing to its left.
# The while loop, specifically lhb[i] = max(lhb[i-1], arr[i]), iterates from the second element (i=1) to the end. For each position i, lhb[i] is set to the maximum of lhb[i-1] (the maximum height encountered before i) and arr[i] (the height of the current building). This ensures lhb[i] always holds the tallest building from index 0 to i.
# Creating rhb (Right Highest Bar) Array:

# rhb = [0] * size: Similar to lhb, this array will store the maximum height of a building encountered so far from the right, up to the current index (inclusive).
# rhb[size-1] = arr[size-1]: The last element of rhb is the height of the last building.
# The while loop, specifically rhb[j] = max(rhb[j+1], arr[j]), iterates from the second to last element (j=size-2) down to the beginning. For each position j, rhb[j] is set to the maximum of rhb[j+1] (the maximum height encountered after j) and arr[j] (the height of the current building). This ensures rhb[j] always holds the tallest building from index size-1 to j.
# Calculating Trapped Water:

# sum_trapped_water = 0: Initialize a variable to accumulate the total trapped water.
# for x in range(0, size):: Iterate through each position x in the array.
# water_at_x = min(lhb[x], rhb[x]) - arr[x]: For each position x, the amount of water that can be trapped above arr[x] is determined by the shorter of the two surrounding "walls" (lhb[x] and rhb[x]). From this minimum height, we subtract the actual height of the building at arr[x]. If arr[x] is taller than or equal to min(lhb[x], rhb[x]), water_at_x will be 0 or negative, meaning no water can be trapped there.
# sum_trapped_water += water_at_x: Add the water trapped at the current position to the total.
# Return sum_trapped_water: The function returns the final accumulated sum.