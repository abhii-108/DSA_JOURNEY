# Maximum size rectangle binary sub-matrix with all 1s

# Given a 2d binary matrix mat[][], the task is to find the maximum size rectangle binary-sub-matrix with all 1's. 

# Input: 
# mat = [
#    [0, 1, 1, 0],
#    [1, 1, 1, 1],
#    [1, 1, 1, 1],
#    [1, 1, 0, 0] ]

# Output : 8
# Explanation : The largest rectangle with only 1's is from (1, 0) to (2, 3) which is
# [1, 1, 1, 1]
# [1, 1, 1, 1]

# Input: 
# mat = [
#    [0, 1, 1],
#    [1, 1, 1],
#    [0, 1, 1] ]

# Output: 6
# Explanation: The largest rectangle with only 1's is from (0, 1) to (2, 2) which is
# [1, 1]
# [1, 1]
# [1, 1]

from collections import deque


def max_area_histogram(arr):

    stack = deque()

    op_nsl = [0] * len(arr)
    op_nsr = [0] * len(arr)


    for i in range(0, len(arr)):

        if len(stack) == 0:
            op_nsl[i] = -1

        
        elif stack[-1][1] < arr[i]:
            op_nsl[i]=stack[-1][0]
        
        else:

            while (len(stack) != 0) and (stack[-1][1] >= arr[i]):
                stack.pop()
            
            if len(stack) == 0:
                op_nsl[i] = -1
            else:
                op_nsl[i]=stack[-1][0]
        
        stack.append([i,arr[i]])
    

    stack.clear()

    for i in range(len(arr)-1,-1,-1):

        if len(stack) == 0:
            op_nsr[i] = len(arr)

        elif stack[-1][1] < arr[i]:
            op_nsr[i] = stack[-1][0]
        
        else:
            while (len(stack) != 0 ) and (stack[-1][1] >= arr[i]):
                stack.pop()
            
            if len(stack) == 0:
                op_nsr[i] = len(arr)
            else:
                op_nsr[i] = stack[-1][0]

        stack.append([i,arr[i]])


    max_area_hist = 0
    print(end='\n')
    for i in range(0, len(arr)):
        print(f'{op_nsr[i] - op_nsl[i] - 1}' ,end='-->')
        max_area_index = (op_nsr[i] - op_nsl[i] - 1) * arr[i]

        max_area_hist = max(max_area_hist, max_area_index)
    
    return max_area_hist




# print(max_area_histogram([6,2,5,4,5,1,6])) 
# print(max_area_histogram([1,1,1,1])) 


def max_area_matrix(mat):


    rows = len(mat)
    
    cols = len(mat[0]) if rows > 0 else 0

    one_d = [0] * cols ##  above rows & cols are used to get the length of cols in an matrix which can be use to create one d array 
    

    max_area = 0
    max_area_matrix = 0 
    for row in mat:

        for i, j in enumerate(row):

            if j == 0:
                one_d[i] = 0
            else:
                one_d[i] += j 

        #print(max_area_histogram(one_d) )  
        max_area = max_area_histogram(one_d)
        max_area_matrix = max(max_area_matrix, max_area)
    
    return max_area_matrix


print(max_area_matrix([
   [0, 1, 1, 0],
   [1, 1, 1, 1],
   [1, 1, 1, 1],
   [1, 1, 0, 0] ]
))


print(max_area_matrix([
   [0, 1, 1],
   [1, 1, 1],
   [0, 1, 1] ]))



######################################################################################################################

from collections import deque

