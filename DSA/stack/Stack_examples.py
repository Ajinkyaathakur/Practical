# Stack implementation using a list
class Stack:
    def __init__(self):
        self.stack = []

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Add an element to the top of the stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    # Remove the top element of the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        return self.stack.pop()

    # View the top element of the stack without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        return self.stack[-1]

    # Display the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current Stack:", self.stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

print(f"Popped element: {stack.pop()}")
stack.display()

print(f"Top element is: {stack.peek()}")
