## Sum of all elements between k1'th and k2'th smallest elements

## Given an array of integers and two numbers k1 and k2. Find the sum of all elements between given two k1'th and k2'th smallest elements of the array. It may be assumed that (1 <= k1 < k2 <= n) and all elements of array are distinct.

# Input : arr[] = {20, 8, 22, 4, 12, 10, 14},  k1 = 3,  k2 = 6  
# Output : 26          
#          3rd smallest element is 10. 6th smallest element 
#          is 20. Sum of all element between k1 & k2 is
#          12 + 14 = 26

# Input : arr[] = {10, 2, 50, 12, 48, 13}, k1 = 2, k2 = 6 
# Output : 73 


import heapq

def sumbetween_twokth(arr, k1, k2):

    max_heap = []

    for val in arr :

        heapq.heappush(max_heap, -val)

        if len(max_heap) >= k2:
            heapq.heappop(max_heap)

    res = 0
    while len(max_heap) > k1:

        res += (-1 *heapq.heappop(max_heap))
    
    return res 


if __name__ == "__main__":
  
    arr = [20, 8, 22, 4, 12, 10, 14]
    arr2 = [10, 2, 50, 12, 48, 13]
    print(sumbetween_twokth(arr,3,6))
    print(sumbetween_twokth(arr2,2,6))