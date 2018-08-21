class Insertion():
    @staticmethod
    def less(v,w):
        if v < w:
            return -1 < 0
        elif v > w:
            return 1 < 0
        else:
            return 0 < 0
    
    @staticmethod
    def exch(a, i, j):
        swap = a[i]
        a[i] = a[j]
        a[j] = swap

    @staticmethod
    def isSorted(a):
        i = 1
        while i < len(a):
            if Insertion.less(a[i], a[i-1]):
                return False
            i += 1
        return True
    
    @staticmethod
    def sort(a):
        i = 0
        N = len(a)
        while i < N:
            j = i
            while j > 0:
                if Insertion.less(a[j], a[j-1]):
                    Insertion.exch(a, j, j-1)
                else:
                    break
                j -= 1
            i += 1

a = [5,2,3,1]
Insertion.sort(a)
print(a)