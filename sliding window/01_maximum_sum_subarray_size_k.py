#Max Sum Subarray of size K

# Input: arr[] = [100, 200, 300, 400] , k = 2
# Output: 700
# Explanation: arr3  + arr4 = 700, which is maximum.


def max_sum_subarray(arr,k):
    """Calculate maximum sum of any contiguous subarray of size k
    
    Args:
        arr (list): Input array of integers
        k (int): Fixed window size
    
    Returns:
        int: Maximum sum of any k-length subarray
    """

    i = 0  # left pointer or start of the window 
    j = 0  # Right pointer or End of window 

    max_sum = float('-inf')
    window_sum = 0 

    while j < len(arr):

        window_sum += arr[j]


        if (j-i+1) < k: # check size/length of subarray is yet not met. increase right pointer
            j += 1
        
        elif (j-i+1) == k: #  if length of subarry is matched. The do find max sum 
            max_sum = max(max_sum,window_sum)
            print(f'{max_sum}', end="-->")

            window_sum -= arr[i] ## removing the value of left pointer from window sum before increamenting left pointer
            i += 1
            j += 1
    
    print('------max sum sub array is------',end='\n')
    return max_sum



print(max_sum_subarray([100, 200, 300, 400] , 2))
print(max_sum_subarray([100, 200, 300, 400] , 1))