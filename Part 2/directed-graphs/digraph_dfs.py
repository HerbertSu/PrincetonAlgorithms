
from digraph_api import Digraph

class DirectedDFS:
    def __init__(self, G, s):
        self.marked = [False]*G.V()
        self.dfs(G,s)
    
    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adjacent(v):
            if not self.marked[w]:
                self.dfs(G, w)
    
    def visited(self, w):
        return self.marked[w]
