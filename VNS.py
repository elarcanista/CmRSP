import math
import solution
import constructives as cons
import random
import copy as copy

def isSource(point, sol):
    return point.id == 0 or point.id == sol.n +1

def add(graph, key1, key2, item):
    if key1 in graph:
        graph[key1][key2] = item
    else:
        graph[key1] = {key2 : item}

#{(u2,u1),(u1,u3)} to {(u2,u3), (u1,u3)}
def swap(sol, u1, u2, u3):
    w12 = sol.y[u1][u2]
    w21 = sol.y[u2][u1]
    w13 = sol.y[u1][u3]
    w31 = sol.y[u3][u1]
    add(sol.y, u2, u3, w21)
    add(sol.y, u3, u2, w12)
    del sol.y[u1][u2]
    del sol.y[u2][u1]
    del sol.y[u1][u3]
    del sol.y[u3][u1]
    del sol.y[u1]
    sol.z[u1] = u3
    sol.z2.add(u3)

#{(u2,u1),(u1,u3)} to {(u2,v),(v,u3), (u1,v)}
def swap2(sol, u1, u2, u3, v):
    w12 = sol.y[u1][u2]
    w21 = sol.y[u2][u1]
    w13 = sol.y[u1][u3]
    w31 = sol.y[u3][u1]
    add(sol.y, u2, v, w21)
    add(sol.y, v, u2, w12)
    add(sol.y, u3, v, w31)
    add(sol.y, v, u3, w13)
    del sol.y[u1][u2]
    del sol.y[u2][u1]
    del sol.y[u1][u3]
    del sol.y[u3][u1]
    del sol.y[u1]
    sol.z[u1] = v
    sol.w.add(v)


#{(u2,u1),(u1,u3),(u3,u4)} to {(u2,u3),(u1,u3),(u1,u4)}
def swap3(sol, u1, u2, u3, u4):
    wu12 = sol.y[u1][u2]
    wu21 = sol.y[u2][u1]
    wu34 = sol.y[u3][u4]
    wu43 = sol.y[u4][u3]
    sol.y[u1].pop(u2, None)
    sol.y[u2].pop(u1, None)
    add(sol.y, u2, u3, wu21)
    add(sol.y, u3, u2, wu12)
    sol.y[u3].pop(u4, None)
    sol.y[u4].pop(u3, None)
    add(sol.y, u4, u1, wu43)
    add(sol.y, u1, u4, wu34)

#{(u2,u1),(u3,u1),(v2,v1),(v3,v1)} to {(u2,v1),(u3,v1),(v2,u1),(v3,u1)}
def swap4(sol, u1, u2, u3, v1, v2, v3):
    wu12 = sol.y[u1][u2]
    wu21 = sol.y[u2][u1]
    wu13 = sol.y[u1][u3]
    wu31 = sol.y[u3][u1]
    wv12 = sol.y[v1][v2]
    wv21 = sol.y[v2][v1]
    wv13 = sol.y[v1][v3]
    wv31 = sol.y[v3][v1]
    sol.y[u1].pop(u2, None)
    sol.y[u2].pop(u1, None)
    sol.y[u1].pop(u3, None)
    sol.y[u3].pop(u1, None)
    sol.y[v1].pop(v2, None)
    sol.y[v2].pop(v1, None)
    sol.y[v1].pop(v3, None)
    sol.y[v3].pop(v1, None)
    add(sol.y, u2, v1, wu21)
    add(sol.y, v1, u2, wu12)
    add(sol.y, u3, v1, wu31)
    add(sol.y, v1, u3, wu13)
    add(sol.y, v2, u1, wv21)
    add(sol.y, u1, v2, wv12)
    add(sol.y, v3, u1, wv31)
    add(sol.y, u1, v3, wv13)

def localSearchZ3(sol):
    solp = sol.cost()
    while True:
        for u1, d in sol.y.items():
            if u1.id == 0 or u1.id == sol.n+1 or \
               (not u1 in sol.z) or sol.z[u1] != u1 \
                or u1 in sol.z2:
                continue
            u =  list(map(lambda a: a[0], d.items()))
            u = list(filter(lambda a: isSource(a,sol) or \
                            a in sol.w or \
                            sol.z[a] == a, u))
            u2, u3 = u
            minV = u1
            W1 = math.inf
            for v in sol.W:
                if v in sol.y:
                    continue
                if u1.euclidDistance(v) + u2.euclidDistance(v) + u3.euclidDistance(v) < W1:
                    W1 = u1.euclidDistance(v) + u2.euclidDistance(v) + u3.euclidDistance(v)
                    minV = v
            W2 = math.inf
            if not isSource(u3,sol):
                if u1.euclidDistance(u2) > u2.euclidDistance(u3):
                    W2 = u2.euclidDistance(u3) + u1.euclidDistance(u3)
            W3 = math.inf
            if not isSource(u2,sol):
                if u1.euclidDistance(u3) > u2.euclidDistance(u3):
                    W3 = u2.euclidDistance(u3) + u1.euclidDistance(u2)
            minmin = min(W1, W2, W3)
            if minmin < u1.euclidDistance(u2) + u1.euclidDistance(u3):
                if minmin == W1:
                    swap2(sol, u1, u3, u2, minV)
                    break
                if minmin == W2:
                    swap(sol, u1, u2, u3)
                    break
                if minmin == W3:
                    swap(sol, u1, u3, u2)
                    break
        if solp == sol.cost():
            return sol
        solp = sol.cost()

def changeNeighbourhood(sol):
    u1 = random.choice(list(sol.y))
    v1 = random.choice(list(sol.y))
    while isSource(u1, sol) or isSource(v1, sol):
        u1 = random.choice(list(sol.y))
        v1 = random.choice(list(sol.y))
    sU = sum([sol.y[u][u1] - sol.y[u1][u] for u in sol.y[u1]])/2
    sV = sum([sol.y[v][v1] - sol.y[v1][v] for v in sol.y[v1]])/2
    u2, u3 = [u for u in sol.y[u1]]
    u4 = ""
    if u3 == v1:
        v2, v3 = [v for v in sol.y[u3]]
        u4 = v3 if v2 == u1 else v2
        swap3(sol,u1,u2,u3,u4)
    elif u2 == v1:
        v2, v3 = [v for v in sol.y[u2]]
        u4 = v3 if v2 == u1 else v2
        swap3(sol,u1,u3,u2,u4)
    elif sU == sV:
        v2, v3 = [u for u in sol.y[v1]]
        swap4(sol,u1,u2,u3,v1,v2,v3)
    return sol

def VNS(p,it):
    seed = cons.naive(p,1,0)
    best = localSearchZ3(copy.deepcopy(seed))
    c = 0
    while c < it:
        newS = localSearchZ3(changeNeighbourhood(copy.deepcopy(best)))
        newS2 = localSearchZ3(changeNeighbourhood(copy.deepcopy(seed)))
        if best.cost() > newS.cost():
            best = newS
            c = 0
        elif best.cost() > newS2.cost():
            best = newS2
            c = 0
        else:
            c += 1
    return best
