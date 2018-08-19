

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
        if self.isEmpty():
            self.first = Node()
            self.first.changeData(item)
        else:
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

    def iterator(self):
        return LinkedListStack.ListIterator(self)


    class ListIterator():
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            self.current = outer_instance.first

        def hasNext(self):
            return self.current.getNextNode() != None
        
        def next(self):
            currentData = self.current.getData()
            print(currentData, "'s next node points to", hex(id(self.current.getNextNode())))
            self.current = self.current.getNextNode()
            print("new current has data", self.current.getData())
            
            return currentData
    
    

    


stack = LinkedListStack()
print("empty stack's has data", stack.first.getData())
print("empty stack's has nextNode", stack.first.getNextNode())

stack.push("node 1")
print("node 1's nextNode points to",stack.first.getNextNode())

stack.push("node 2")
print("node 2's nextNode points to",stack.first.getNextNode())
stack.push("node 3")
print("node 3's nextNode points to",stack.first.getNextNode())


i = stack.iterator()

while i.hasNext():
    data = i.next()
