class ArrayStack():

    def __init__(self, capacity):
        self.s = [None]*capacity
        self.N = 0
    
    def isEmpty(self):
        return self.N == 0

    def push(self, item):
        self.s[self.N] = item
        self.N += 1

    def pop(self):
        item = self.s[N]
        self.s[self.N] = None
        self.N -= 1
        return item