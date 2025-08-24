# Allocate Minimum Pages

# Given an array arr[] and an integer k, where arr[i] denotes the number of pages of a book and k denotes total number of students. 
# All the books need to be allocated to k students in contiguous manner, with each student getting at least one book.

# The task is to minimize the maximum number of pages allocated to a student. If it is not possible to allocate books to all students, return -1.

# Input: arr[] = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation: Books can be distributed in following ways:

# [12] and [34, 67, 90] - The maximum pages assigned to a student is  34 + 67 + 90 = 191.
# [12, 34] and [67, 90] - The maximum pages assigned to a student is 67 + 90 = 157.
# [12, 34, 67] and [90] - The maximum pages assigned to a student is 12 + 34 + 67 = 113.
# The third combination has the minimum pages assigned to a student which is 113.

# Input: arr[] = [15, 17, 20], k = 5
# Output: -1
# Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.

# Input: arr[] = [22, 23, 67], k = 1
# Output: 112
# Explanation: Since there is only 1 student, all books are assigned to that student. So, maximum pages assigned to a student is 22 + 23 + 67 = 112.

def isvalid(arr,n,k,mx):

    student = 1
    sum = 0 

    for i in range(0,n):
        sum += arr[i]

        if sum > mx:
            student += 1
            if student > k :
                return False
            sum = arr[i]

    if student == k:
        return True


def allocate_pages(arr,k):

    ## Edge case if len(arr) < k 

    if len(arr) < k:
        return -1 
    

    ## Now we need to find the sum of array 
    end = 0  ## this will be end in binary search list 
    for x in (arr): 
        end += x
    
    start = max(arr) ## find the max value in array which will be our start point 

    res = -1 

    while start <= end:
        mid = start + (end-start) // 2

        if (isvalid(arr,len(arr),k,mid)):
            res = mid
            end = mid - 1

        else:
            start = mid + 1

    return res 


print(allocate_pages( [10,20,30,40],2))