class Node:
    def __init__(self,data):
        self.data = data 
        self.nref = None 

class Ciruclar_ll:
    def __init__(self):
        self.last = None 

    ## Add Node at the begining of the circular Linked List 

    def at_begin(self,data):
        new_node = Node(data)

        if self.last == None:
            self.last = new_node
            self.last.nref = new_node
            return
  
        new_node.nref = self.last.nref  
        self.last.nref  = new_node

        return 
    
    ## Add Node at the End of the circular Linked List 

    def at_end(self,data):
        new_node = Node(data)

        if self.last == None:
            self.last = new_node
            new_node.nref = new_node
            return
        
      
        new_node.nref = self.last.nref
        self.last.nref = new_node
        self.last = new_node

        return
    
    ## Dispaly / traversal of circular linked list 
    def display_cll(self):

        if self.last == None:
            print('circular linked list is empty', end='\n')
            return 
        
        curr = self.last.nref 

        while True:
            print(f'{curr.data}', end="-->")
            
            curr = curr.nref 
            if curr == self.last.nref:
                break
         
    
        # while curr != self.last :
        ## looking for alternative while conditions 
        #     print(f'{curr.data}', end="-->")
            
    ## Insert a node after a specific key 
    
    def inset_after_key(self,data,x):

        if self.last == None:
            print('Linked List is empty...!')
            return 
        
        curr = self.last.nref 

        while True :
            if curr.data == x and curr == self.last:
                new_node = Node(data)
                new_node.nref = self.last.nref 
                curr.nref = new_node
                self.last = new_node
                break 
            elif curr.data == x :
                new_node = Node(data)
                new_node.nref = curr.nref 
                curr.nref = new_node
                break 

            curr = curr.nref 
            if curr == self.last.nref:
                print(f'{x} node is not present in linked list..!')
                break 
        return 
    
    ## To delete node from begining of circular linked list 
    def del_at_start(self):

        if self.last == self.last.nref or self.last is None:
            self.last = None 
            return 

        #print(f'last value in cc is {self.last.data}')   ## testing 

        self.last.nref = self.last.nref.nref 
        #print(f'last value in cc is {self.last.data}') ## testing 
        return 

    ## to delete node from end of circular linked list 

    def del_at_end(self):

        if self.last == self.last.nref or self.last is None:
            self.last = None 
            return 
        
        curr = self.last.nref

        while True:
            if curr.nref == self.last:
                curr.nref = self.last.nref
                self.last = curr 
                break 
            curr = curr.nref 

    

        


            

    

my_cll = Ciruclar_ll()
my_cll.at_begin(10)
my_cll.at_begin(5)
#my_cll.display_cll()
my_cll.at_end(20)
my_cll.at_end(39)
my_cll.inset_after_key(25,20)
my_cll.inset_after_key(7,5)
my_cll.inset_after_key(49,39)
my_cll.display_cll()
print('----------',end="\n")
my_cll.del_at_end()
my_cll.display_cll()
print(end="\n")
my_cll.del_at_start()
my_cll.display_cll()
            





        
