class Percolation():
    
    def __init__(self, n):
        #create a grid
        self.__grid = [None]*n
        self.__id = [None]*n*n
        self.__n = n
        
        i = 0
        for element in self.__id:
            self.__id[i] = i
            i+=1

        rowArray = [None]*n
        rowArrayIndex = 0
        element = 0
        gridRow = 0

        while gridRow < n:
            
            while rowArrayIndex < n:
                rowArray[rowArrayIndex] = element
                element += 1
                rowArrayIndex += 1
            rowArrayIndex = 0
            self.__grid[gridRow] = rowArray
            rowArray = [None]*n
            gridRow += 1
    
    def get_grid(self):
        return self.__grid

    def get_id(self):
        return self.__id
        
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

    def __connected(self, p, q):
        return
    
    def __union(self, p, q):
        return

    def open(self, row, col):
        if col == 1 or col == self.__n:
            if row == 1 or row == self.__n:
        
        
        return 
    
    def isOpen(self, row, col):
        return
    
    def isFull(self, row, col):
        return
    
    def numberOfOpenSites(self):
        return
    
    def percolates(self):
        return





        
percolate = Percolation(3)
print(percolate.get_grid())
print(percolate.get_id())
