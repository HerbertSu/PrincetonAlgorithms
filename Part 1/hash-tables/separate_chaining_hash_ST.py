class SeparateChainingHashST:
    def __init__(self):
        self.M = 97 #number of chains
        self.st = [None]*self.M #array of chains

    class Node:
        def __init__(self, key, val, next):
            self.key = key
            self.val = val
            self.next = next

    def hash(self, key):
        return abs(hash(key)) % self.M

    def get(self, key):
        i = self.hash(key)
        x = self.st[i]
        while x != None:
            if key == x.key:
                return x.val
            x = x.next
        return None
    
    def put(self, key, val):
        i = hash(key)
        x = self.st[i]
        while x != None:
            if key == x.key:
                x.val = val
                return
        self.st[i] = SeparateChainingHashST.Node(key, val, self.st[i])
