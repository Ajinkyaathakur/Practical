class Node:
    def __init__(self, value, priority):
        self.data = value
        self.next = None
        self.priority = priority

class DoubleEndedPriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue_front(self, new_node):
        # Enqueue at the front according to priority
        if self.front is None:  # Queue is empty
            self.front = self.rear = new_node
        elif new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            # Find the right position to insert
            temp = self.front
            while temp.next and temp.next.priority <= new_node.priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            if new_node.next is None:
                self.rear = new_node

    def enqueue_rear(self, new_node):
        # Always enqueue at the rear without priority check
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue_front(self):
        if self.front is None:
            print("Queue is empty!")
            return
        temp = self.front
        print(f"Node deleted from front: {temp.data}")
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        del temp

    def dequeue_rear(self):
        if self.rear is None:
            print("Queue is empty!")
            return
        if self.front == self.rear:  # Only one node in the queue
            print(f"Node deleted from rear: {self.rear.data}")
            self.front = self.rear = None
        else:
            # Traverse to the second last node
            temp = self.front
            while temp.next != self.rear:
                temp = temp.next
            print(f"Node deleted from rear: {self.rear.data}")
            temp.next = None
            self.rear = temp

    def print_queue(self):
        temp = self.front
        while temp:
            print(f"(Value: {temp.data}, Priority: {temp.priority}) ->", end=" ")
            temp = temp.next
        print("None")

# Example usage
deque = DoubleEndedPriorityQueue()
deque.enqueue_front(Node(10, 3))
deque.enqueue_front(Node(20, 1))
deque.enqueue_front(Node(30, 2))
deque.enqueue_rear(Node(40, 5))
deque.enqueue_rear(Node(50, 4))

deque.print_queue()

deque.dequeue_front()
deque.print_queue()

deque.dequeue_rear()
deque.print_queue()

deque.dequeue_front()
deque.print_queue()

deque.dequeue_rear()
deque.print_queue()

deque.dequeue_front()
deque.print_queue()
