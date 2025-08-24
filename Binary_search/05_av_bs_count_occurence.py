class bsoccurence:
    def __init__(self,arr,x):
        self.arr = arr
        self.x = x 

    def first_occurence(self):

        start, end = 0, len(self.arr)-1
        res = -1 

        while start <= end:

            mid = start + (end-start)//2

            if self.arr[mid] == self.x :
                res = mid 

                end = mid - 1

            elif self.arr[mid] > self.x:
                end = mid - 1 
            else:
                start = mid + 1 
        
        return res 

    def last_occurence(self):
        start, end = 0, len(self.arr) - 1
        res = -1 

        while start <= end:

            mid = start + (end - start) // 2

            if self.arr[mid] == self.x :
                res = mid 
                start = mid + 1 

            elif self.arr[mid] > self.x :
                end = mid - 1

            else:
                start = mid + 1
        return res 
    
    def count_occurence(self):
        first = self.first_occurence()
        last = self.last_occurence()

        if first == -1 :
            return -1 
        else:
            return last-first+1
        

get_count_occ = bsoccurence([1, 3, 5, 5, 5, 5, 7, 123, 125 ],5)

print(get_count_occ.count_occurence())