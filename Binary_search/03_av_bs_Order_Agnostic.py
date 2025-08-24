#Order-Agnostic Binary Search

#Order-Agnostic Binary Search is a modified version of Binary Search algorithm. Here in this modified binary search comes with one more condition checking. The intuition behind this algorithm is what if the order of the sorted array is not given. So here check that the value of the first element is greater or smaller than the last element.

# If the first element is smaller than the last element-then if the search key value X is less than the middle of the interval then the end pointer will be changed to middle -1 otherwise start will be changed to middle + 1.
# If the first element is greater than the last element-then if the search key value X is less than the middle of the interval then the start pointer will move to the next element of the middle element otherwise the end pointer will move previous to the middle element.




def bs_order_agnostic(arr,x):
    start, end = 0, len(arr)-1

    asce =  arr[start] < arr[end]  ## this will return true of false 

    while start <= end :

        mid = start + (end - start)//2 
        if arr[mid] == x :
            return mid 

        if asce:

            if arr[mid] > x :
                end = mid - 1 
            else :
                start = mid + 1
        else:
            if arr[mid] > x :
                start = mid + 1
            else:
                end = mid - 1
    return -1 


print(bs_order_agnostic([5, 4, 3, 2, 1],4))
print(bs_order_agnostic([2, 3, 4, 10, 40],10))