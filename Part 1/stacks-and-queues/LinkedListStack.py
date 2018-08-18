

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


stack = LinkedListStack()
print("is empty?", stack.isEmpty())
stack.push("node 1")
print("node 1", stack.first.getData())
print(stack.first.getNextNode())
stack.push("node 2")
print("node 2", stack.first.getData())
print(stack.first.getNextNode())
stack.push("node 3")
print("node 3", stack.first.getData())
print(stack.first.getNextNode())
print("pop",stack.pop())
print("after pop", stack.first.getData())
print("is empty?", stack.isEmpty())
