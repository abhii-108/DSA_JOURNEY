#Add 1 to a number represented as linked list

# A number is represented in linked list such that each digit corresponds to a node in linked list. The task is to add 1 to it.

# Input: head: 4 -> 5 -> 6
# Output: head: 4 -> 5 -> 7
# Explanation: Adding 1 to number represented by Linked List = 456 + 1 = 457
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def helper(tmp):

    if tmp is None:
        return 1 

    carry = helper(tmp.next)
    sum = tmp.data + carry
    tmp.data = sum % 10 
    return sum//10

    # sum = tmp.data + carry
    
    # if sum < 10:
    #     return 0
    # tmp.data = 0
    # return 1

def addition(head):

    carry = helper(head)

    if (carry == 1):
        newNode = Node(1)
        newNode.next = head 
        head = newNode
    #print_list(head)
    return head 

def print_list(node):
    while node:
        print(node.data, end="-->")
        node = node.next
    print()

if __name__ == "__main__":

    # head1 = Node(1)
    # head1.next = Node(2)
    # head1.next.next = Node(3)

    # Creating second linked list 4->5->6->7->8
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)

    head2 = Node(9)
    head2.next = Node(9)
    head2.next.next = Node(9)

    print_list(head)
    
    op = addition(head)
    print_list(op)

    print_list(head2)
    op2 = addition(head2)
    print_list(op2)

    
###################### deep seek op ####################
    
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

def helper(tmp):
    """Recursive helper function to add 1 to the number represented by the linked list.
    
    Args:
        tmp: Current node being processed
        
    Returns:
        Carry value to be added to the previous digit
    """
    # Base case: reached end of list (least significant digit)
    if tmp is None:
        return 1  # Return carry=1 since we're adding 1 to the number
    
    # Recursive call to process next node (more significant digit first)
    carry = helper(tmp.next)
    
    # Add current digit value with carry from lower digits
    total = tmp.data + carry
    
    # Update current digit (keep only units place)
    tmp.data = total % 10 
    
    # Return carry for next higher digit
    return total // 10

def addition(head):
    """Main function to add 1 to a number represented as a linked list.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        New head of the modified linked list
    """
    # Special case: empty list
    if head is None:
        return Node(1)  # Return [1] if list was empty
    
    # Start recursive addition process
    carry = helper(head)
    
    # If final carry exists after processing all digits
    if carry == 1:
        # Create new node with carry value (new most significant digit)
        newNode = Node(1)
        # New node points to original head
        newNode.next = head 
        # Update head to new node
        head = newNode
    
    return head