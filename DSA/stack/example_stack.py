class node:
     def __init__(self,value):
          self.data = value
          self.next = None

class stack:
     def __init__(self):
          self.top = None

     #add an element to the top of the stack
     def push(self,new_node):
          new_node.next = self.top
          self.top = new_node

     #remove an element that is at the top of the stack that is latest added/pushed element
     def pop(self):
          temp = self.pop
          print("Popped element: ",temp.data)
          self.top = temp.next
          del temp

     # Display the stack
     def print(self):
          temp = self.top
          print("Stack contains... ")
          while temp:
               print(temp.data)
               temp = temp.next

st = stack()
