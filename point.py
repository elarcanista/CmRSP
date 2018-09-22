class Point:
    def __init__(self, n, x, y):
        self.id = n
        self.x = x
        self.y = y

    def euclidDistance2(self, p2):
        return (self.x-p2.x)**2 + (self.y-p2.y)**2
