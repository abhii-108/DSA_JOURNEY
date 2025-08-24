#Nth Root of a Number using Binary Search

#Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. 
#If the 'nth root is not an integer, return -1.

# Example 1:
# Input Format: N = 3, M = 27
# Result: 3
# Explanation: The cube root of 27 is equal to 3.

# Example 2:
# Input Format: N = 4, M = 69
# Result: -1
# Explanation: The 4th root of 69 does not exist. So, the answer is -1.

def helper(N,M,mid):
    sum = 1 
    for i in range(N+1):
        sum = sum * mid 

        if sum > M :
            return 2 
        elif sum == M :
            return 1 
        
    if sum < M:
        return 0

def n_root_num(N, M):

    # our range of search is from 1 to M 
    # we will require one helper function which will do the multiplication N time 


    left = 1
    right = M 
  
    while left<= right:

        mid = left + (right - left) // 2 

        mid_cal_op = helper(N,M,mid )

        if mid_cal_op == 1:
            return mid 

        elif mid_cal_op == 0 :
            left = mid + 1

        else:
            right = mid - 1

    return -1  


print(n_root_num(3,27))

print(n_root_num(4,69))

print(n_root_num(7,256))