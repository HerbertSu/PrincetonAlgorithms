import random

class Selection:
    
    @staticmethod
    def selection(a, k):
        Selection.shuffle(a)
        lo = 0
        hi = len(a) - 1
        while hi > lo:
            j = Selection.partition(a, lo, hi)
            if k < j:
                hi = j - 1
            elif k > j:
                lo = j + 1
            else:
                return a[k]
    
        return a[k]

    @staticmethod
    def shuffle(a):
        i = 0
        while i < len(a):
            r = random.randint(0,i)
            Selection.exch(a, i, r)
            i += 1

    @staticmethod
    def partition(a, lo, hi):
        i = lo + 1
        j = hi 
        while True:
            while Selection.less(a[i], a[lo]):
                i += 1
                if i == hi:
                    break
            while Selection.less(a[lo], a[j]):
                j -= 1
                if j == lo:
                    break
            if i >= j:
                break
            Selection.exch(a, i, j)
        Selection.exch(a, lo, j)
        return j


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


# a = ["K","R","A","T","E","L","E","P","U","I","M","Q","C","X","O","S"]
a= [1,2,3,4,5,6,7,8]

print(Selection.selection(a,7))
