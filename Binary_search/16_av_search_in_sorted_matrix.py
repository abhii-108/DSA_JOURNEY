# #Approach
# To efficiently search for a target value in a row-wise and column-wise sorted matrix, we can leverage the sorted properties to eliminate rows or columns in each comparison. The algorithm starts from the top-right corner of the matrix (or bottom-left) and moves based on comparisons with the target value:

# Start at top-right corner: Initialize the search at (row=0, col=n-1).

# Compare and move:

# If the current element equals the target, return its position.

# If the current element is greater than the target, move left (decrease column index) to find a smaller value.

# If the current element is less than the target, move down (increase row index) to find a larger value.

# Termination: If the search goes out of bounds, the target is not present.

# This approach efficiently reduces the search space by either moving left or down in each step, leveraging the sorted properties of the matrix.


def search_in_sorted_matrix(matrix,x):
    #Edge case checking 
    if not matrix or not matrix[0]:
        return None 
    
    # set length for row  and columns 

    m = len(matrix) ## Finding number of row in matrix 
    n = len(matrix[0]) ## Finding number of columns in matrix 

    # setting the pointer location 

    row = 0  ## we will start from first row 
    col = n-1 ## We will start from last column first element   matrix [ _ _ _ *]


    # Interate over matrix 
    ## setting while condition for traversal ... column will be reducing from n to 0  and rows will be increase from 0 to m   
    while row < m and col >= 0: 

        current = matrix[row][col]

        if current == x :
            return (row, col)
        
        ## if current value is more then full column is of no use we can skip and move to left column 
        elif current > x :
            col -= 1
        
        else : # increase the row to search in next / below row if current value is less 
            row += 1

    return None

# Test case
matrix = [
    [3, 30, 38],
    [20, 52, 54],
    [35, 60, 69]
]
x = 20
print(search_in_sorted_matrix(matrix, x))  