# Move all zeros to end of array

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

# Input: arr[] = [10, 20, 30]
# Output: arr[] = [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: arr[] = [0, 0]
# Explanation: No change in array as there are all 0s.


def pushZerosToEnd(arr):

    slow = 0
    fast = 1


    while fast < len(arr)-1:

        if arr[slow] == 0 and arr[fast] != 0:
            print(f'swap {fast}')
            arr[slow]  = arr[fast]
            arr[fast] = 0
            slow += 1
            fast += 1
        elif arr[slow] == 0 and arr[fast] == 0:
            fast += 1
        else:
            slow += 1
            fast += 1

        
    return arr


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    arr2 =  [0, 0]
    arr1=pushZerosToEnd(arr2)
    for num in arr1:
        print(num, end=" ")