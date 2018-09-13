class RB_BST:
    
    def __init__(self, root):
        self.root = root

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.count = 0
        

    def get(self, key):
        x = self.root
        while x != None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None