#Find position of an element in a sorted array of infinite numbers
#Given a sorted array arr[] of infinite numbers. The task is to search for an element k in the array.

def find_element_inf(arr,x):
    
    left,right = 0,1

    ## here we increase the position of right pointer 
    while x > arr[right]:
        left = right
        right = right * 2

    while left <= right :

        mid = left + (right - left) // 2


        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            left = mid + 1
        
        else:
            right = mid - 1

    return -1


print(find_element_inf([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170],10))


