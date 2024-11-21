class Node:
    def __init__(self, value, priority):
        self.data = value
        self.next = None
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        # If the queue is empty, insert the new node at the front
        if self.front is None:
            self.front = self.rear = new_node
        else:
            # If the new node has a higher priority than the front, insert it at the front
            if new_node.priority < self.front.priority:
                new_node.next = self.front
                self.front = new_node
            else:
                # Traverse the queue find the correct position
                temp = self.front
                while temp.next and temp.next.priority <= new_node.priority:
                    temp = temp.next
                
                new_node.next = temp.next
                temp.next = new_node

                # If the new node is added at the end, update the rear pointer
                if new_node.next is None:
                    self.rear = new_node

    def print_queue(self):
        temp = self.front
        while temp:
            print(f"(Value: {temp.data}, Priority: {temp.priority}) ->", end=" ")
            temp = temp.next
        print("None")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty!!")
            return
        else:
            temp = self.front
            print(f"Node deleted: {temp.data}")
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            del temp


# Example usage
que = PriorityQueue()
que.enqueue(Node(10, 3))
que.enqueue(Node(20, 1))
que.enqueue(Node(30, 2))
que.enqueue(Node(40, 5))
que.enqueue(Node(50, 4))

que.print_queue()

que.dequeue()
que.print_queue()

que.dequeue()
que.print_queue()

que.dequeue()
que.print_queue()

que.dequeue()
que.print_queue()

que.dequeue()
que.print_queue()
