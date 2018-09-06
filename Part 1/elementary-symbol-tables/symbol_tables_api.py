class ST:

    def __init__(self, keys):
        self.keys = keys
        self.vals = []
        self.N = len(self.keys)
        return
    
    def put(self, key, value):
        return
    
    def get(self, key):
        if self.isEmpty():
            return None
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            return self.vals[i]
        else:
            return None
        

    def rank(self, key):
        lo = 0
        hi = self.N - 1 
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo 

    def delete(self, key):
        self.put(key, None)
    
    def contains(self, key):
        return self.get(key) != None
    
    def isEmpty(self):
        return
    
    def size(self):
        return
    
    def keys(self):
        return