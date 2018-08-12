import random
import math

class Percolation():
    
    def __init__(self, n):
        #create a grid
        self.__grid = [None]*n
        self.__id = [None]*n*n
        self.__n = n
        self.__sz = [1]*n*n
        self.__numberOfOpenSites = 0
        # self.__topVirtualSite = [-1]*n
        # self.__botVirtualSite = [n]*n
        
        i = 0
        for element in self.__id:
            self.__id[i] = i
            i+=1

        i = 0
        for element in self.__grid:
            self.__grid[i] = [None]*n
            i += 1
        
    
    def __root(self, i):
        
        while self.__id[i] != i:
            self.__id[i] = self.__id[self.__id[i]]
            i = self.__id[i]
        return i



    def __connected(self, p, q):
        return self.__root(self.__id[p]) == self.__root(self.__id[q]) 
    
    def __union(self, p, q):
        i = self.__root(p)
        j = self.__root(q)

        if self.__sz[i] < self.__sz[j]:
            self.__id[i] = j
            self.__sz[j] += self.__sz[i]
        else:
            self.__id[j] = i
            self.__sz[i] += self.__sz[j]
        return

    def get_sz(self):
        return self.__sz

    def get_grid(self):
        return self.__grid

    def get_id(self):
        return self.__id
    
    def __getElementFromRowCol(self, row, col):
        if row >= 1 and row <= self.__n and col >= 1 and col <= self.__n:
            return self.__grid[row - 1][col - 1]
        else:
            return False

    def __rowColToIndex(self, row, col):
        return self.__n*(row - 1) + col -1
    
    def __indexToRowCol(self, index):
        
        if (index + 1) > self.__n:
            col = (index % self.__n) + 1
            row = (int((index + 1 - col)/self.__n) + 1)
        else:
            col = index + 1
            row = 1

        return [row, col]

    def isFull(self, row, col):

        if self.isOpen(row,col):
            for element in self.__grid[0]:
                if element != None:
                    if self.__connected(element, self.__id[self.__rowColToIndex(row,col)]):
                        return True
            return False
        else:
            return False
     

    def isOpen(self, row, col):
        if self.__grid[row-1][col-1] == None:
            return False
        else: 
            return True

    def open(self, row, col):
        if self.isOpen(row, col):
            return 
        else:
            self.__numberOfOpenSites += 1
            index = self.__rowColToIndex(row,col)
            self.__grid[row-1][col-1] = index

            # checking which ones to connect to
            # only 4 that you need to check [ (row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
            if self.__getElementFromRowCol(row, col - 1) != None and self.__getElementFromRowCol(row, col - 1) != False:
                self.__union(self.__getElementFromRowCol(row, col), self.__getElementFromRowCol(row, col - 1))

            if self.__getElementFromRowCol(row, col + 1) != None and self.__getElementFromRowCol(row, col + 1) != False:
                self.__union(self.__getElementFromRowCol(row, col), self.__getElementFromRowCol(row, col + 1))
            
            if self.__getElementFromRowCol(row - 1, col) != None and self.__getElementFromRowCol(row - 1, col) != False:
                self.__union(self.__getElementFromRowCol(row, col), self.__getElementFromRowCol(row - 1, col))
            
            if self.__getElementFromRowCol(row + 1, col) != None and self.__getElementFromRowCol(row + 1, col) != False:
                self.__union(self.__getElementFromRowCol(row, col), self.__getElementFromRowCol(row + 1, col))

        return 
    
    
    
    def numberOfOpenSites(self):
        return self.__numberOfOpenSites
    
    def percolates(self):
        for element in self.__grid[self.__n - 1]:
            if element != None:
                row = self.__indexToRowCol(element)[0]
                col = self.__indexToRowCol(element)[1]
                
                if self.isFull(row, col):
                    return True
        return False


        return





n = 20
nsq = n*n
runs = 20
pList = []
runningSum = 0
p = 0

percolate = Percolation(n)
condition = False

for run in [None]*runs:
    while condition == False:
        
        row = random.randint(1, n)
        col = random.randint(1, n)
        percolate.open(row,col)
        if percolate.percolates():
            condition = True
            p = float(percolate.numberOfOpenSites())/(nsq)
            # print(p)
    condition = False
    pList.append(p)
    runningSum += p

# print(pList)
average = float(runningSum)/runs

ssqNum = 0
for p in pList:
    ssqNum += (p - average)*(p - average)

ssq = float(ssqNum)/(runs - 1)
s = math.sqrt(ssq)

stdev = float(1.96*s)/(math.sqrt(runs))

bottomP = average - stdev
upperP = average + stdev

print(average)
print("percolation p is between for n=", n, "and runs", runs, [bottomP, upperP])






# print(percolate.get_grid())
# print(percolate.get_id())
# print("after open (1,1)")
# percolate.open(1,1)
# print(percolate.get_grid())
# print(percolate.get_id())
# print("percolates?", percolate.percolates())

# print("isFull 1,1", percolate.isFull(1,1))
# print("isFull 3,3", percolate.isFull(3,3))
# print("after open (1,2)")
# percolate.open(1,2)
# print(percolate.get_grid())
# print(percolate.get_id())
# print(percolate.get_sz())
# print("percolates?", percolate.percolates())

# print("isFull 3,3", percolate.isFull(3,3))
# print("after open (2,2)")
# percolate.open(2,2)
# print(percolate.get_grid())
# print(percolate.get_id())
# print("percolates?", percolate.percolates())

# print("isFull 3,3", percolate.isFull(3,3))
# print("after open (3,2)")
# percolate.open(3,2)
# print(percolate.get_grid())
# print(percolate.get_id())
# print("isFull 3,2", percolate.isFull(3,2))
# print("percolates?", percolate.percolates())

# print("isFull 3,3", percolate.isFull(3,3))
# print("after open (3,3)")
# percolate.open(3,3)
# print(percolate.get_grid())
# print(percolate.get_id())
# print("isFull 3,3", percolate.isFull(3,3))
# print("number of opened sites", percolate.numberOfOpenSites())
# print("percolates?", percolate.percolates())

