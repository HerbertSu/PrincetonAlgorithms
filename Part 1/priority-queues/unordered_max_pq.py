class UnorderedMaxPQ:
    def __init__(self):
        self.pq = []
        self.N = None
    
    def isEmpty(self):
        return self.N == None
    
    def insert(self, x):
        if self.isEmpty():
            self.pq.append(x)
            self.N = 1
        else:
            self.pq.append(x)
            self.N += 1
    
    def delMax(self):
        max = 0
        i = 1
        while i < self.N:
            if self.pq[max] < self.pq[i - 1]:
                max = i-1
            i += 1
        lastValue = self.pq[self.N-1]
        self.pq[self.N - 1] = self.pq[max]
        self.pq[max] = lastValue
        return self.pq.pop()

        
a = UnorderedMaxPQ()
a.insert(4)
a.insert(3)
a.insert(19)
a.insert(93)
a.insert(33)
print(a.delMax())
print(a.pq)
