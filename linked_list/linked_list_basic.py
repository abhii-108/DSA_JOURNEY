###### Basic Linked List ##########
import time
class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None

class LinkedList:
    def __init__(self):
        self.head = None 

    ## Now I want to add node at the beginning of the list 
    
    def at_begin(self,data):
        newNode = Node(data)
        #check if linked list is empty or not 
        if self.head is None:
            self.head = newNode 
            return
        # newnode nref is pointing to none after creation so it need to point current first node 
        # Location of current first Node is at head hence newNode next ref is point to head first 
        # Then change the pointing of head to new Node 
        newNode.nref = self.head
        self.head = newNode 

    def at_end(self, data):
        newNode = Node(data)

        #check if linked list is empty or not
        if self.head is None:
            self.head = newNode 
            return 

        # We create a temp variable name curr pointing at the location of head/first node 
        # This is use to traversal the node from head to last node 
        curr = self.head

        # While condition is used to check if we next node is not none. It will stop at last node 
        # For last node nref is pointint to null we need to make it point to new node 
        while curr.nref is not None:
            curr = curr.nref # This is kind of counter to move the curr pointer to next node 
        
        curr.nref = newNode 
        return

    def after_specific_node(self,data,x):
        
        #check if linkedlist is empty or not 

        if self.head is None:
            print('Given node is not present in Empty Linked List')
            return 

        curr = self.head 

        while curr is not None:
            if curr.data == x :
                newNode = Node(data)
                newNode.nref = curr.nref  ## Assume if we adding to last node then null value will be there is curr.nref. If x is in middle then this line is important. 
                curr.nref = newNode  ## current ref will point to newNode 
                return 
            curr = curr.nref
        print('Give After specific node value not found in LinkedList ')
        return 

    
    def before_specific_node(self, data, x ):

        #check if LinkedList is empty or not 
        if self.head is None:
            print('Given node is not present in Empty Linked List..!')
            return 
        if self.head.data == x:
            newNode = Node(data)
            newNode.nref = self.head
            self.head = newNode 
            return 
        
        curr = self.head 

        while curr.nref is not None:
            if curr.nref.data == x :
                newNode = Node(data)
                newNode.nref = curr.nref
                curr.nref = newNode 
                return 
            curr = curr.nref 
        print('Give before specific node value not found in LinkedList ')
        return 

    def traverse_ll(self):
        if self.head is None:
            print('LinkedList you are finding is empty')

        curr = self.head 

        while curr is not None:
            print(f'{curr.data}', end="-->")
            curr = curr.nref 

    ################################### Now Node deletion ##############################
    def ll_check(self):
        if self.head is None:
            print('LinkedList you are finding is empty.. Hence cant delete first node ')
            return True

    
    def del_at_start(self):
        # if self.head is None:
        #     print('LinkedList you are finding is empty.. Hence cant delete first node ')
        #     return 
        if self.ll_check(): return 
        self.head = self.head.nref 
        return 
    
    def del_at_end(self):
        # if self.head is None:
        #     print('LinkedList you are finding is empty.. Hence cant delete last node ')
        #     return
        if self.ll_check(): return 
        
        curr = self.head

        while curr.nref.nref is not None:
            curr = curr.nref 

        curr.nref = None 

    def del_by_val(self,x):
        if self.ll_check(): return 

        curr = self.head

        if curr.data == x :
            self.head = curr.nref
            return 
        
        while curr.nref is not None:
            if curr.nref.data == x :
                curr.nref = curr.nref.nref 
            curr = curr.nref 

        return 


        


        

        





my_ll = LinkedList()
my_ll.traverse_ll()
my_ll.del_at_start()
my_ll.del_at_end()
print('----------1----------',end='\n')
my_ll.at_begin(10)
my_ll.at_begin(5)
my_ll.at_begin(2)
my_ll.at_end(20)
my_ll.at_end(40)
my_ll.at_end(60)
#my_ll.traverse_ll()
print('----------2----------',end='\n')
my_ll.traverse_ll()
#time.sleep(2)
my_ll.before_specific_node(30,40)
#time.sleep(2)
print('----------3----------',end='\n')
my_ll.del_at_start()
my_ll.del_at_end()
my_ll.after_specific_node(35,30)
my_ll.del_by_val(10)
my_ll.traverse_ll()









