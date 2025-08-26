# #Rearrange characters in a String such that no two adjacent characters are same
# Given a string s with lowercase repeated characters, the task is to rearrange characters in a string so that no two adjacent characters are the same. If it is not possible to do so, then print empty string ("").

# Note: Multiple valid rearranged strings can be possible for same input string.

# Examples: 

# Input: s = "aaabc" 
# Output: abaca 
# Explanation: No two adjacent characters are same in the output string.

# Input: s = "aa"
# Output: ""
# Explanation: Not Possible

# Input: s = "aaaabc" 
# Output: ""
# Explanation: Not Possible

import heapq 
import math
from collections import Counter 

def re_arrange_string(arr):
    n  = len(arr)
    mp = Counter(arr)

    max_heap = []

    for val, freq in mp.items():
        if  freq > math.floor((n+1)/2):
            #print('Not possible')
            return 'Not possible'
        heapq.heappush(max_heap,(-freq, val))

    res = ''

    while len(max_heap) > 1:
        freq1, val1 = heapq.heappop(max_heap)
        freq2, val2 = heapq.heappop(max_heap)

        res += val1 + val2

        if freq1 < -1: 
            heapq.heappush(max_heap,(freq1+1,val1))
        if freq2 < -1: 
            heapq.heappush(max_heap,(freq2+1,val2))

    
    while max_heap:
        freq, val = heapq.heappop(max_heap)
        res += val

    return res 

    ## We can store result in arr and  return ''.join(ans) at end/

if __name__ == "__main__":
    arr ='aaabc'
    arr2 = 'aaaabc'


    # Function call
    print("RE-Arrange string", re_arrange_string(arr))

    print("RE-Arrange string", re_arrange_string(arr2))
