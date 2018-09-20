class IntervalST:

    def __init__(self):
        self.root = None
        return

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

    
    def put(self, lo, hi, val):
        return
    
    def get(self, lo, hi):
        return
    
    def delete(self, lo, hi):
        return
    
    def intersects(self, lo, hi):
        return

    def intervalSearch(self, lo ,hi):
        x = self.root
        while x != None:
            if x.interval.intersects(lo, hi):
                return x.interval
            elif x.left == None:
                x = x.right
            elif x.left.max < lo:
                x = x.right
            else:
                x = x.left
        return None
    
   