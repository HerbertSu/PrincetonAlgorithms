class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    def from(self):
        return self.v
    def to(self):
        return self.w
    def weight(self):
        return self.weight