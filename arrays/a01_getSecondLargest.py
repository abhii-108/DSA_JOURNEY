# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

# Note: If the second largest element does not exist, return -1

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.

# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 there is no second largest element. float('-inf')


def getSecondLargestElement(arr):

    max1 = -1
    max2 = -1

    for i in range(len(arr)):
        if arr[i] > max1:
            max2 = max1 
            max1 = arr[i]
        
        elif arr[i] < max1 and arr[i] > max2:
            max2 = arr[i]
        
    return max2 

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    #arr2 =  [0, 0]
    print(getSecondLargestElement(arr))
    print(getSecondLargestElement([10, 10, 10]))
    print(getSecondLargestElement([10, 5, 10]))