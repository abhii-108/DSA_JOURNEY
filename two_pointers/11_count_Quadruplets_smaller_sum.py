#Count Quadruplets with Sum Smaller Than Target: Count all quadruplets (a, b, c, d) such that a + b + c + d < target.

def four_sum_smaller(arr,target):

    #Edge case if array size is less then 4
    if len(arr) < 4:
        return 0
    arr.sort()
    res = 0 

    n = len(arr)

    for i in range(0,n-3):
        
        for j in range(i+1,n-2):

            left = j + 1
            right = n - 1 

            while left < right :

                curr_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if curr_sum < target:
                    res = res + (right - left)
                    left += 1
                else:
                    right -= 1
    
    return res 

print(four_sum_smaller([-1, 2, 3,2,3,1,-2,-5,2,4],2))


######################################
# 4 Sum - All Distinct Quadruplets with given Sum in an Array
# Input: arr[] = [10, 11, 10, 12, 11], target = 43 
# Output: [[10, 10, 11, 12]]
# Explanation: The quadruplets are: 
# [10, 11, 10, 12], sum = 10 + 11 + 10 +12 = 43
# [10, 11, 10, 11], sum = 10 + 11 + 10 + 11 = 42
# [10, 11, 12, 11], sum = 10 + 11 + 12 + 11 = 44
# [10, 10, 12, 11], sum = 10 + 10 + 12 + 11 = 43
# [11, 10, 12, 11], sum = 11 + 10 + 12 + 11 = 44
# When arranged in sorted order, there is only one distinct quadruplet with sum = 43, that is [10, 10, 11, 12]

# Input: arr[] = [10, 2, 3, 4, 5, 7, 8], target = 23 
# Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]] 
# Explanation: There are only three distinct quadruplets with sum = 23.

# Input: arr[] = [1, 1, 1, 1, 1, 1], target = 4 
# Output: [[1, 1, 1, 1]]


# Python Program to find all Distinct Quadruplets with given
# Sum in an Array using Two Pointer Technique

# Function to find quadruplets that sum to the target
def fourSum(arr, target):
    res = []
    n = len(arr)
    
    # Sort the array
    arr.sort()

    # Generate quadruplets
    for i in range(n):
      
        # Skip duplicates for i
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n):
          
            # Skip duplicates for j
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            k, l = j + 1, n - 1

            # Two pointers approach
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total == target:
                    res.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1

                    # Skip duplicates for k and l
                    while k < l and arr[k] == arr[k - 1]:
                        k += 1
                    while k < l and arr[l] == arr[l + 1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1

    return res

if __name__ == "__main__":
	arr = [10, 2, 3, 4, 5, 7, 8]
	target = 23
	ans = fourSum(arr, target)
	for v in ans:
		print(" ".join(map(str, v)))