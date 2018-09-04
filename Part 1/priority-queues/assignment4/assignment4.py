class Board:
    def __init__(self,n):
        self.blocks = [[None]*n]*n

    def dimension(self):
        return self.n

    
board = Board(3)
print(board.blocks)