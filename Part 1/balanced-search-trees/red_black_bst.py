

class RB_BST:
    BLACK = False
    RED = True

    def __init__(self, root):
        self.root = root

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.count = 0 
        
    def rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED 
        return x

    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def flipColors(self, h):
        h.color = RED
        h.right.color = BLACK
        h.left.color = BLACK

    def __isRed(self, node):
        if node == None:
            return False
        return node.color == RED

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