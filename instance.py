import math
import point

class Instance:
    def __init__(self, v0, u, w, m=1, q=math.inf):
        self.v0 = v0
        self.u = u
        self.w = w
        self.m = m
        self.q = q
        self.v = {i.id: i for i in (u+w)}
        self.v[0] = point.Point(0, v0.x, v0.y)
        self.v[self.size()] = v0

    def __str__(self):
        return "{m = " + str(self.m) + \
                 ", q = " + str(self.q) + \
                 ", v0 = " + str(self.v0) + \
                 ", u = " + str(self.u) + \
                 ", Steiner nodes = " + str(self.w) + \
                 "}"

    def size(self):
        return len(self.u) + len(self.w) + 1

def genTest(nodes, alpha=1, m=1, q=math.inf):
    nodes = list(map(lambda i: point.Point(*i), nodes))
    v0 = nodes.pop(-1)
    u = nodes[:math.floor( alpha*len(nodes) )]
    w = nodes[math.floor( alpha*len(nodes) ):]
    return Instance(v0, u, w, m, q)
