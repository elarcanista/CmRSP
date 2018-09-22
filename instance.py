import math

class Instance:
    def __init__(self, depot, clients, steiners, m=1, q=math.inf):
        self.depot = depot
        self.clients = clients
        self.steiners = steiners
        self.m = m
        self.q = q

    def __str__(self):
        return "{m = " + str(self.m) + \
                 ", q = " + str(self.q) + \
                 ", depot = " + str(self.depot) + \
                 ", clients = " + str(self.clients) + \
                 ", Steiner nodes = " + str(self.steiners) + \
                 "}"

def genTest(nodes, alpha=1, m=1, q=math.inf):
    depot = nodes.pop(-1)
    clients = nodes[:math.floor( alpha*len(nodes) )]
    steiners = nodes[math.floor( alpha*len(nodes) ):]
    return Instance(depot, clients, steiners, m, q)
