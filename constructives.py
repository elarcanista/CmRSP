import math
import solution as sol
import point

def add(graph, key1, key2, item):
    if key1 in graph:
        graph[key1][key2] = item
    else:
        graph[key1] = {key2 : item}

def naive(inst):
    depot1 = inst.v0
    depot2 = inst.v[0]
    unvisited = set(inst.u)
    y = dict()
    z = dict()
    while(unvisited):
        last = depot1
        clients = 0
        while(unvisited and clients < inst.q):
            curr = min(unvisited, key = last.euclidDistance)
            add(y, last, curr, inst.q - clients)
            add(y, curr, last, clients)
            z[curr] = curr
            clients += 1
            unvisited.remove(curr)
            last = curr
        add(y, last, depot2, inst.q - clients)
        add(y, depot2, last, clients)
    return sol.Solution({}, y, z, inst)
