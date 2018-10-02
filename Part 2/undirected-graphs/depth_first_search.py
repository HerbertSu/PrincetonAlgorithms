from graph_api import Graph 

class DepthFirstPaths:
    def __init__(self, G, s):
        self.marked = []
        self.edgeTo = []
        self.s = s
        self.G = G

        self.dfs(self.G, s)
        
    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj:
            if not self.marked[w]:
                self.dfs(G, w)
                self.edgeTo[w] = v
    

