

class Node():
    def __init__(self):
        self.__data = None
        self.__nextNodeAddress = None
        self.__isHead = False
        self.__isTail = False
    

    def getData(self):
        return self.__data

    def getIsHead(self):
        return self.__isHead
    
    def getIsTail(self):
        return self.__isTail

    def changeAddress(self, newAddress):
        self.__nextNodeAddress = newAddress
    
    def changeData(self, newData):
        self.__data = newData
    
    def switchIsTail(self):
        self.__isTail = not self.__isTail
    
    def switchIsHead(self):
        self.__isHead = not self.__isHead





class StackOfStrings():


    def __init__(self):
        self.first = Node()
        self.first.switchIsHead() 
        return
    
    def push(self, item):

        if self.first.getIsHead() == True:
            oldNode = self.first
            self.first = Node()
            self.first.changeData(item)
            self.first.changeAddress(id(oldNode))
        return
    
    def pop(self, item):
        return

    def isEmpty(self):
        if self.first.getData() == None:
            return True
        else:
            return False

    def size(self):
        return


stack = StackOfStrings()
print("is empty?", stack.isEmpty())
stack.push("node 1")
print(stack.first.getData())