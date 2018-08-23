class Merge():

    @staticmethod
    def merge(a, aux, lo, mid, hi):
        if not Merge.isSorted(a[lo:mid + 1]):
            return False
        if not Merge.isSorted(a[mid + 1: hi + 1]):
            return False

        k = lo
        while k <= hi:
            aux.append(a[k])
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


a = [1,4,5,2,3,6]
aux=[]
lo = 0
mid = 2
hi = 5
a = Merge.merge(a,aux, lo, mid, hi)
print(a)
