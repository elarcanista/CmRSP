import math
import point

class Instance:
    def __init__(self, v0, u, w, m=1, q=math.inf):
        self.v0 = v0
        self.U = u
        self.W = w
        self.m = m
        self.q = q
        self.V = {i.id: i for i in (u+w)}
        self.V[0] = point.Point(0, v0.x, v0.y)
        self.V[self.size()] = v0

    def __str__(self):
        return "{m = " + str(self.m) + \
                 ", q = " + str(self.q) + \
                 ", v0 = " + str(self.v0) + \
                 ", u = " + str(self.u) + \
                 ", Steiner nodes = " + str(self.w) + \
                 "}"

    def size(self):
        return len(self.U) + len(self.W) + 1
