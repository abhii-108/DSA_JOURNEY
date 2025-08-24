# Third largest element in an array of distinct elements

# Given an array of n integers, the task is to find the third largest element. All the elements in the array are distinct integers. 

# Examples : 

# Input: arr[] = {1, 14, 2, 16, 10, 20}
# Output: 14
# Explanation: Largest element is 20, second largest element is 16 and third largest element is 14

# Input: arr[] = {19, -10, 20, 14, 2, 16, 10}
# Output: 16
# Explanation: Largest element is 20, second largest element is 19 and third largest element is 16 


def thirdLargest(arr):
    m1 = float('-inf')
    m2 = float('-inf')
    m3 = float('-inf')

    for i in range(0,len(arr)):
        if arr[i] > m1:
            
            m3 = m2
            m2 = m1
            m1 = arr[i]
        elif arr[i] < m1 and arr[i] > m2 :
            m3 = m2
            m2 = arr[i]
        elif arr[i] > m3:
            m3 = arr[i]

    return m3

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    #arr2 =  [0, 0]
    print(thirdLargest(arr))
    print(thirdLargest([10, 30, 0]))
    print(thirdLargest([19, -10, 20, 14, 2, 16, 10]))