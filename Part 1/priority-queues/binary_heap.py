class BinaryHeap:

    def __init__(self,a):
        self.a = a
        self.N = len(self.a) - 1

    def exch(self, i, j):
        swap = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = swap
    
    def less(self,v,w):
        if self.a[v] < self.a[w]:
            return -1 < 0
        else:
            return 0 < 0

    def swim(self, k):
        while k > 1 and self.less(k//2, k):
            self.exch( k//2, k)
            k = k//2
    
    def insert(self, x):
        self.a.append(x)
        self.N = len(self.a) - 1
        self.swim(self.N)
         
    def sink(self, k):
        while 2*k <= self.N:
            j = 2*k
            if j + 1 > self.N:
                pass
            elif self.less(j, j + 1): #Find the larger of the two children
                j += 1

            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def delMax(self):
        self.exch(1, self.N)
        max = self.a.pop()
        self.N = len(self.a) - 1
        self.sink(1)
        return max





a=BinaryHeap([None,16,11,11,10,6,10,8,9,8,5])
# a=BinaryHeap([None, "T","S","R","N","P","O","A","E","I","G","H"])
# a.swim(8)
# a.insert(99)
print("before pop", a.a, "length", a.N)
print(a.delMax())
print("after pop", a.a, "length", a.N)
# print(a.delMax())
# print("after pop", a.a, "length", a.N)
# a.insert("S")
# print("After insert S", a.a, "length", a.N)
         