def max_area_histogram(heights):
    """
    Calculates the maximum rectangular area in a histogram.
    This function finds the Next Smaller Left (NSL) and Next Smaller Right (NSR)
    for each bar and uses them to calculate the width of the rectangle for each bar.

    Args:
        heights: A list of integers representing the heights of bars in a histogram.

    Returns:
        The maximum area of a rectangle that can be formed within the histogram.
    """
    n = len(heights)
    # Hint: Handle empty histogram or single bar cases.
    if n == 0:
        return 0
    if n == 1:
        return heights[0]

    stack = deque()  # Monotonic stack to store (index, height) pairs.
                     # It maintains elements in increasing order of height.

    op_nsl = [0] * n  # Array to store the index of the Next Smaller Element to the Left for each bar.
    op_nsr = [0] * n  # Array to store the index of the Next Smaller Element to the Right for each bar.

    # --- Step 1: Calculate Next Smaller Left (NSL) for each bar ---
    # Hint: Iterate from left to right. Maintain a monotonic increasing stack.
    # When a bar is encountered, pop elements from stack that are greater than or equal to current bar.
    # The top of stack (if not empty) will be the NSL.
    for i in range(n):
        while stack and stack[-1][1] >= heights[i]:
            stack.pop() # Pop elements taller or equal to current bar, as they can't be NSL.

        if not stack:
            op_nsl[i] = -1 # No smaller element to the left (boundary condition).
        else:
            op_nsl[i] = stack[-1][0] # The top of stack is the NSL.

        stack.append([i, heights[i]]) # Push current bar's index and height onto the stack.

    stack.clear() # Clear the stack for the next pass (NSR calculation).

    # --- Step 2: Calculate Next Smaller Right (NSR) for each bar ---
    # Hint: Iterate from right to left. Maintain a monotonic increasing stack.
    # Similar logic to NSL, but for the right side.
    for i in range(n - 1, -1, -1):
        while stack and stack[-1][1] >= heights[i]:
            stack.pop() # Pop elements taller or equal to current bar, as they can't be NSR.

        if not stack:
            op_nsr[i] = n # No smaller element to the right (boundary condition, use array length).
        else:
            op_nsr[i] = stack[-1][0] # The top of stack is the NSR.

        stack.append([i, heights[i]]) # Push current bar's index and height onto the stack.

    max_area_hist = 0 # Initialize maximum area for the histogram.

    # --- Step 3: Calculate area for each bar and find the maximum ---
    # Hint: For each bar, the width of the largest rectangle it can form is (NSR index - NSL index - 1).
    # The height is the bar's own height.
    for i in range(n):
        width = op_nsr[i] - op_nsl[i] - 1 # Calculate the width based on NSL and NSR indices.
        current_area = width * heights[i]  # Calculate the area for the rectangle with current bar's height.
        max_area_hist = max(max_area_hist, current_area) # Update overall maximum area.

    return max_area_hist


def max_area_matrix(mat):
    """
    Calculates the maximum rectangular area of a sub-matrix with all 1s.
    This function converts each row of the binary matrix into a histogram
    and uses max_area_histogram to find the largest area.

    Args:
        mat: A list of lists (binary matrix) containing 0s and 1s.

    Returns:
        The maximum area of a rectangle with all 1s.
    """
    rows = len(mat)
    cols = len(mat[0]) if rows > 0 else 0 # Handle empty matrix case.

    # Hint: If the matrix is empty, return 0.
    if rows == 0 or cols == 0:
        return 0

    # one_d: Represents the current histogram heights for the accumulated 1s from previous rows.
    # Initialize with the first row of the matrix.
    one_d = [0] * cols
    for j in range(cols):
        one_d[j] = mat[0][j] # Initialize with the first row.

    # max_area_matrix: Stores the overall maximum area found so far.
    # Start with the max area from the first row's histogram.
    max_area_matrix = max_area_histogram(one_d)

    # Hint: Iterate through the remaining rows. For each row, update the histogram 'one_d'.
    # If an element is 0, reset its corresponding height in 'one_d' to 0.
    # If an element is 1, increment its height in 'one_d' (accumulating 1s from above).
    for r in range(1, rows): # Start from the second row.
        for c in range(cols):
            if mat[r][c] == 0:
                one_d[c] = 0 # Reset height if current cell is 0.
            else:
                one_d[c] += 1 # Accumulate height if current cell is 1.

        # Calculate the maximum area for the current histogram (current row's accumulated heights).
        current_row_max_area = max_area_histogram(one_d)
        # Update the overall maximum area.
        max_area_matrix = max(max_area_matrix, current_row_max_area)

    return max_area_matrix

# --- Test Cases ---

