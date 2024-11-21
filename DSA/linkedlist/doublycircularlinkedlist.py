#Write a program to implement doubly circular linked list with append, insert, print and delete operations
# Node class for Doubly Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# DoublyCircularLinkedList class
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # Append a node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    # Insert a node at a specific position
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            if not self.head:
                self.head = new_node
                new_node.next = self.head
                new_node.prev = self.head
            else:
                last = self.head.prev
                new_node.next = self.head
                new_node.prev = last
                self.head.prev = new_node
                last.next = new_node
                self.head = new_node
            return

        current = self.head
        count = 0
        while current.next != self.head and count < position - 1:
            current = current.next
            count += 1
        
        if current.next == self.head and count < position - 1:
            print("Position out of bounds")
            return

        next_node = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next = next_node
        next_node.prev = new_node

    # Delete a node by value
    def delete(self, value):
        if not self.head:
            print("List is empty")
            return

        temp = self.head

        # If the node to be deleted is the head node
        if temp.data == value:
            if temp.next == self.head:  # Only one node in the list
                self.head = None
            else:
                last = self.head.prev
                last.next = self.head.next
                self.head.next.prev = last
                self.head = self.head.next
            return

        # Search for the node to delete
        while temp.next != self.head and temp.data != value:
            temp = temp.next

        if temp.data != value:
            print("Node not found")
            return

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    # Print the list
    def print_list(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example usage
dll = DoublyCircularLinkedList()
dll.append(3)
dll.append(1)
dll.append(7)
dll.append(5)

print("Doubly Circular Linked List:")
dll.print_list()

print("\nInserting 10 at position 2:")
dll.insert(10, 2)
dll.print_list()

print("\nDeleting node with value 1:")
dll.delete(1)
dll.print_list()
