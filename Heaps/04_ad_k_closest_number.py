#Closest K Elements in a Sorted Array

# You are given a sorted array arr[] containing unique integers, a number k, and a target value x. Your goal is to return exactly k elements from the array that are closest to x, excluding x itself if it is present in the array.

# An element a is closer to x than b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a > b (i.e., prefer the larger element if tied)
# Examples: 

# Input: arr[] = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], k = 4, x = 35
# Output: 39 30 42 45
# Explanation: First closest element to 35 is 39.
# Second closest element to 35 is 30.
# Third closest element to 35 is 42.
# And fourth closest element to 35 is 45.

# Input: arr[] = [1, 3, 4, 10, 12], k = 2, x = 4
# Output: 3 1
# Explanation: 4 is excluded, Closest elements to 4 are: 3 (1), 1 (3). So, the 2 closest elements are: 3 1


import heapq 

def closest_k_number(arr, k, x):

    max_heap = []

    for val in arr:

        # To satisfy this condition [excluding x itself if it is present in the array.]
        if val != x:
            diff = abs(x - val)

            heapq.heappush(max_heap,(-diff, val))

        if len(max_heap) > k :
            heapq.heappop(max_heap)

    res = []
    while max_heap:
        diff, val = heapq.heappop(max_heap)
        res.append(val)

    return res 

if __name__ == "__main__":
    arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    arr2 = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10]
    k = 4
    k2 = 2

    # Function call
    print("#Closest K Elements in a Array", closest_k_number(arr, k, 35))