# you are given 'N’ roses and you are also given an array 'arr'  where 'arr[i]'  denotes that the 'ith' rose will bloom on the 'arr[i]th' day.
# You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet.
# Find the minimum number of days required to make at least ‘m' bouquets each containing 'k' roses. Return -1 if it is not possible.


# Example 1:
# Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
# Result: 12
# Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.


# Observation: 


# Impossible case: To create m bouquets with k adjacent flowers each, we require a minimum of m*k flowers in total. If the number of flowers in the array, represented by array-size, is less than m*k, it becomes impossible to form m bouquets even after all the flowers have bloomed. In such cases, where array-size < m*k, we should return -1.
#  Maximum possible answer: The maximum potential answer corresponds to the time needed for all the flowers to bloom. In other words, it is the highest value within the given array i.e. max(arr[]).
# Minimum possible answer: The minimum potential answer corresponds to the time needed for atleast one flower to bloom. In other words, it is the smallest value within the given array i.e. min(arr[]).


def helper(arr,day,m,k):
    N = len(arr)
    # decalare variable to save the count of consequtive flower that has bloom 
    cnt = 0 
    no_of_b =0 
    for i in range(0,N):
        if arr[i] <= day:
            cnt += 1
        else:
            no_of_b += cnt // k 
            cnt = 0

    no_of_b += cnt // k 

    if no_of_b >= m:
        return True 
    else:
        return False 




def roseGarden(arr,k,m):
    val = m * k  ## for comparision for edge case 
    N = len(arr)

    if N < val:
        return -1 
    
    # We are finding left (min value for a single flower to bloom) right (max value for a single flower to bloom)
    left = float('inf')
    right = float('-inf')

    for i in range(0,N):
        left = min(left, arr[i])
        right = max(right, arr[i])

    
    #Binary search on the left and right range we have to use a helper function to find m bouqguets with K flower 
    # Binary search is use for finding the required day fast. 
    res = -1     
    while left <= right:

        mid = left + (right - left) // 2

        if helper(arr,mid,k,m):
            res = mid 
            right = mid - 1
        else:
            left = mid + 1

    return res 



print(roseGarden([7, 7, 7, 7, 13, 11, 12, 7],2,3))