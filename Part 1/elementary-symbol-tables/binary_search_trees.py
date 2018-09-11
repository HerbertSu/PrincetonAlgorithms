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
        
    def fullSize(self):
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


    def keys(self, q):
        # q = Queue() #Queue object
        self.__inorder(self.root, q)
        return q
    
    def __inorder(self, node, q):
        if node == None:
            return
        self.__inorder(node.left, q)
        q.enqueue(node.key)
        self.__inorder(node.right, q)


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


    def put(self, key, value):
        self.root = self.__put(self.root, key, value)    

    def __put(self, node, key, value):
        if node == None:
            return BST.Node(key, value)
        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.val = value
        node.count = 1 + self.size(node.left) + self.size(node.right)
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
bst.put(2,2)
print(bst.get(2))