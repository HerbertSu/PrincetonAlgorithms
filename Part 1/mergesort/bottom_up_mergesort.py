class MergeBU:
    aux = []

    @staticmethod
    def merge(a, aux, lo, mid, hi):
        if not MergeBU.isSorted(a[lo:mid + 1]):
            return False
        if not MergeBU.isSorted(a[mid + 1: hi + 1]):
            return False

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
            elif MergeBU.less(aux[j], aux[i]):
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1
            k += 1

        if not MergeBU.isSorted(a):
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
    def isSorted(a):
        i = 1
        while i < len(a):
            if MergeBU.less(a[i], a[i-1]):
                return False
            i += 1
        return True

    @staticmethod
    def sort(a):
        N = len(a)
        aux = [None]*N

        sz = 1
        while sz < N:
            lo = 0
            while lo < N - sz:
                MergeBU.merge(a, aux, lo, lo + sz - 1, min(lo + sz + sz - 1, N - 1))
                lo += sz + sz
            sz += sz

a = ["M","E","R","G","E","S","O","R","T","E","X","A","M"]
MergeBU.sort(a)
print(a)