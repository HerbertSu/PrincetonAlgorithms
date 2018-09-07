class BST:

    def __init__(self, root):
        self.root = root

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
    
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
            node.left = BST.__put(node.left, key, value)
        elif key > node.key:
            node.right = BST.__put(node.right, key, value)
        else:
            node.val = value
        return node

bst = BST(BST.Node(1,1))
bst.put(0,0)
print(bst.get(2))