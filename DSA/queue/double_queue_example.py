class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoubleEndedQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue_front(self, value):
        new_node = Node(value)
        if self.front is None:  # If the deque is empty
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def enqueue_rear(self, value):
        new_node = Node(value)
        if self.rear is None:  # If the deque is empty
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def dequeue_front(self):
        if self.front is None:
            print("Deque is empty!")
            return
        temp = self.front
        print(f"Node deleted from front: {temp.data}")
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # If it was the only node
        else:
            self.front.prev = None
        del temp

    def dequeue_rear(self):
        if self.rear is None:
            print("Deque is empty!")
            return
        temp = self.rear
        print(f"Node deleted from rear: {temp.data}")
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None  # If it was the only node
        else:
            self.rear.next = None
        del temp

    def print_queue(self):
        temp = self.front
        while temp:
            print(f"{temp.data} ->", end=" ")
            temp = temp.next
        print("None")

# Example usage
deque = DoubleEndedQueue() 
deque.enqueue_front(10)
deque.enqueue_front(20)
deque.enqueue_rear(30)
deque.enqueue_rear(40)

deque.print_queue()

deque.dequeue_front()
deque.print_queue()

deque.dequeue_rear()
deque.print_queue()

deque.dequeue_front()
deque.print_queue()

deque.dequeue_rear()
deque.print_queue()
 
