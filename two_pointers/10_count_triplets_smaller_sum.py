#### Count Triplets with Sum Smaller Than Target ########
#### Count all triplets [a, b, c] such that a + b + c < target ####


def count_triplets_smaller_sum(arr,target):

    if len(arr) < 3:
        return 0
    
    arr.sort()

    #creating variable to store the length of arrya 
    n = len(arr)

    res_cnt = 0 

    for i in range(0,n-2):

        left = i+1 
        right = n-1

        while left < right:

            curr_sum  = arr[i] + arr[left] + arr[right]

            if curr_sum < target:
                res_cnt += right - left 

                left += 1
                # below code is for distinct value of triplet 
                while left <right and arr[left] == arr[left - 1]:
                    left += 1

                right -= 1
                while left <right and arr[right] == arr[right - 1]:
                    right -= 1
            
            else:
                right -= 1

        
    return res_cnt


print(count_triplets_smaller_sum([-1, 2, 3,2,3,1,-2,-5,2,4],5))
