def nearly_sorted(arr,x):
    left, right = 0, len(arr)-1


    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid 

        if arr[mid-1] == x and left < mid:
            return mid-1
        
        if arr[mid+1] == x and right > mid:
            return mid+1 
        
        if arr[mid] > x :
            rigth = mid - 2
        else:
            left = mid + 2


    return -1 



print(nearly_sorted([10, 3, 40, 20, 50, 80, 70],80))