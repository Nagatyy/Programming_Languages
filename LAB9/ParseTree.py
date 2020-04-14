class ParseTree:
    class Node:
        def __init__(self, data, left = None, right = None):
            self.data, self.left, self.right = data, left, right
        def __str__(self):
            return self.data
    def __init__(self, root = None):
        self.root = root
    def __str__(self):
         pass # to be implemented
    def fromPostfix(self, expression=""):
         pass # ...
