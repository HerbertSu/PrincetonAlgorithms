import math
class DijkstraSP:
    def __init__(self, G, s):
        self.edgeTo = [None]*G.V()
        self.distTo = [math.inf]*G.V()
        self.pq = IndexMinPQ(G.V())

        self.distTo[s] = 0
        self.pq.insert(s, 0.0)
        while not self.pq.isEmpty():
            v = self.pq.delMin()
            for e in G.adjacent(v):
                self.relax(e)
    def relax(e):
        v = e.from()
        w = e.to()
        if self.distTo[w] > self.distTo[v] + e.weight():
            self.distTo[w] = self.distTo[v] + e.weight()
            self.edgeTo[w] = e
            if self.pq.contains(w):
                self.pq.decreaseKey(w, self.distTo[w])
            else:
                self.pq.insert(w, self.distTo[w])