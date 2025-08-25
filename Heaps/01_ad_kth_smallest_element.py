# Given an array arr[] of N distinct elements and a number K, where K is smaller than the size of the array. Find the K'th smallest element in the given array.


# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
# Output: 7

# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
# Output: 10 


import heapq

def kth_smallest(arr,k):

    max_heap = []

    # python doesn't have in-build max_heap only min_heap is present. Therefore we insert value with negative symbol to get proper value.
    for x in arr:

        heapq.heappush(max_heap, x)

        if len(max_heap) > k :
            heapq.heappop(max_heap)

    # For self understanding how output look 
    # for key, val in enumerate(max_heap):
    #     print(f'{key} -> {val}')

    # This will also return top values. and max_heap[0] would have also returned Kth  smallest or largest element from array. 
    return (heapq.heappop(max_heap))


if __name__ == "__main__":
    #arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    arr = [7, 10, 4, 3, 20, 15]
    K = 3

    # Function call
    print("Kth Smallest Element is:", kth_smallest(arr, K))