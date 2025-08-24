# Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), peek() and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must have a time complexity of O(1). 


# Input: queries = [push(2), push(3), peek(), pop(), getMin(), push(1), getMin()]
# Output: [3, 2, 1] 

class SpecialStack:
    def __init__(self):
        self.st = []
        self.min_ele = -1 

    def push(self,x):
        if not self.st:
            self.st.append(x)
            self.min_ele = x 
        
        elif x < self.min_ele:
            self.st.append(2*x - self.min_ele)
            self.min_ele = x 

        else:
            self.st.append(x)

    
    def pop(self):
        if not self.st:
            return -1 
        
        top = self.st.pop()

        if top < self.min_ele:
            self.min_ele = (2 * self.min_ele - top)

    
    def peek(self):
        if not self.st:
            return -1 
        
        top = self.st[-1]

        if top < self.min_ele:
            return self.min_ele
        else:
            return top
        
    
    def get_min(self):
        if not self.st:
            return -1
        
        return self.min_ele
    


        

if __name__ == '__main__':
    ss = SpecialStack()
    
    # Function calls
    ss.push(2)
    ss.push(3)
    print(ss.peek(), end=" ")
    ss.pop()
    print(ss.get_min(), end=" ")
    ss.push(1)
    print(ss.get_min(), end=" ")