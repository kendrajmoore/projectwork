####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def is_empty(self):
        return len(self.items) == 0
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
