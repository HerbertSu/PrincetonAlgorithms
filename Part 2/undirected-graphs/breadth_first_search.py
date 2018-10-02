from graph_api import Graph

class Node():
    def __init__(self):
        self.item = None
        self.nextNode = None

class Queue():
    def __init__(self):
        self.first = Node()
        self.last = Node()
        return
    
    def isEmpty(self):
        return self.first.item == None
    
    def enqueue(self, item):
        oldLast = self.last

        mostRecentNode = Node()
        mostRecentNode.item = item
        
        if self.isEmpty():
            self.first = mostRecentNode
        else:
            oldLast.nextNode = mostRecentNode

        return

    def dequeue(self):
        oldestNode = self.first
        self.first = self.first.nextNode 
        if self.isEmpty():
            self.last = None       
        return oldestNode.item
        
class BreadthFirstPaths:
    def __init__(self):
        self.marked = []
        self.edgeTo = []
        #initalize graph

    def bfs(self, G, s):
        q = Queue()
        q.enqueue(s)
        self.marked[s] = True
        while not q.isEmpty():
            v = q.dequeue()
            for w in G.adjacent(v):
                if not self.marked[w]:
                    q.enqueue(w)
                    self.marked[w] = True
                    self.edgeTo[w] = v
    
                    

            
            