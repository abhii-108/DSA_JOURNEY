# Remove Element: Given an array nums and a value val, remove all occurrences of val in-place. Return the number of elements in nums which are not equal to val.
# Input: arr[] = [3, 2, 2, 3], ele = 3
# Output: 2
# Explanation: The answer is 2 because there are 2 elements which are not equal to 3 and arr[] will be modified 
#such that the first 2 elements contain the elements which are not equal to 3 and remaining elements can contain any element. So, modified arr[] = [2, 2, _, _]

# Input: arr[] = [0, 1, 3, 0, 2, 2, 4, 2], ele = 2
# Output: 5
# Explanation: The answer is 5 because there are 5 elements which are not equal to 2 and arr[] will be modified 
#such that the first 5 elements contain the elements which are not equal to 2 and remaining elements can contain any element. So, modified arr[] = [0, 1, 3, 0, 4, _, _, _]


def remove_element(arr,ele):
    #Edge case if arr size less then 1 i.e 0

    if len(arr)<1:
        return []

    slow = 0 

    for fast in range(0, len(arr)):

        if arr[fast] != ele:
            arr[slow] = arr[fast]
            slow += 1

    for x in range(slow, len(arr)):
        arr[x] = '_'

    print(arr)
    return slow 


print(remove_element([0, 1, 3,2,2, 0, 2,5,6, 2, 4, 2, 11],2))
