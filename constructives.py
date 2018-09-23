import math
import queue
import random
import solution as sol
import point

def add(graph, key1, key2, item):
    if key1 in graph:
        graph[key1][key2] = item
    else:
        graph[key1] = {key2 : item}

def naive(inst, kth = 1, noiseV = 0):
    depot1 = inst.v0
    depot2 = inst.V[0]
    unvisited = set(inst.U)
    y = dict()
    z = dict()
    while(unvisited):
        last = depot1
        clients = 0
        while(unvisited and clients < inst.q):
            best = list(unvisited)
            best.sort(key=lambda x: random.normalvariate(0, noiseV) + \
                      last.euclidDistance(x))
            curr = best[random.randrange(min(kth,len(best)))]
            add(y, last, curr, inst.q - clients)
            add(y, curr, last, clients)
            z[curr] = curr
            clients += 1
            unvisited.remove(curr)
            last = curr
        add(y, last, depot2, inst.q - clients)
        add(y, depot2, last, clients)
    return sol.Solution({}, y, z, inst)
