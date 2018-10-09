class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    def either(self):
        return self.v
    
    def other(self, vertex):
        if vertex == self.v:
            return self.w
        else:
            return self.v

    def compareTo(self, that):
        if self.weight > that.weight:
            return 1
        elif self.weight < that.weight:
            return -1
        else:
            return 0