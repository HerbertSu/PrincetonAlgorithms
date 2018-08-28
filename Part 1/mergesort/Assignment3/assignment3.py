
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #Check if self point is less than that point
    def compareTo(self, that):
        if self.y == that.y:
            if Point.less(self.x, that.x):
                return True
            else:
                return False
        else:
            return Point.less(self.y, that.y)
    
    def slopeTo(self, that):
        if self.y == that.y and self.x == that.x:
            slope = -math.inf
        elif self.y == that.y:
            slope = 0
        elif self.x == that.x:
            slope = math.inf
        else:
            slope = (that.y - self.y) / (that.x - self.x)
        return slope

    #that1's slope is less than that2's slope
    def slopeOrder(self, that1, that2):
        inf = math.inf 
        if Point.less(self.slopeTo(that1), self.slopeTo(that2)):
            return True
        else:
            return False
        


    @staticmethod
    def less(v,w):
        if v < w:
            return -1 < 0
        elif v > w:
            return 1 < 0
        else:
            return 0 < 0


point1 = Point(0,0)
point2 = Point(3,3)
point3 = Point(0,2)

print(point1.slopeOrder(point3,point2))