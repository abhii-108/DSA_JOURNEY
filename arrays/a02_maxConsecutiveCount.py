# Maximum consecutive one’s (or zeros) in a binary array

# Given an array arr[] consisting of only 0's and 1's, the task is to find the count of a maximum number of consecutive 1's or 0's present in the array.

# Input: arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
# Output: 4
# Explanation: The maximum number of consecutive 1's in the array is 4 from index 8-11.

# Input: arr[] = {0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1}
# Output: 2
# Explanation: The maximum number of consecutive 0's in the array is 2 from index 0-1.

# Input: arr[] = {0, 0, 0, 0}
# Output: 4
# Explanation: The maximum number of consecutive 0's in the array is 4.



def maxConsecutiveCount(arr):

    (maxcount,count) = (0, 1)

    for i in range(1, len(arr)):
        
        if arr[i] == arr[i-1]:
            count += 1
            
        else:
            maxcount = max(maxcount, count)
            #print(f'iteration-{i}, count-->{count}, maxcount-->{maxcount}')
            count = 1
    
    return max(maxcount,count) 

if __name__ == "__main__":
    arr = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    #arr2 =  [0, 0]
    print(maxConsecutiveCount(arr))
    