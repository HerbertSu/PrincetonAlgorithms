from topological_sort import DepthFirstOrder

class KosarajuSharirSCC:
    def __init__(self, G):
        self.marked = [False]*G.V()
        self.id = [None]*G.V()
        self.count = 0

        dfo = DepthFirstOrder(G.reverse())
        for v in dfo.returnReversePost():
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = Truef
        self.id[v] = self.count
        for w in G.adjacent(v):
            if not self.marked[w]:
                self.dfs(G, w)
    
    def stronglyConnected(self, v, w):
        return self.id[v] == self.id[w]

        