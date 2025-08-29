## Remove Stones to Minimize the Total

# You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

# Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
# Notice that you can apply the operation on the same pile more than once.

# Return the minimum possible total number of stones remaining after applying the k operations.

# floor(x) is the largest integer that is smaller than or equal to x (i.e., rounds x down).

 

# Example 1:

# Input: piles = [5,4,9], k = 2
# Output: 12
# Explanation: Steps of a possible scenario are:
# - Apply the operation on pile 2. The resulting piles are [5,4,5].
# - Apply the operation on pile 0. The resulting piles are [3,4,5].
# The total number of stones in [3,4,5] is 12.

from typing import List
import heapq 
import math 

def minStoneSum(piles: List[int], k: int) -> int:

    total_stones=0 

    for i, val in enumerate(piles):
        piles[i] = -val
    
    heapq.heapify(piles)

    while k > 0:
        top = -( heapq.heappop(piles))

        top = math.ceil(top/2)

        total_stones += (top)

        k -= 1
    
    while piles:
        
        total_stones += (-heapq.heappop(piles))

    return total_stones



print(minStoneSum([5,4,9],2))