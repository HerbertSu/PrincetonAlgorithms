class binarySearch():
# Unfinished
    def __init__(self, a, key):
        self.__a = a
        self.__key = key
        self.__aLow = 0
        self.__aHigh = len(a) - 1
        self.__found = False
        self.__index = 0
    
    def findMiddleIndex(self):
        aSize = len(self.__a)
        if aSize <= 1:
            return 0
        elif aSize%2 == 0:
            return aSize//2 - 1 
        else:
            return aSize//2
    
    def get_a(self):
        return self.__a

    def checkMiddle(self):

        while self.__found == False:

            if len(self.__a) <= 1:
                if self.__a[0] != self.__key:
                    return False

            else:
                middleIndex = self.findMiddleIndex()
                print("a", self.__a)
                print("middleIndex", middleIndex)

                if self.__a[middleIndex] == self.__key:
                    self.__index = middleIndex
                    self.__found = True
                    print("true")
                # what if item doesn't exist?
                elif self.__key < self.__a[middleIndex]:
                    self.__aHigh = middleIndex 
                    self.__a = self.__a[self.__aLow: middleIndex]

                else:
                    self.__aLow = middleIndex + 1
                    self.__a = self.__a[middleIndex + 1: self.__aHigh]

        return self.__index
    
    
            

    



binary = binarySearch([1,2,3,4,5], 0)
print(binary.checkMiddle())
print(binary.get_a())