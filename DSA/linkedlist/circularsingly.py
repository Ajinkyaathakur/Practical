#Write a program to implement singly circular linked list with append, insert, print and delete operations
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# SinglyCircularLinkedList class
class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    # Append a node to the list
    def append(self, new_node):
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Add a node at a specific position
    def add_node_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            if not self.head:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                new_node.next = self.head
                self.head = new_node
                temp.next = self.head
            return

        current = self.head
        count = 0

        while current.next != self.head and count < position - 1:
            current = current.next
            count += 1

        if current.next == self.head and count < position - 1:
            print("Position out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    # Delete a node by value
    def delete_node(self, val):
        if not self.head:
            print("List is empty")
            return

        temp = self.head

        # If the node to be deleted is the head node
        if temp.data == val:
            if temp.next == self.head:
                self.head = None
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                last.next = self.head.next
                self.head = self.head.next
            return

        prev = None
        while temp.next != self.head and temp.data != val:
            prev = temp
            temp = temp.next

        if temp.data != val:
            print("Node not found")
            return

        prev.next = temp.next

    # Print the list (for debugging purposes)
    def print_list(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example usage
sll = SinglyCircularLinkedList()
sll.append(Node(3))
sll.append(Node(1))
sll.append(Node(7))
sll.append(Node(5))
sll.append(Node(7))

print("Circular Linked List:")
sll.print_list()

print("\nDeleting node with value 1:")
sll.delete_node(1)
sll.print_list()

print("\nInserting node with value 10 at position 2:")
sll.add_node_at_position(10, 2)
sll.print_list()
