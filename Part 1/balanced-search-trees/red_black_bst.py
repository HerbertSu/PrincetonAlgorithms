BLACK = False
RED = True

class RB_BST:
    

    def __init__(self, root):
        self.root = root

    class Node:
        def __init__(self, key, val, color):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.count = 0 
            self.color = color
        
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

    def put(self, key, value):
        self.root = self.__put(self.root, key, value)
       

    def __put(self, node, key, value):
        if node == None:
            return RB_BST.Node(key, value, RED)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.val = value

        if self.__isRed(node.right) and not self.__isRed(node.left):
           node = self.rotateLeft(node)
        if self.__isRed(node.left) and self.__isRed(node.left.left):
            node = self.rotateRight(node)
        if self.__isRed(node.left) and self.__isRed(node.right):
            self.flipColors(node)
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node


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

    def fullSize(self):
        return self.root.count
    
    def size(self, node):
        if node == None:
            return None
        return node.count
    

    def rank(self, key):
        return self.__rank(key, self.root)

    def __rank(self, key, node):
        if node == None:
            return 0
        if key < node.key:
            return self.__rank(key, node.left)
        elif key > node.key:
            return 1 + self.size(node.left) + self.__rank(key, node.right)
        else:
            return self.size(node.left)

    def floor(self, key):
        node = self.__floor(self.root, key)
        if node == None:
            return None
        return node.key

    def __floor(self, node, key):
        if node == None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self.__floor(node.left,key)
        
        t = self.__floor(node.right, key)
        if t != None:
            return t
        else:
            return node