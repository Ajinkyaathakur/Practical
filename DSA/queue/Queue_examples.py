# Queue implementation using a list
class Queue:
    def __init__(self):
        self.queue = []

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Add an element to the rear of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to the queue.")

    # Remove an element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty."
        return self.queue.pop(0)

    # View the front element of the queue without removing it
    def peek(self):
        if self.is_empty():
            return "Queue is empty."
        return self.queue[0]

    # Display the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current Queue:", self.queue)

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

print(f"Dequeued element: {queue.dequeue()}")
queue.display()

print(f"Front element is: {queue.peek()}")
