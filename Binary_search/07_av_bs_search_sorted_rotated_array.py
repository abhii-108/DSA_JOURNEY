class searchrotated_bs:
    def __init__(self,arr,x):
        self.arr = arr
        self.x = x 

    def rotated_count(self,arr):
        left, right = 0, len(self.arr)-1



        while left <= right:
            if arr[left] <= arr[right]:
                return left

            mid = left + (right - left) // 2
            next = (mid+1) % len(arr)
            prev = (mid-1+len(arr)) % len(arr)

            #print(f'prev -->{prev} mid-->{mid} next-->{next} ')

            if (arr[mid] <= self.arr[next]) and (arr[mid] <= arr[prev]):
                return mid 
            
            if arr[mid] >= arr[left]:
                left = mid + 1
            else:
                right = mid - 1  
            
        return -1
    
    def binary_search(self,b_arr,x):
        left = 0 
        print(b_arr)
        right = len(b_arr)-1

        while left <= right:
            mid = left + (right - left) // 2

            if b_arr[mid] == x:
                return mid 
            
            elif b_arr[mid] < x:
                left = mid + 1 
            else:
                right = mid - 1 
        return -1 
    
    def search_in_rotated_sorted(self):

        mid_val = self.rotated_count(self.arr)
        val1 = self.binary_search(self.arr[:mid_val], self.x)
        val2 = self.binary_search(self.arr[mid_val:], self.x) + mid_val

        if val1 == -1 :
            return val2
        elif val2 == -1 :
            return val1
        else:
            return -1 
        

find = searchrotated_bs([4,5,6,7,0,1,2],0)

print(find.search_in_rotated_sorted())








