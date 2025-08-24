#Find the index of first 1 in a sorted array of 0's and 1's

#Given a sorted array consisting 0's and 1's. The problem is to find the index of first '1' in the sorted array. It could be possible that the array consists of only 0's or only 1's. If 1's are not present in the array then print "-1".


def binary_search(arr):

    left, right = 0, len(arr)-1

    res = -1 

    while left <= right:

        mid = left + (right - left) // 2 

        if arr[mid] == 1:
            res = mid 
            right = mid - 1
        
        else:
            left = mid+1

    return res 

print(binary_search([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))