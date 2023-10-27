class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def __str__(self, level=0):
        def leaf_str():
            return '\t' * (level+1) + 'None\n'
        
        tree_str = '\t' * level + repr(self.value) + '\n'

        for child in [self.left, self.right]:
            tree_str += child.__str__(level+1) if child else leaf_str()