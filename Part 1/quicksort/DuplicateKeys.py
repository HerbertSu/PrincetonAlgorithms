import random

class DuplicateKeys:   
    @staticmethod
    def exch(a, i, j):
        swap = a[i]
        a[i] = a[j]
        a[j] = swap
    
    @staticmethod
    def shuffle(a):
        i = 0
        while i < len(a):
            r = random.randint(0,i)
            DuplicateKeys.exch(a, i, r)
            i += 1

    @staticmethod
    def __sort(a, lo, hi):
        if hi <= lo:
            return
        lt = lo 
        gt = hi
        v = a[lo]
        i = lo

        while i <= gt:
            if a[i] < v:
                DuplicateKeys.exch(a, lt, i)
                lt += 1
                i += 1
            elif a[i] > v:
                DuplicateKeys.exch(a, gt, i)
                gt -= 1
            else:
                i += 1
        
        DuplicateKeys.__sort(a, lo, lt - 1)
        DuplicateKeys.__sort(a, gt + 1, hi)

    @staticmethod
    def sort(a):
        DuplicateKeys.shuffle(a)
        print(a)
        DuplicateKeys.__sort(a, 0, len(a) - 1)

# a = [19,4,19,5,32,6,6,7,6,5,7,5,6]
a = ["K","R","A","T","E","L","E","P","U","I","M","Q","C","X","O","S"]
DuplicateKeys.sort(a)
print(a)
                