class Merge():

    @staticmethod
    def __sort(a, aux, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) // 2
        print("lo to mid sorting", lo, "to", mid)
        Merge.__sort(a, aux, lo, mid)
        print("mid + 1 to hi sorting", mid + 1, "to", hi)
        Merge.__sort(a, aux, mid + 1, hi)
        
        print("Merge.merge lo:",lo,"mid:",mid,"hi",hi)
        # print("a before Merge.merge",a )
        b = Merge.merge(a, aux, lo, mid, hi)
        # print("Merge.merge()", a)
    
    @staticmethod
    def sort(a):
        aux = [None]*len(a)
        Merge.__sort(a, aux, 0, len(a) -1)

    @staticmethod
    def merge(a, aux, lo, mid, hi):
        if not Merge.isSorted(a[lo:mid + 1]):
            # print("lo to mid not sorted")
            return False
        if not Merge.isSorted(a[mid + 1: hi + 1]):
            # print("mid + 1 to hi not sorted")
            return False

        # print("merging")
        k = lo
        while k <= hi:
            aux[k] = a[k]
            k += 1

        i = lo
        j = mid + 1
        k = lo

        while k <= hi:    
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif Merge.less(aux[j], aux[i]):
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1
            k += 1

        if not Merge.isSorted(a):
            return False
        return a


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
            if Merge.less(a[i], a[i-1]):
                return False
            i += 1
        return True


# a = [0,1,4,5,2,3,6]
a = ["M","E","R","G","E","S","O","R","T","E","X","A","M","P","L","E"]
aux=[]
lo = 0
mid = 2
hi = 5
# a = Merge.merge(a,aux, lo, mid, hi)
Merge.sort(a)
print(a)
    