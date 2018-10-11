from edge_weighted_graph import EdgeWeightedGraph

class QuickUnionUF():

    def __init__(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id

    def QuickUnionUF(self, N):
        self.__id = [None]*N
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
        self.__id[i] = j
        return

class KruskalMST:

    mst = Queue()

    def __init__(self, G):
        self.pq = MinPQ() 
        for e in G.edges():
            self.pq.insert(e)

        self.uf = UF(G.V())
        while not self.pq.isEmpty() and mst.size() < G.V() - 1:
            e = self.pq.delMin()
            v = e.either()
            w = e.other(v)
            if not self.uf.connected(v,w):
                uf.union(v, w)
                mst.enqueue(e)
    
    def edges(self):
        return mst


