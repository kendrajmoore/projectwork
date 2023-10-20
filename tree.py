class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return
        current = self.root
        while current:
            if key < current.value:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.value:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return
            
    def search(self, key):
        current = self.root
        while current:
            if key == current.value:
                return True
            elif key < current.value: 
                current = current.left
            else:
                current = current.right

        return False


    def inorder_traversal(self):
        res = []
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.value)
            current = current.right
        return res
    

bst = BinaryTree()
values = [50, 30, 20, 40, 70, 60, 80]
for v in values:
    bst.insert(v)

print("In-order Traversal:", bst.inorder_traversal())
print("Search 25:", bst.search(25))
print("Search 70:", bst.search(70))
