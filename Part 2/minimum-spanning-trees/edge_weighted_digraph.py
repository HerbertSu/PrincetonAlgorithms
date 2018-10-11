class EdgeWeightedDigraph:
    def __init__(self, V):
        self.V = V
        self.adj = [None]*V
        v = 0
        while v < V:
            self.adj[v] = Bag()
            v += 1
    def addEdge(self, e):
        v = e.from()
        self.adj[v].add(e)
    def adjacent(self, v):
        return self.adj[v]