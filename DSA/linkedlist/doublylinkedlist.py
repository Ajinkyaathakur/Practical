#Linked List- Write a python program to implement Doubly Linear Linked List with following operations
#1. Create 
#2. Insert
#3. Delete
#4. Print node data
#5. Print node values in reverse order
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # New pointer for the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the end of the list
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp  # Update the previous pointer of the new node

    # Delete a node by value
    def delete_node(self, val):
        temp = self.head

        # If the node to be deleted is the head
        if temp and temp.data == val:
            self.head = temp.next
            if self.head:
                self.head.prev = None  # Update the new head's prev pointer
            temp = None
            return

        # Search for the node to be deleted, keep track of the previous node
        while temp and temp.data != val:
            temp = temp.next

        # If the value was not present in the list
        if temp is None:
            print("Node is not present")
            return

        # Unlink the node from the linked list
        if temp.next:
            temp.next.prev = temp.prev  # Update the next node's prev pointer
        if temp.prev:
            temp.prev.next = temp.next  # Update the previous node's next pointer

        temp = None

     # Print the list (for debugging purposes)
    def print_node(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ") 
            temp = temp.next
        print("None")

    # Reverse the linked list
    def reverse_list(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    # Count the number of nodes in the list
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Find the minimum value in the list
    def find_min_max(self):
        if not self.head:
            return None

        min_value = self.head.data
        max_value = self.head.data
        temp = self.head.next
        while temp:
            if temp.data < min_value:
                min_value = temp.data
            elif temp.data > max_value:
                max_value = temp.data
            temp = temp.next
        return (f"minimum value in the list is {min_value} , maximum value in the list is {max_value}")


# Example usage
dl1 = DoublyLinkedList()
dl1.add_node(1)
dl1.add_node(3)
dl1.add_node(5)
dl1.add_node(7)
dl1.add_node(9)

print("Doubly linked List is:")
dl1.print_node()

print("Deleteing the node:")
dl1.delete_node(5)

dl1.print_node()

print("reversing the list")
dl1.reverse_list()

print("Total no of nodes in the list are:",dl1.print_node())

print(dl1.find_min_max())
