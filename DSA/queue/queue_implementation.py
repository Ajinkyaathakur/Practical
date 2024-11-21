# queue implementation

class node:
     def __init__(self,value):
          self.data = value
          self.next = None

class linear_queue:
     def __init__(self):
          self.front = self.rear = None

     def enqueue(self,new_node):
          if self.rear:
               self.rear.next = new_node
               self.rear = new_node
          else:
               self.front = self.rear = new_node
               return

     def print(self):
          temp = self.front
          while temp:
               print(temp.data,"-> ", end= '' )
               temp = temp.next
          print()

     def dequeue(self):
          if self.rear != None:
               temp = self.front
               #print("Node deleted  ",temp.data)
               self.front = self.front.next
               if self.front == None:
                    self.rear = None
               del temp
          else:
               print("Queue is empty!!")

que = linear_queue()
que.enqueue(node(10))
que.enqueue(node(20))
que.enqueue(node(30))
que.enqueue(node(40))
que.enqueue(node(50))
que.enqueue(node(60))
que.enqueue(node(70))
que.enqueue(node(80))
que.enqueue(node(90))
#que.enqueue(node(100))


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
que.dequeue()
que.print()
que.dequeue()
que.print()

