class Date():
    def __init__(self, m, d, y):
        self.m = m
        self.d = d
        self.y = y
    
    def compareTo(self, that):
        if self.y < that.y:
            return -1
        if self.y > that.y:
            return 1
        if self.m < that.m:
            return -1
        if self.m > that.m:
            return 1
        if self.d < that.d:
            return -1
        if self.d > that.d:
            return 1
        return 0
    
    @staticmethod
    def less(v,w):
        return v.compareTo(w) < 0

    @staticmethod
    def exch(a, i, j):
        swap = a[i]
        a[i] = a[j]
        a[j] = swap

    @staticmethod
    def isSorted(a):
        i = 1
        while i < len(a):
            if Date.less(a[i], a[i-1]):
                return False
            i += 1
        return True

dateA = Date(8,20,2018)
dateB = Date(8,21,2018)
dateC = Date(8,23,2018)

a = [dateC, dateB, dateA]

print(Date.isSorted(a))