class Quicksort:
    
    @staticmethod
    def partition(a, lo, hi):
        #commented portion is my code
        # i = 1
        # j = hi
        # condition = True
        # while condition:
            
        #     if a[i] < a[lo]:
        #         i += 1
        #     else:
        #         if a[j] > a[lo]:
        #             j -= 1
        #         else:
        #             auxi = a[i]
        #             a[i] = a[j]
        #             a[j] = auxi
        #             i += 1
        #             j -= 1
        #     if j <= i:
        #         auxlo = a[lo]
        #         a[lo] = a[j]
        #         a[j] = auxlo
        #         condition = False
        # return j
        i = lo + 1
        j = hi 
        while True:
            while Quicksort.less(a[i], a[lo]):
                i += 1
                if i == hi:
                    break
            while Quicksort.less(a[lo], a[j]):
                j -= 1
                if j == lo:
                    break
            if i >= j:
                break
            Quicksort.exch(a, i, j)
        Quicksort.exch(a, lo, j)
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

a=["a","b","c"]
# a = ["K","R","A","T","E","L","E","P","U","I","M","Q","C","X","O","S"]
lo = 0
hi = len(a) - 1
print(Quicksort.partition(a,lo,hi))
print(a)