import sys
import parser
import matplotlib.pyplot as plt
import testing as test
import instance as inst
import solution as sol
import constructives as cons
import graphing as graph

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        nodes = parser.read(arg)
        tests = test.testCases(nodes, [0.25, 0.5, 0.75, 1], [3, 4, 5], 0.9)
        sol = map(lambda x: map(lambda y:cons.naive(y,1,10), x), tests)
        sol = list(map(list, sol))
        graph.graphSolutions(sol)
        graph.toLaTeX(sol)
