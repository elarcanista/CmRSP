import sys
import parser
import matplotlib.pyplot as plt
import testing as test
import instance as inst
import solution as sol
import constructives as cons
import lpSolution as lp
import graphing as graph

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        nodes = parser.read(arg)
        alpha = [0.25]
        m = [2]
        tests = test.testCases(nodes, alpha, m, 0.9)
        #sol = map(lambda x: map(lambda y:cons.naive(y,1,0), x), tests)
        sol = map(lambda x: map(lp.solve, x), tests)
        sol = list(map(list, sol))
        graph.graphSolutions(sol)
        #graph.toLaTeX(sol)
