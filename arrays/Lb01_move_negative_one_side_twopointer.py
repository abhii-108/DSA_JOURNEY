# Move all negative numbers to beginning and positive to end with constant extra space

# Given an array containing both positive and negative numbers in random order. The task is to rearrange the array elements so that all negative numbers appear before all positive numbers.

# Note:

# Given array does not contain any zeroes.
# Order of resultant array does not matter.

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5


# def move_element(arr):

#     i = 0
#     j = 0 
#     print(arr)
#     size = len(arr)
#     while j < size:

#         if arr[j] < 0:

#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

#             j += 1
#             i += 1

#         elif arr[j] > 0:

#             j += 1
        
#     return arr 

# print(move_element([-12, 11, -13, -5, 6, -7, 5, -3, -6]))


def move_element(arr):
    i = 0 
    j = len(arr)-1

    while i < j :

        if arr[i] < 0 and arr[j] > 0 :
            i += 1
            j -= 1
        
        elif arr[i] > 0 and arr[j] < 0:
            (arr[i],arr[j]) = (arr[j],arr[i])
            i += 1
            j -= 1
        
        elif arr[i] < 0:
            i += 1
        
        elif arr[j] > 0:
            j += 1
        
    return arr 

print(move_element([-12, 11, -13, -5, 6, -7, 5, -3, -6]))