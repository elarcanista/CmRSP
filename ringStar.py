import sys
import parser
import matplotlib.pyplot as plt
import instance as inst
import constructives as cons
import solution as sol

def graphInstance(instance):
    plt.scatter(instance.v0.x, instance.v0.y, marker="s")
    x,y = zip(*list(map(lambda i: (i.x, i.y), instance.u)))
    print(x, y)
    plt.scatter(x, y, marker="o")
    x,y = zip(*list(map(lambda i: (i.x, i.y), instance.w)))
    plt.scatter(x, y, marker="^")

def graphSolution(instance, solution = sol.Solution({},[],[])):
    for k, v in solution.y.items():
        x = (instance.v[k[0]][0], instance.v[k[1]][0])
        y = (instance.v[k[0]][1], instance.v[k[1]][1])
        plt.plot(x, y, 'r-')

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        nodes = parser.read(arg)
        test = inst.genTest(nodes, 0.75, 3, 14)
        graphInstance(test)
        sol = cons.naive(test)
        #graphSolution(test, sol)
        plt.show()
