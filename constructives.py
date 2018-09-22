import math
import solution as sol
import point
import matplotlib.pyplot as plt

def naive(inst):
    depot1 = inst.v0
    depot2 = inst.v[0]
    unvisited = set(inst.u)
    y = dict()
    z = dict()
    while(unvisited):
        last = depot1
        clients = 0
        while(unvisited and clients <= inst.q):
            curr = min(unvisited, key = last.euclidDistance2)
            y[last, curr] = inst.q - clients
            y[curr, last] = clients
            z[curr] = curr
            clients += 1
            unvisited.remove(curr)
            last = curr
        y[last, depot2] = inst.q - clients
        y[depot2, last] = clients
    print(len(y))
    return sol.Solution({}, y, z)
