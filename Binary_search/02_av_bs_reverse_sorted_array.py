#Search an element in a reverse sorted array
#Given an array arr[] sorted in decreasing order, and an integer X,
#the task is to check if X is present in the given array or not. If X is present in the array, print its index ( 0-based indexing). Otherwise, print -1.


# Input: arr[] = {5, 4, 3, 2, 1}, X = 4
# Output: 1
# Explanation: Element X (= 4) is present at index 1.
# Therefore, the required output is 1.



# Input: arr[] = {10, 8, 2, -9}, X = 5
# Output: -1
# Explanation: Element X (= 5) is not present in the array.
# Therefore, the required output is -1.
#



def reverse_binary_search(arr,x):

    start, end = 0 , len(arr)


    while start <= end :
        ## find mid position 
        mid = start + (end - start) // 2

        if arr[mid] == x :
            return mid 
        
        elif arr[mid] > x :
            start = mid + 1
        
        else:
            end = mid - 1

    return -1 


print(reverse_binary_search([10, 8, 2, -9],5))

print(reverse_binary_search([5, 4, 3, 2, 1],4))