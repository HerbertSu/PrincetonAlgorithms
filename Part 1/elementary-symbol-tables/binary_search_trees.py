class BST:

    def __init__(self, root):
        self.root = root

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.count = 0
        
    def size(self):
        return self.root.count
    
    def size(self, node):
        if node == None:
            return None
        return node.count
    
    def get(self, key):
        node = self.root 
        while node != None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.val
        return None


    def put(self, key, value):
        self.root = self.__put( self.root, key, value)    

    def __put(self, node, key, value):
        if node == None:
            return BST.Node(key, value)
        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.val = value
        return node

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
        

bst = BST(BST.Node(1,1))
bst.put(0,0)
print(bst.get(2))