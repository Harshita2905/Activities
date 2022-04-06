# creaking stack class with list
class stack:
    def __init__(self):
        self.items = []

    #method to check the stack is empty or not
    def isempty(self):
        return self.items == []
    
    #method for pushing item
    def push(self, item):
        self.items.append(item)

    #method for popping an item
    def pop(self):
        return self.items.pop()

    #check what item is on top of the stack without removing it
    def peek(self):
        return self.items[-1]

    #method to get the size
    def size(self):
        return len(self.items)
    
    #to view the entire stack
    def fullstack(self):
        return self.items

stack = stack()
print('Current stack:', stack.fullstack())
print('Stack empty?:', stack.isempty())
print('Pushing integer 1')
stack.push(1)
print('Pushing string "Told you, I am generic stack!"') 
stack.push('Told you, I am generic stack!') 
print('Pushing integer 3')
stack.push(3)
print('Current stack:', stack.fullstack()) 
print('Popped item:', stack.pop())
print('Current stack:', stack.fullstack())
print('Stack empty?:', stack.isempty())