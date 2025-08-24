## Binary search algorithm 

#Binary Search Algorithm is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N).

arr = [2, 3, 4, 10, 40]
x = 10

def binary_search(arr,x):
    start, end = 0,len(arr)-1

    if len(arr) == 0 or (len(arr) == 1 and arr[0] != x ):
        return -1 
    
    if len(arr) == 1 and arr[0] == x:
        return 0

    while start <= end:
        mid = start + (end - start) // 2


        if arr[mid] == x :
            return mid 
        
        ## search left side of mid by reducing the value of  end pointer 
        elif arr[mid] > x :
            end = mid - 1
        
        ## search right side of mid by increasing the value if start pointer arr[mid] < x value of mid is less than given value to find then move to right side for search 
        else: 
            start = mid + 1

    ## if value not found then return value to -1 
    return -1 


print(binary_search(arr,x))