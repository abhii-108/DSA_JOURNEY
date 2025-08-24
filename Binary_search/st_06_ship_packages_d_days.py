#Capacity to Ship Packages within D Days

#You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. The packages must be shipped within 'd' days.
# The weights of the packages are given in an array 'of weights'. The packages are loaded on the conveyor belts every day in the same order as they appear in the array. 
# The loaded weights must not exceed the maximum weight capacity of the ship.
# Find out the least-weight capacity so that you can ship all the packages within 'd' days.

# Input Format: N = 5, weights[] = {5,4,5,2,3,4,5,6}, d = 5
# Result: 9
# Explanation: If the ship capacity is 9, the shipment will be done in the following manner:
# Day         Weights            Total
# 1        -       5, 4          -        9
# 2        -       5, 2          -        7
# 3        -       3, 4          -        7
# 4        -       5             -        5
# 5        -       6             -        6
# So, the least capacity should be 9.

def helper(arr,day_capactiy):

    curr_load = 0 
    curr_day = 1
    for x in range(0,len(arr)):

        if (curr_load + arr[x]) > day_capactiy:
            curr_load = arr[x]
            curr_day += 1
        else:
            curr_load += arr[x]

    return curr_day


def least_ship_capacity(arr,d):
    N = len(arr)

    #we need to find the maximum weight in array as this will be the minium weight that ship can take in single day 
    # Also we need to find sum of total weight, this will help in setting the range of max weight that can be take on single day 
    # left = max(arr) # This will store the maximum weight 
    # right = sum(arr) #This will store the minimum weight 

    left = 0 
    right = 0
    for x in range(0,len(arr)):
        left = max(left, arr[x])
        right += arr[x]
    res = -1
    print(f'{left},{right}')
    #Applying Binary search....
    while left <= right:
        mid = left + (right - left) // 2

        if helper(arr,mid) <= d:
            res = mid 
            right = mid - 1
        else:
            left = mid+1

    return left 


print(least_ship_capacity([5,4,5,2,3,4,5,6],5))




###############################




def findDays(weights, cap):
    days = 1  # First day
    load = 0
    n = len(weights)  # Size of array
    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # Move to next day
            load = weights[i]  # Load the weight
        else:
            # Load the weight on the same day
            load += weights[i]
    return days

def leastWeightCapacity(weights, d):
    # Find the maximum and the summation
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high) // 2
        numberOfDays = findDays(weights, mid)
        if numberOfDays <= d:
            # Eliminate right half
            high = mid - 1
        else:
            # Eliminate left half
            low = mid + 1
    return low

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacity(weights, d)
print("The minimum capacity should be:", ans)



