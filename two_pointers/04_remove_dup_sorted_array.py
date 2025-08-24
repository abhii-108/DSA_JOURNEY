# Problem Statement: Given a sorted array nums, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Return the number of unique elements.



def remove_duplicate(arr):
    if len(arr) < 2:
        return arr 
    
    slow = 0 


    for fast in range (1,len(arr)-1):

        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]

    #return arr[:slow+1] 
    return arr


print( remove_duplicate([1, 2, 2,2,2,2,2,3,3,3,3,3, 4, 4, 4, 5, 5]))

