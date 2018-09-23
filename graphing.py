import matplotlib.pyplot as plt

def graphInstance(instance, axs):
    axs.scatter(instance.v0.x, instance.v0.y, marker="s", label = "Depot")
    if instance.U:
        x,y = zip(*list(map(lambda i: (i.x, i.y), instance.U)))
        axs.scatter(x, y, marker="o", label = "Users")
    if instance.W:
        x,y = zip(*list(map(lambda i: (i.x, i.y), instance.W)))
        axs.scatter(x, y, marker="^", label = "Steiner nodes")

def graphSolution(solution, axs):
    title = "|U| = " + str(len(solution.U)) + \
            ", |W| = " + str(len(solution.W)) + \
            ", m = " + str(solution.m) + \
            ", q = " + str(solution.q) + \
            ", cost = " + str(round(solution.cost(), 1))
    axs.set_title(title)
    graphInstance(solution, axs)
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
            axs.plot([u.x, v.x], [u.y, v.y],
                     color=color[c%len(color)], linestyle='-')
            if v in vis and v.id != 0:
                continue
            s.append(v)
            vis.add(v)

def toLaTeX(solutions):
    for i in solutions:
        for solution in i:
            table = str(len(solution.U)+len(solution.W)) + \
            " & " + str(len(solution.U)) + \
            " & " + str(len(solution.W)) + \
            " & " + str(solution.m) + \
            " & " + str(solution.q) + \
            " & " + str(round(solution.cost(), 1)) + " & \\\\"
            print(table)

def graphSolutions(solutions):
    fig, axs = plt.subplots(len(solutions), len(solutions[0]))
    for i in range(len(solutions)):
        for j in range(len(solutions[0])):
            graphSolution(solutions[i][j], axs[i][j])
    handles, labels = axs[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper left')
    plt.show()
