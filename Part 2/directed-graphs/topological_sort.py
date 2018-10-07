from digraph_api import Digraph

class Node():
    def __init__(self):
        self.__data = None
        self.__nextNode = None
    

    def getData(self):
        return self.__data
    
    def getNextNode(self):
        return self.__nextNode

    def changeNextNode(self, newNode):
        self.__nextNode = newNode
    
    def changeData(self, newData):
        self.__data = newData

class LinkedListStack():


    def __init__(self):
        self.first = Node()
        return
    
    def push(self, item):
        oldNode = self.first
        self.first = Node()
        self.first.changeData(item)
        self.first.changeNextNode(oldNode)
        return
    
    def pop(self):
        item = self.first.getData()
        self.first = self.first.getNextNode()
        return item

    def isEmpty(self):
        if self.first.getData() == None:
            return True
        else:
            return False

    def size(self):
        return


class DepthFirstOrder:
    def __init__(self, G):
        self.marked = [False]*G.V()
        self.reversePost = LinkedListStack()

        v = 0
        while v < G.V():
            if not self.marked[v]:
                self.dfs(G, v)
            v += 1
    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adjacent(v):
            if not self.marked[w]:
                self.dfs(G, w)
        self.reversePost.push(v)
    def returnReversePost(self):
        return self.reversePost





