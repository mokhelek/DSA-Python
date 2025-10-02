"""
Singly Linked List Utilities

This module provides a singly linked list implementation with common operations: append, prepend, insert, delete, search, reverse, detect cycle, and find middle.
"""

#%%
# todo -> CREATE A SINGLE LINKED LIST

class Node:
    def __init__(self, value):
        self.value = value  #? THE ACTUAL DATA WE WANT TO STORE
        self.next = None  #?  THE POINTER TO THE NEXT NODE 
        
        
class LinkedList:
    def __init__(self):
        self.head = None  #? THE FIRST ELEMENT OF THE LIST, INITIALLY NULL
        self.size = 0   #? KEEPING TRACK OF THE SIZE OF THE LIST 
        
        
    def is_empty(self):
        # check if list is empty
        return self.head is None 
    
    
    def __len__(self):
        # return size/ num of nodes 
        return self.size
    
    
    def prepend(self, value):
        # ? Inserting a new node at the beginning of the list O(1)
        new_node = Node(value)
        new_node.next = self.head 
        self.head =  new_node 
        self.size += 1 
        
        
    def append(self, value):
        new_node = Node(value) 
        
        if self.is_empty():
            self.head = new_node 
        else:
            # ? Traverse all the way to last node ( O(n) time )
            
            current = self.head # because we start traversing from the head
            
            while current.next is not None:
                current =  current.next 
                
            current.next = new_node 
            
        self.size += 1
        
        
    def insert_at(self, value, index):
        # ? Insert data at a specific index 
        
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            new_node = Node(value)
            current =  self.head   # starting point for the traversing
            
            for _ in range(index - 1): 
                current = current.next 
            
            # Update pointers
            new_node.next = current.next
            current.next = new_node
            self.size += 1
        
        
    def delete(self, value):
        # ? Delete first occurrence of data
        
        if self.is_empty():
            raise ValueError("List is empty")
        
        if self.head.value == value:
            self.head = self.head.next 
            self.size -= 1 
            return  
        
        # Traverse the list to find the node to delete
        current = self.head
        
        while current.next is not None:
            if current.next.value == value:
                current.next == current.next.next
                self.size -= 1
                return 
            current = current.next 
            
        raise ValueError("Data not found in list")
    
    
    def search(self, value):
        # ? Check if value exist in linked list  
        
        if self.is_empty():
            return False 
        
        current = self.head # starting point for the traversal
        
        while current is not None:
            if current.value == value:
                return True 
            current = current.next 
            
        return False 
    
    
    def get_at(self, index):
        # ? Get data at a specific index (0-based)
        
        if index < 0 or index >= self.size:
            return IndexError("Index is out of bound") 
        
        current = self.head    # ? start traversing from the head 
        
        for _ in range(index):
            current = current.next
        
        return current.value 
    
    
    def __str__(self):
        
        elements = [] 
        current =  self.head 
        
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements) + " -> None"
        
    
    def reverse(self):
        # ? Reverse the linked list using the iterative method
        
        current_node = self.head  # start traversing from the head
        previous_node = None   # points to previous Node
        next_node = None  # points to next Node
        
        while current_node is not None:
            # * Store the next node to ensure we have access to it before overriding
            
            next_node = current_node.next

            # * WE REVERSE THE LINK !! 
            
            current_node.next = previous_node     
            
            # * Move forward
            
            previous_node =  current_node 
            current_node =  next_node
            
        # ! Assign the head to the previous node    
        self.head = previous_node
        
    
    def has_cycle(self):
        
        # Handle empty list or single node without cycle
        if self.head is None or self.head.next is None:
            return False
        
        slow_pointer = self.head  # Moves one node at a time
        fast_pointer = self.head  # Moves two nodes at a time
        
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next         # Move slow by 1
            fast_pointer = fast_pointer.next.next    # Move fast by 2
            
            # If they meet, there's a cycle
            if slow_pointer == fast_pointer:
                return True
        
        # If fast reaches end, no cycle
        return False
    
    
    def find_middle(self):
        # ? Find the middle node of the linked list using the fast/slow pointer approach.
      
        if self.is_empty():
            return -1 
        
        slow_pointer = self.head 
        fast_pointer = self.head  
        
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer =  slow_pointer.next
          
        return slow_pointer.value
    
    
    
#?################################################################## TESTING ##################################################################?#  

linked_list = LinkedList()

# Append some data
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)  

# Prepend data
linked_list.prepend(5) 

print( linked_list )

linked_list.reverse() 

print(linked_list)

print("middle :", linked_list.find_middle())


# %%
