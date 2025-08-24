#Ceiling in a sorted array

# Given a sorted array and a value x, find index of the ceiling of x. The ceiling of x is the smallest element in an array greater than or equal to x.

# Note: In case of multiple occurrences of ceiling of x, return the index of the first occurrence


def ceil(arr,x):
    left, right = 0, len(arr)-1
    res = -1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= x:
            res = mid 
            right = mid - 1

        else:
            left = mid + 1

    return res 

print(ceil([1, 2, 4, 6, 10, 12, 14],13) )


print(ceil([1, 2, 8, 10, 10, 12, 19],3) )



print(ceil([1, 2, 8, 10, 10, 12, 19],20) )

print(ceil([1, 2, 8, 10, 10, 12, 19],0) )