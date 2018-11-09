class Solution:
    def __init__(self, w, y, z, inst):
        self.w = w
        self.y = y
        self.z = z
        self.n = inst.n
        self.z2 = set()
        self.v0 = inst.v0
        self.m = inst.m
        self.q = inst.q
        self.U = inst.U
        self.W = inst.W
        self.V = inst.V
        self.instance = inst

    def __str__(self):
        return "{w = " + str(self.w) + \
               ", y = " + str(self.y) + \
               ", z = " + str(self.z) + "}"

    def __repr__(self):
        return str(self)

    def cost(self):
        c = 0
        for u, d in self.y.items():
            for v, w in d.items():
                c += u.euclidDistance(v)*(w + self.y[v][u])
        c /= (self.q*2)
        for u, v in self.z.items():
            c += u.euclidDistance(v)
        return c
