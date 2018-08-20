class Node():
    def __init__(self):
        self.data = None
        self.nextNode = None
        self.previousNode = None

class Deque():

    def __init__(self):
        self.front = Node()
        self.back = self.front
        self.size = 0
    
    def isEmpty(self):
        return (self.front.data == None) and (self.back.data == None)

    def size(self):
        return self.size

    def addFirst(self,item):
        if self.isEmpty():
            self.front.data = item
            self.size += 1
            return
        
        oldFront = self.front
        self.front = Node()
        self.front.data = item
        
        if self.size == 1: 
            self.front.nextNode = self.back
            self.back.previousNode = self.front
            self.size += 1
        else:
            self.front.nextNode = oldFront
            oldFront.previousNode = self.front
            self.size += 1
            
    def addLast(self,item):
        if self.isEmpty():
            self.back.data = item
            self.size += 1
            return
        
        oldBack = self.back
        self.back = Node()
        self.back.data = item
        
        if self.size == 1: 
            self.front.nextNode = self.back
            self.back.previousNode = self.front
            self.size += 1
        else:
            self.back.previousNode = oldBack
            oldBack.nextNode = self.back
            self.size += 1
            
    def removeFirst(self):
        if self.isEmpty():
            return "deque is empty"
        elif self.size == 1:
            oldFront = self.front
            self.front = Node()
            self.back = self.front
            self.size -= 1
            return oldFront.data
        else:
            oldFront = self.front
            self.front = self.front.nextNode

            if oldFront.nextNode == self.back:
                self.back.previousNode = self.front

            self.size -= 1
            return oldFront.data

    def removeLast(self):
        if self.isEmpty():
            return "deque is empty"
        elif self.size == 1:
            oldBack = self.back
            self.back = Node()
            self.front = self.back
            self.size -= 1
            return oldBack.data
        else:
            oldBack = self.back
            self.back = self.back.previousNode

            if oldBack.previousNode == self.front:
                self.front.nextNode = self.back

            self.size -= 1
            return oldBack.data

    def iterator(self):
        return Deque.LinkedListIterator(self)

    class LinkedListIterator():
        def __init__(self, deque_node):
            self.i = deque_node.front
        
        def hasNext(self):
            return self.i != None
        
        def next(self):
            current = self.i
            self.i = self.i.nextNode
            return current.data
    


deque = Deque()

deque.addLast("3")
deque.addLast("2")
deque.addLast("1")



deque.addFirst("3")
# print("after adding first item 3 to the front")
# print("front.data",deque.front.data)
# print("back.data", deque.back.data)

deque.addFirst("2")
# print("after adding second item 2 to the front")
# print("front.data",deque.front.data)
# print("back.data", deque.back.data)
# print("front.data.nextNode", deque.front.nextNode.data)
# print("back.data.previousNode", deque.back.previousNode.data)
        
deque.addFirst("1")
# print("after adding third item 1 to the front")
# print("front.data",deque.front.data)
# print("front.nextNode.data", deque.front.nextNode.data)
# print("front.nextNode.nextNode.data", deque.front.nextNode.nextNode.data)
# print("back.previousNode.previousNode.data", deque.back.previousNode.previousNode.data)
# print("back.previousNode.data", deque.back.previousNode.data)
# print("back.data", deque.back.data)

deque.addLast("4")
# print("after adding first item 4 to the back")
# print("front.data",deque.front.data)
# print("back.data", deque.back.data)

deque.addLast("5")
# print("after adding second item 5 to the back")
# print("front.data",deque.front.data)
# print("back.data", deque.back.data)
# print("front.data.nextNode", deque.front.nextNode.data)
# print("back.data.previousNode", deque.back.previousNode.data)
        
deque.addLast("6")
# print("after adding third item 6 to the back")
# print("front.data",deque.front.data)
# print("front.nextNode.data", deque.front.nextNode.data)
# print("front.nextNode.nextNode.data", deque.front.nextNode.nextNode.data)
# print("back.previousNode.previousNode.previousNode.data", deque.back.previousNode.previousNode.previousNode.data)
# print("back.previousNode.previousNode.data", deque.back.previousNode.previousNode.data)
# print("back.previousNode.data", deque.back.previousNode.data)
# print("back.data", deque.back.data)

i = deque.iterator()
while i.hasNext():
    print(i.next())