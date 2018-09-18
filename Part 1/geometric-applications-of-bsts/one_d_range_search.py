
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
    
    def contains(self, key):
        node = self.root 
        while node != None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return True
        return False


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
        if node.left != None:
            node.count += self.size(node.left)
        if node.right != None:
            node.count += self.size(node.right)
        node.count += 1
        return node
    
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

    def keys(self):
        array = []
        self.__inorder(self.root, array)
        return array
    
    def __inorder(self, node, array):
        if node == None:
            return
        self.__inorder(node.left, array)
        array.append(node.key)
        self.__inorder(node.right, array)

    def rangeCount(self, lo, hi):
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def rangeSearch(self, lo, hi):
        array = []
        self.__rangeSearch(self.root, lo, hi, array)
        return array

    def __rangeSearch(self, node, lo, hi, array):
        
        if node == None:
            return 

        if node.key < lo:
            self.__rangeSearch(node.right, lo, hi, array)
        elif node.key > hi:
            self.__rangeSearch(node.left, lo, hi, array)
        
        self.__rangeSearch(node.left, lo, hi, array)
        if node.key >= lo and node.key <= hi:
            array.append(node.key)
        self.__rangeSearch(node.right, lo, hi, array)
        return 

root = BST.Node("S","S")
bst = BST(root)
bst.put("E","E")
bst.put("X","X")
bst.put("A","A")
bst.put("C","C")
bst.put("R","R")
bst.put("H","H")
bst.put("M","M")
bst.put("P","P")
bst.put("L","L")
print(bst.keys())
print(bst.rangeSearch('Z', 'X'))