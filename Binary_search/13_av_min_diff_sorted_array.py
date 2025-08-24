def ceil(arr,x):
    left, right = 0, len(arr)-1
    ceil_res = -1
    floor_res = -1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= x:
            ceil_res = mid
            right = mid - 1

        else:
            left = mid + 1

    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= x:
            floor_res = mid 
            left = mid + 1

        else:
            right = mid - 1

    return min(arr[ceil_res],arr[floor_res])


print(ceil([1, 2, 4, 6, 10, 12, 14],13) )


print(ceil([1, 2, 8, 10, 10, 12, 19],3) )



print(ceil([1, 2, 8, 10, 10, 12, 19],20) )

print(ceil([1, 2, 8, 10, 10, 12, 19],0) )