# print(f"Matrix 1: \n[0, 1, 1, 0],\n[1, 1, 1, 1],\n[1, 1, 1, 1],\n[1, 1, 0, 0]
# Output: {max_area_matrix([[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]])}\nExpected: 8")
# print(f"Matrix 2: \n[0, 1, 1],\n[1, 1, 1],\n[0, 1, 1]\nOutput: {max_area_matrix([[0, 1, 1], [1, 1, 1], [0, 1, 1]])}\nExpected: 4")
# print(f"Matrix 3 (All 1s): \n[1, 1, 1],\n[1, 1, 1],\n[1, 1, 1]\nOutput: {max_area_matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])}\nExpected: 9")
# print(f"Matrix 4 (All 0s): \n[0, 0, 0],\n[0, 0, 0]\nOutput: {max_area_matrix([[0, 0, 0], [0, 0, 0]])}\nExpected: 0")
# print(f"Matrix 5 (Single row): \n[1, 0, 1, 1, 1]\nOutput: {max_area_matrix([[1, 0, 1, 1, 1]])}\nExpected: 3")
# print(f"Matrix 6 (Single column): \n[1],\n[1],\n[0],\n[1]\nOutput: {max_area_matrix([[1], [1], [0], [1]])}\nExpected: 2")
# print(f"Matrix 7 (Empty Matrix): \n[]\nOutput: {max_area_matrix([])}\nExpected: 0")
# print(f"Matrix 8 (Empty Columns): \n[[]]\nOutput: {max_area_matrix([[]])}\nExpected: 0")
# print(f"Matrix 9 (Complex): \n[1,0,1,0,0],\n[1,0,1,1,1],\n[1,1,1,1,1],\n[1,0,0,1,0]\nOutput: {max_area_matrix([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]])}\nExpected: 6") # Largest is 3x2 block in rows 2,3 columns 2,3,4 or 2x3 block


###### Overall Strategy (max_area_matrix function):

# Reduce to Histogram Problem: The key insight is that for any given row r in the binary matrix, we can calculate a "histogram" where the height of each bar j (column j) is the count of consecutive '1's ending at (r, j) and extending upwards.
# Iterate Row by Row:
# Initialize a 1D array (one_d) of size cols (number of columns in the matrix) to store the current histogram heights.
# For the first row, one_d is simply a copy of mat[0]. Calculate the maximum rectangle in this initial histogram using max_area_histogram.
# For each subsequent row r from 1 to rows-1:
# Update the one_d array:
# If mat[r][c] is 0, then the continuous block of 1s above it is broken, so one_d[c] becomes 0.
# If mat[r][c] is 1, then it extends the block of 1s from above, so one_d[c] is incremented by 1 (i.e., one_d[c] += 1).
# After updating one_d for the current row, call max_area_histogram(one_d) to find the largest rectangle that ends at this row.
# Keep track of the overall maximum area found across all rows.
# Detailed Strategy for max_area_histogram (Largest Rectangle in Histogram):

# This function uses a monotonic stack to efficiently find the Next Smaller Element to the Left (NSL) and Next Smaller Element to the Right (NSR) for each bar in the histogram.

# NSL Calculation (op_nsl array):

# Iterate through the heights array from left to right (i from 0 to n-1).
# Maintain a stack of (index, height) pairs. The stack is kept monotonically increasing in terms of height. This means stack[-1][1] (top element's height) is always less than or equal to stack[-2][1], and so on.
# For each heights[i]:
# Pop while not smaller: While the stack is not empty AND the height at the top of the stack (stack[-1][1]) is greater than or equal to heights[i], pop elements from the stack. These popped elements are "candidates" for NSL for elements further to their right, but heights[i] is a smaller element that cuts off their potential.
# Determine NSL:
# If the stack becomes empty after popping, it means there is no smaller element to the left of heights[i]. So, op_nsl[i] is set to -1 (a sentinel value indicating no boundary).
# Otherwise, the element at the top of the stack (stack[-1][0]) is the index of the nearest smaller element to the left of heights[i]. So, op_nsl[i] is set to stack[-1][0].
# Push current element: append (i, heights[i]) to the stack.
# NSR Calculation (op_nsr array):

# Similar to NSL, but iterate from right to left (i from n-1 down to 0).
# The logic is the same: pop elements from the stack that are greater than or equal to heights[i].
# Determine NSR:
# If the stack becomes empty, op_nsr[i] is set to n (a sentinel value indicating no boundary on the right).
# Otherwise, op_nsr[i] is set to stack[-1][0].
# append (i, heights[i]) to the stack.
# Calculate Area for Each Bar:

# After computing op_nsl and op_nsr for all bars, iterate from i from 0 to n-1.
# For each bar heights[i], the width of the largest rectangle it can be part of (where it's the shortest bar) is given by: (op_nsr[i] - op_nsl[i] - 1).
# op_nsr[i] gives the index of the first bar smaller than heights[i] to its right.
# op_nsl[i] gives the index of the first bar smaller than heights[i] to its left.
# The bars between op_nsl[i] and op_nsr[i] (exclusive) are all greater than or equal to heights[i].
# Subtracting 1 accounts for the fact that indices are 0-based and we need the count of elements between the boundaries.
# The current_area is width * heights[i].
# Update max_area_hist with the maximum current_area found.
# Return max_area_hist: This is the largest rectangle found within that specific histogram.