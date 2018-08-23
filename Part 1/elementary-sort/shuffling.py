import random

class Shuffle():

    @staticmethod
    def shuffle(a):
        N = len(a)
        i = 0
        while i < len(a):
            r = random.randint(0,i)
            Shuffle.exch(a, i, r)
            i += 1


    @staticmethod
    def exch(a, i, j):
        swap = a[i]
        a[i] = a[j]
        a[j] = swap

a = [1,2,3,4,5]
Shuffle.shuffle(a)
print(a)