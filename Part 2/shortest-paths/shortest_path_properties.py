
class ShortestPath:
    def __init__(self):
        return
    def distanceTo(self, v):
        return self.distTo[v]
    def pathTo(self, v):
        path = Stack()
        e = self.edgeTo[v]
        while e != None:
            path.push(e)
            e = self.edgeTo[e.from()]
        return path
    