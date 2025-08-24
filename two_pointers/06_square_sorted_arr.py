#Squaring a Sorted Array

#Problem Statement: Given a sorted array of integers, return a new array containing the squares of all numbers from the input array, also sorted in increasing order.


def sorted_squares(arr):
    # creating a list to store the value of square rooted element 
    square_op = [0] * len(arr)

    #setting two pointer left and right for iterating through arr/list
    left, right = 0, len(arr)-1

    op_pointer = len(arr) - 1 


    while left <= right:
        # getting the abs value of left and right pointer 

        # abs_left = abs(arr[left])
        # abs_right = abs(arr[right])

        # if abs_left > abs_right:
        #     square_op[op_pointer] = abs_left * abs_left
        #     op_pointer -= 1
        #     left += 1
        # else:
        #     square_op[op_pointer] = abs_right * abs_right
        #     op_pointer -= 1
        #     right -= 1

        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            square_op[op_pointer] = left_square
            left += 1
        else:
            square_op[op_pointer] = right_square
            right -= 1

        op_pointer -= 1
                
        
    return square_op


print(sorted_squares([-6, -3, -1, 2, 4, 5]))
print(sorted_squares([-5, -4, -2, 0, 1]))