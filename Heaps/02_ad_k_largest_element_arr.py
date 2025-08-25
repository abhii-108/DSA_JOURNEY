#Find k largest elements in an array

#Given an array arr[] and an integer k, the task is to find k largest elements in the given array. Elements in the output array should be in decreasing order.

#Input:  [1, 23, 12, 9, 30, 2, 50], k = 3
# Output: [50, 30, 23]

# Input:  [11, 5, 12, 9, 44, 17, 2], k = 2
# Output: [44, 17]

import heapq

def largest_k_element(arr, k):

    min_heap = []

    for x in arr:

        heapq.heappush(min_heap,x)

        if len(min_heap)>k:
            heapq.heappop(min_heap)
        

    res = []
    # if we use for loop then we were not getting last element 
    while min_heap:
        res.append(heapq.heappop(min_heap))

    return res 

if __name__ == "__main__":
    arr = [1, 23, 12, 9, 30, 2, 50]
    arr2 = [11, 5, 12, 9, 44, 17, 2]
    K = 3
    k2 = 2

    # Function call
    print("Kth Smallest Element is:", largest_k_element(arr, K))

    print("Kth Smallest Element is:", largest_k_element(arr2, k2))