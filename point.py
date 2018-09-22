import math

class Point:
    def __init__(self, n, x, y):
        self.id = n
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.id) + \
               ", " + str(self.x) + \
               ", " + str(self.y) + ")"

    def __repr__(self):
        return str(self)

    def euclidDistance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)
