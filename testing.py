import math
import point
import instance as inst

def genTest(nodes, alpha=1, m=1, q=math.inf):
    nodes = list(map(lambda i: point.Point(*i), nodes))
    v0 = nodes.pop(-1)
    u = nodes[:math.floor( alpha*len(nodes) )]
    w = nodes[math.floor( alpha*len(nodes) ):]
    return inst.Instance(v0, u, w, m, q)

def testCases(nodes, alpha, m, q):
    tests = []
    for i in alpha:
        tests.append([])
        u = math.floor( i*len(nodes) )
        for j in m:
            tests[-1].append(genTest(nodes, i, j, math.ceil(u/(q*j)) ))
    return tests
