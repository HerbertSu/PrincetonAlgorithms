class QuickUnionUF():

    def __init__(self, id):
        self.__id = id
        self.__sz = []
    
    def get_id(self):
        return self.__id
    def get_sz(self):
        return self.__sz

    def QuickUnionUF(self, N):
        self.__id = [None]*N
        self.__sz = [1]*N
        i=0
        for element in self.__id:
            self.__id[i] = i
            i += 1


    def __root(self, i):
        # Commented out code is me trying to implement setting all elements
            # examined above i to the root. This flattens it
        # root = i
        # while root != self.__id[root]:
        #     root = self.__id[root]
        
        while i != self.__id[i]:
            self.__id[i] = self.__id[self.__id[i]]
            i = self.__id[i]
            # self.__id[i] = root
            
        return i
    
    def connected(self, p, q):
        return self.__root(self.__id[p]) == self.__root(self.__id[q])

    def union(self, p, q):
        i = self.__root(p)
        j = self.__root(q)
        if self.__sz[i] < self.__sz[j]:
            self.__id[i] = j
            self.__sz[j] += self.__sz[i]
        else:
            self.__id[j] = i
            self.__sz[i] += self.__sz[j]
        self.__root(q)
        return

union = QuickUnionUF([])
union.QuickUnionUF(10)
print(union.get_id())
union.union(6,5)
print("union(6,5)")
print("id", union.get_id())
print("sz", union.get_sz())
print("\n")
union.union(4,3)
print("union(4,3)")
print("id", union.get_id())
print("sz", union.get_sz())
print("\n")

union.union(9,2)
print("union(9,2)")
print("id", union.get_id())
print("sz", union.get_sz())
print("\n")
union.union(4,2)
print("union(4,2)")
print("id", union.get_id())
print("sz", union.get_sz())
print("\n")
