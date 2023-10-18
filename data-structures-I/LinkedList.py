####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def remove(self, value):
        if self.head is None:
            return None
        
        if self.head.value == value:
            self.head = self.head.next
            return 
        
        prev = None
        curr = self.head
        while curr and curr.value != value:
            prev = curr
            curr = curr.next

        if curr is None:
            return
        
        prev.next = curr.next
    
    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False




llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(6)
llist.print_list()
print("Linked list before deletion:")
llist.remove(2)
llist.print_list()
print("Linked list after deletion:")
llist.search(3)