# #Sort a nearly sorted (or K sorted) array

# #Given an array arr[] and a number k . The array is sorted in a way that every element is at max k distance away from it sorted position. It means if we completely sort the array, then the index of the element can go from i - k to i + k where i is index in the given array. Our task is to completely sort the array.

# Examples: 

# Input: arr= [6, 5, 3, 2, 8, 10, 9], k = 3 
# Output: [2, 3, 5, 6, 8, 9, 10]

# Input: arr[]= [1, 4, 5, 2, 3, 6, 7, 8, 9, 10], k = 2
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import heapq 

def nearly_sort(arr,k):

    min_heap = []
    res = []
    for x in arr:

        heapq.heappush(min_heap, x)

        if len(min_heap) > k:
            res.append(heapq.heappop(min_heap))

    while min_heap:
        res.append(heapq.heappop(min_heap))


    return res 

if __name__ == "__main__":
    arr = [6, 5, 3, 2, 8, 10, 9]
    arr2 = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10]
    K = 3
    k2 = 2

    # Function call
    print("Sort a nearly sorted (or K sorted) array", nearly_sort(arr, K))

    print("Sort a nearly sorted (or K sorted) array", nearly_sort(arr2, k2))
