import matplotlib.pyplot as plt

def graphInstance(instance):
    plt.scatter(instance.v0.x, instance.v0.y, marker="s")
    x,y = zip(*list(map(lambda i: (i.x, i.y), instance.u)))
    plt.scatter(x, y, marker="o")
    x,y = zip(*list(map(lambda i: (i.x, i.y), instance.w)))
    plt.scatter(x, y, marker="^")

def graphSolution(solution):
    s = [solution.v0]
    vis = set()
    color = 'bgrcmyk'
    c = 0
    while s:
        u = s.pop()
        if u.id == 0:
            c += 1
            continue
        vis.add(u)
        for v, w in solution.y[u].items():
            plt.plot([u.x, v.x], [u.y, v.y],
                     color=color[c%len(color)], linestyle='-')
            if v in vis and v.id != 0:
                continue
            s.append(v)
            vis.add(v)
