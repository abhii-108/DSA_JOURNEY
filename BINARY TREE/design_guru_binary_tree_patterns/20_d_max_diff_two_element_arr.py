#Maximum Difference between Two Elements such that Larger Element Appears after the Smaller Element

#Given an array of integers, the task is to find the maximum difference between any two elements such that larger element appears after the smaller number.  We mainly need to find maximum difference in an inversion (larger before smaller)

#Note: If no such pair exists, return -1.

# Input : arr = [2, 3, 10, 6, 4, 8, 1]
# Output : 8
# Explanation : The maximum difference is between 10 and 2.

# Input : arr = [7, 9, 5, 6, 3, 2]
# Output : 2
# Explanation : The maximum difference is between 9 and 7.

# Input: arr = [4, 3, 3, 2, 1]
# Output: -1
# Explanation: No such pair exists such that i < j and arr[i] < arr[j].

########## Try to solve this question using ####### 



def max_diff(arr):

    n= len(arr)
    if n <= 1:
        return 0 
    


    def helper(arr, idx, min_val, max_val):
    ## base condition 
        if idx == len(arr):
            return min_val, max_val
        ## Task  

        min_val = min(min_val, arr[idx])
        max_val = max(max_val, arr[idx])


        #print(f'mn-->{mn} mx-->{mx} diff-->{diff2}')

        return helper(arr,idx+1, min_val, max_val)

    min_element, max_element = helper(arr,0,arr[0],arr[0])

    return abs(max_element - min_element)

print(max_diff([2, 3, 10, 6, 4, 8, 1]))

############################################################################################################################################

