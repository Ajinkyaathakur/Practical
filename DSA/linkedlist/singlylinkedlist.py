#linked List- Write a python program to implement Singly Linear Linked List with following operations
#1. Create                                               
#2. Insert                                               
#3. Delete                                               
#4. Print                                                
#5. Reverse                                              
#6. Count Nodes                                          
#7. Find Min and Max value Nodes
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglylinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the end of the list
    def add_node(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Delete a node by value
    def delete_node(self,val):
        temp = self.head
        
        if temp and temp.data == val: #if node to be deleted is head
            self.head = temp.next
            temp = None
            return
        
        # Search for the node to be deleted, keep track of the previous node
        prev = None
        while temp and temp.data != val:
            prev =temp
            temp = temp.next
            
        # If the value was not present in the list
        if temp is None:
            print ("Node not present in the List")
            return
        
        # Unlink the node from the linked list
        prev.next = temp.next
        temp = None

    def print_node(self):
        temp = self.head
        while temp:
            print(temp.data,end=">")
            temp = temp.next
        print("None")

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def min_max(self):
        if not self.head:
            return None
        min_value = self.head.data
        max_value = self.head.data
        temp = self.head.next
        while temp :
            if temp.data < min_value:
                min_value = temp.data
            elif temp.data > min_value:
                max_value = temp.data
            temp = temp.next
        return (f"minimum value in the list is {min_value} , maximum value in the list is {max_value}")

#testing usage
sl1 = SinglylinkedList()
sl1.add_node(1)
sl1.add_node(3)
sl1.add_node(5)
sl1.add_node(7)
sl1.add_node(9)

print("Singly linked List is:")
sl1.print_node()

print("Deleteing the node:")
sl1.delete_node(5)

sl1.print_node()

print("reversing the list")
sl1.reverse_list()

print("Total no of nodes in the list are:",sl1.print_node())

print(sl1.min_max())
