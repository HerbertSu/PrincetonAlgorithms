
class LazyPrimMST:
    def __init__(self, G):
        self.pq = MinPQ()
        self.mst = Queue()
        self.marked = [False]*G.V()

        self.visit(G, 0)

        while not self.pq.isEmpty():
            e = pq.delMin()
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.enqueue(e)
            if not self.marked[v]:
                self.visit(G, v)
            if not self.marked[w]:
                self.visit(G, w)
    def visit(self, G, v):
        self.marked[v] = True
        for e in G.adjacent(v):
            if not self.marked[e.other(v)]:
                self.pq.insert(e)
    def returnMST(self):
        return self.mst

