
class node:
     def __init__(self, value):
          self.data = value
          self.next = None

class circular_queue:
     def __init__(self):
          self.front = self.rear = None

     def enqueue(self, new_node):
          if self.rear:  # When the queue is not empty
               self.rear.next = new_node
               self.rear = new_node
               self.rear.next = self.front  # Point the rear's next to the front node to make it circular
          else:  # When the queue is empty
               self.front = self.rear = new_node
               self.rear.next = self.front  # Point to itself to form a single circular node

     def print(self):
          if self.front is None:  # Empty queue
               print("Queue is empty!")
               return
          temp = self.front
          while True:
               print(temp.data, "-> ", end='')
               temp = temp.next
               if temp == self.front:  # Stop when we loop back to the front
                    break
          print()

     def dequeue(self):
          if self.front is None:  # Empty queue
               print("Queue is empty!!")
               return
          temp = self.front
          if self.front == self.rear:  # Single element case
               print("Node deleted: ", temp.data)
               self.front = self.rear = None
          else:
               print("Node deleted: ", temp.data)
               self.front = self.front.next  # Move the front pointer to the next node
               self.rear.next = self.front  # Update the rear's next pointer to the new front node
          del temp 

# Create and use the circular queue
que = circular_queue()
que.enqueue(node(10))
que.enqueue(node(20))
que.enqueue(node(30))
que.enqueue(node(40))
que.enqueue(node(50))
que.enqueue(node(60))
que.enqueue(node(70))
que.enqueue(node(80))
que.enqueue(node(90))

# Printing and deleting nodes from the circular queue
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()

