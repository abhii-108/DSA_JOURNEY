# #Sort elements by frequency

# Given an array of integers arr[], sort the array according to the frequency of elements, i.e. elements that have higher frequency comes first. If the frequencies of two elements are the same, then the smaller number comes first.

# Input: arr[] = [5, 5, 4, 6, 4]
# Output: [4, 4, 5, 5, 6]
# Explanation: The highest frequency here is 2. Both 5 and 4 have that frequency. Now since the frequencies are the same the smaller element comes first. So 4 comes first then comes 5. Finally comes 6. The output is 4 4 5 5 6.

# Input: arr[] = [9, 9, 9, 2, 5]
# Output: [9, 9, 9, 2, 5]
# Explanation: The highest frequency here is 3. Element 9 has the highest frequency So 9 comes first. Now both 2 and 5 have the same frequency. So we print smaller elements first. The output is 9 9 9 2 5.

import collections
import heapq

def sort_by_freq(arr):
    n = len(arr)

    mp = collections.Counter(arr)
    max_heap = []
    for val, freq in mp.items():

        heapq.heappush(max_heap,(-freq, val))

    res = []

    while max_heap:
        freq, val = heapq.heappop(max_heap)
        freq = -freq

        for x in range(freq):
            res.append(val)

    return res 


if __name__ == "__main__":
    arr =[5, 5, 4, 6, 4]
    arr2 = [9, 9, 9, 2, 5]


    # Function call
    print("#Closest K Elements in a Array", sort_by_freq(arr))
    print("#Closest K Elements in a Array", sort_by_freq(arr2))
