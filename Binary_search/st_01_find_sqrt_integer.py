#Program for Square Root of Integer using binary search
# Given a positive integer n, find its square root. If n is not a perfect square, then return floor of √n.

# Input: n = 4
# Output: 2
# Explanation: The square root of 4 is 2.

# Input: n = 11
# Output: 3
# Explanation: The square root of 11 lies in between 3 and 4 so floor of the square root is 3.


def bs_sqrt(n):
    if not n:
        return -1 
    

    left = 1 
    right = n 
    op = 1 
    while left<= right:
        mid = left + (right - left) // 2

        sq_val = mid * mid 

        if sq_val <= n:
            op = mid 
            left = mid + 1
        
        
        else:
            right = mid - 1

    return op 


print(bs_sqrt(21))

print(bs_sqrt(31))

print(bs_sqrt(36))         