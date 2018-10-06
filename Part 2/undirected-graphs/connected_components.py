

class CC:
    def __init__(self, G):
        self.id = [None]*G.V()
        self.count = 0
        self.marked = [False]*G.V()

        v = 0
        while v < G.V():
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1
            v += 1
    
    def componentCount(self):
        return self.count

    def componentId(self, v):
        return self.id[v]

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adjacent(v):
            if not self.marked[w]:
                self.dfs(G, w)



        