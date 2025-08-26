# # ## Kth Largest Element in a Stream

# # You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# # You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.


from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]) -> None:
        self.k = k 
        self.nums = nums 

        heapq.heapify(self.nums)
        # If the heap is larger than k, remove the smallest elements until it has exactly k elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    
    def add(self, val):

        heapq.heappush(self.nums, val)
        # If the heap is larger than k, remove the smallest elements until it has exactly k elements
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # The smallest element in the heap is now the k-th largest element
        return self.nums[0]
    

if __name__ == "__main__":

    arr = [4, 5, 8, 2]
    k = 3

    add = [3,5,10,9,4]
    
    sol = KthLargest(k, arr)

    for x in add:
        print(sol.add(x), end=' ')
    