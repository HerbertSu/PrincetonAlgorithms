class LinearProbingHashST:
    def __init__(self):
        self.M = 30001
        self.vals = [None]*self.M
        self.keys = [None]*self.M

    
    def hash(self, key):
        return abs(hash(key)) % self.M

    def put(self, key, val):
        i = self.hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                break
            i = (i + 1) % self.M
        self.vals[i] = val
        self.keys[i] = key
        
    def get(self, key):
        i = self.hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                return self.vals[i]
            i = (i + 1) % self.M
        return None