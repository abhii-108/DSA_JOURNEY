# #Top K Frequent Elements in an Array

# Given an array arr[] and a positive integer k, the task is to find the k most frequently occurring elements from a given array.

# Note: If more than one element has same frequency then prioritise the larger element over the smaller one.
# Input: arr= [3, 1, 4, 4, 5, 2, 6, 1], k = 2
# Output: [4, 1]
# Explanation: Frequency of 4 is 2 and frequency of 1 is 2, these two have the maximum frequency and 4 is larger than 1.

# Input: arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
# Output: [5, 11, 7, 10]
# Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, frequency of 10 is 1. These four have the maximum frequency and 5 is largest among rest.

from collections import Counter
import heapq

def k_freq_num(arr, k ):

    mp = Counter(arr)

    min_heap = []

    for val, freq in mp.items():

        heapq.heappush(min_heap, (freq, val))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    
    res = []
    while min_heap:
        freq, val = heapq.heappop(min_heap)
        res.append(val)

    # Note: If more than one element has same frequency then prioritise the larger element over the smaller one. for this we have done reverse()
    # 
    res.reverse() 
    return res 

if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    arr2 = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
    k = 2
    k2 = 4

    # Function call
    print("#Closest K Elements in a Array", k_freq_num(arr, k))
    print("#Closest K Elements in a Array", k_freq_num(arr2, k2))