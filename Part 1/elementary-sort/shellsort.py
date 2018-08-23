

class Shell():

    @staticmethod
    def sort(a):

        N = len(a)
        h = 1
        while h <= N/3:
            h = 3*h + 1
            
        while h >= 1:
            i = h
            while i < N:
                j = i
                while j >= h and Shell.less(a[j], a[j-h]):
                    Shell.exch(a, j, j-h)
                    j -= h
                i += 1
            h = h//3
                    
            

        return

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
            if Selection.less(a[i], a[i-1]):
                return False
            i += 1
        return True


a = [5,2,3,1]
Shell.sort(a)
print(a)