
class Selection():
    
    @staticmethod
    def sort(a):
        N = len(a)
        i = 0
        while i < N:
            min = i
            j = i + 1
            while j < N:
                if Selection.less(a[j], a[min]):
                    min = j
                j += 1
            Selection.exch(a, i, min)
            i += 1



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
            if Date.less(a[i], a[i-1]):
                return False
            i += 1
        return True

a = [5,2,3,1]
Selection.sort(a)
print(a)