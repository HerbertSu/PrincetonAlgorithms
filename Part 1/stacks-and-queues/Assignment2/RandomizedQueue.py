import random

class RandomizedQueue():
    def __init__(self):
        self.RandomizedQueue = []
        self.size = 0

    def isEmpty(self):
        return self.RandomizedQueue == []

    def enqueue(self, item):
        self.RandomizedQueue.append(item)
        self.size += 1
    
    def sample(self):
        if not self.isEmpty():
            return self.RandomizedQueue[random.randint(0,self.size)]
        else:
            return False

    def dequeue(self):
        if not self.isEmpty():
            self.size -= 1
            return self.RandomizedQueue.pop(random.randint(0,self.size))
        else:
            return "Empty queue"
    
    def iterator(self):

        return RandomizedQueue.RandomArrayIterator(self)
    
    class RandomArrayIterator():
        def __init__(self, RQ):
            self.RQ = RQ
            self.i = 0
            self.randomIndexes = random.sample(range(0,RQ.size), RQ.size)
        
        def hasNext(self):
            if self.i < self.RQ.size:
                return True
            else:
                return False

        def next(self):
            oldIndex = self.randomIndexes[self.i]
            self.i += 1
            return self.RQ.RandomizedQueue[oldIndex]
               
    

            


rq = RandomizedQueue()
rq.enqueue("a")
rq.enqueue("b")
rq.enqueue("c")
rq.enqueue("4")
rq.enqueue("32")
rq.enqueue("6")
print(rq.RandomizedQueue)
i = rq.iterator()
while i.hasNext():
    print(i.next())

