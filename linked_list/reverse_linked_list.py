
class Node:
    def __init__(self,data):
        self.data = data 
        self.nref = None 

class linkedlist:
    def __init__(self):
        self.head = None 

    
    def at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return 
        curr = self.head 
        while curr is not None:

            if curr.nref is None:
                curr.nref = new_node
                break 
            curr = curr.nref 
        return 
    

    def traverse_ll(self):

        if self.head is None:
            print('linked list is empty')
        
        curr = self.head 

        while curr is not None:

            print(f'{curr.data}',end='-->')
            curr = curr.nref 

    def reverse_ll(self):

        if self.head is None:
            return 
        
        if self.head.nref is None:
            return 
        
        prev = None
        curr = self.head 
        

        while curr is not None:
            next = curr.nref 
            curr.nref = prev 
            prev = curr 
            curr = next 
            
            #if next.nref is not None :
                
        
        
        self.head = prev 
        
        



my_ll = linkedlist()
my_ll.at_end(10)
my_ll.at_end(20)
my_ll.at_end(30)
my_ll.at_end(40)
my_ll.at_end(50)
my_ll.traverse_ll()
print('\n')
my_ll.reverse_ll()
my_ll.traverse_ll()