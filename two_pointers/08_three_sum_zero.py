#Triplet Sum to Zero
#Problem Statement: Given an array of integers, find all unique triplets [a, b, c] such that a + b + c = 0. The solution set must not contain duplicate triplets.
# a + b + c = 0  -->  b + c = -a 


def three_sum_zero(arr):
    # first check if len of arr is more then 2 else return it 
    if len(arr) < 3:
        return arr 
    # we have to use sorting as this will help in using two pointer technique
    arr.sort()

    #setting variable for size of array 
    n = len(arr)

    op = []

    # fixing the first element and then using two pointer inside the loop

    for i in range(0,n-2):

        left = i + 1
        right = n - 1 

        target_sum = -arr[i]

        while left < right:

            curr_sum = arr[left] + arr[right]

            if curr_sum == target_sum:
                op.append((arr[i],arr[left],arr[right]))
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            
