

class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def ccw(a, b, c):
        area2 = (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)
        if area2 < 0:
            return -1
        elif area2 > 0:
            return 1
        else:
            return 0
    
a = Point2D(0,0)
b = Point2D(1, 1)
c = Point2D(2,0)

print(Point2D.ccw(a,b,c))
