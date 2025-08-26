# #Rearrange a string so that all same characters become d distance away

# Given a string s and a positive integer d, rearrange the characters of the string so that any two identical characters are at least d positions apart. If no such arrangement is possible, print "Cannot be rearranged".

# Input: s="abb",  d = 2
# Output: "bab"
# Explanation: The character 'a' and 'b' need to be rearranged such that 'b' appears at least 2 positions away from the other 'b'. One valid solution is "bab", where the two 'b's are at positions 2 and 3, satisfying the distance requirement.

# Input: s="aacbbc",  d = 3
# Output: "abcabc"
# Explanation: The characters are rearranged so that each pair of identical characters ('a', 'b', 'c') are placed at least 3 positions apart. One valid solution is "abcabc".

# Input: s="geeksforgeeks",  d = 3
# Output: "egkegkesfesor"
# Explanation: The characters are rearranged such that identical characters are at least 3 positions apart. One valid solution is "egkegkesfesor".

# Input: s="aaa",  d = 2
# Output: "Cannot be rearranged"
# Explanation: It's impossible to rearrange the characters of the string such that 'a' appears more than once and still respects the required distance of 2.

from collections import Counter, deque
import heapq 

def rearrangeString(arr, k):

    mp = Counter(arr)

    max_heap = []

    for val, freq in mp.items():

        heapq.heappush(max_heap,(-freq, val))

    q = deque()

    res = []
    while max_heap:

        freq, val = heapq.heappop(max_heap)
        freq = - freq 

        res.append(val)

        q.append((freq-1, val))

        if len(q) == k :
            q_freq, q_val = q.popleft()

            if q_freq > 0:
                heapq.heappush(max_heap,(-q_freq, q_val))

    if len(res) == len(arr):
        return "".join(res)

    return "not possible"

if __name__ == "__main__":
    arr ='aacbbc'
    k=3
    arr2 = 'aaa'
    k2=2


    # Function call
    print("RE-Arrange string", rearrangeString(arr,k))

    print("RE-Arrange string", rearrangeString(arr2,k2))
