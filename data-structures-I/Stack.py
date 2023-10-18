####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.is_empty())
stack.pop()
print(stack.peek())
print(stack.size())
stack.pop()
stack.pop()
stack.pop()
print(stack.size())
stack.pop()
print(stack.is_empty())
