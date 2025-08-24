#Floor in a Sorted Array

##Given a sorted array and a value x, find the element of the floor of x. The floor of x is the largest element in the array smaller than or equal to x.


def floor(arr,x):
    left, right = 0, len(arr)-1
    res = -1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= x:
            res = mid 
            left = mid + 1

        else:
            right = mid - 1

    return res 

print(floor ([1, 2, 4, 6, 10, 12, 14],13) )
