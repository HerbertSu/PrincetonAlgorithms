class QuickUnionUF():

    def __init__(self, id):
        self.__id = id
        self.__sz = []
    
    def get_id(self):
        return self.__id

    def QuickUnionUF(self, N):
        self.__id = [None]*N
        self.__sz = [1]*N
        i=0
        for element in self.__id:
            self.__id[i] = i
            i += 1


    def __root(self, i):
        while i != self.__id[i]:
            i = self.__id[i]
        return i
    
    def connected(self, p, q):
        return self.__root(self.__id[p]) == self.__root(self.__id[q])

    def union(self, p, q):
        i = self.__root(p)
        j = self.__root(q)
        if sz[i] < sz[j]:
            self.__id[i] = j
            sz[j] += sz[i]
        else:
            self.__id[j] = i
            sz[i] += sz[j]
        return

union = QuickUnionUF([])
union.QuickUnionUF(10)
print(union.get_id())