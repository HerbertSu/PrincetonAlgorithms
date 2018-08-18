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
        


            