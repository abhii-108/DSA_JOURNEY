#Reduce the array such that each element appears at most 2 times

##Given a sorted array arr of size N, the task is to reduce the array such that each element can appear at most two times.

# Input: arr[] = {1, 2, 2, 2, 3} 
# Output: {1, 2, 2, 3} 
# Explanation: 
# Remove 2 once, as it occurs more than 2 times.


# Input: arr[] = {3, 3, 3} 
# Output: {3, 3} 
# Explanation: 
# Remove 3 once, as it occurs more than 2 times.  

def remove_duplicates_at_most_twice(arr):
    #Edge case check if size of array is less then or equal to 2 
    if len(arr) <= 2:
        return arr 
    
    slow = 2 

    for fast in range(2,len(arr)):

        if arr[fast] != arr[slow-2]:
            arr[slow] = arr[fast]
            slow += 1
    return arr[:slow]


print(remove_duplicates_at_most_twice([1, 2, 2, 2, 3]))

print(remove_duplicates_at_most_twice([3, 3, 3]))


# Q2 # Move Zeros to End: Given an array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements

def move_zeros(arr):
    #Edge case if len of arr is less than or equal to 1
    if len(arr) <= 1:
        return arr 
    
    slow = 0 

    for fast in range(0, len(arr)):

        if arr[fast] != 0 :

            arr[slow] = arr[fast]
            slow += 1
    
    for i in range(slow,len(arr)):
        arr[i]=0
    #print(arr)
    return arr

print(move_zeros([1, 2, 0, 4, 3, 0, 5, 0]))

print(move_zeros([0, 20, 30]))

print(move_zeros([0, 0, 0]))