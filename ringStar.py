import sys
import parser
import matplotlib.pyplot as plt
import testing as test
import instance as inst
import solution as sol
import constructives as cons
import lpSolution as lp
import graphing as graph
import VNS as VNS

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        nodes = parser.read(arg)
        alpha = [0.25,0.5,0.75,1]
        m = [3,4,5]
        it = 100
        tests = test.testCases(nodes, alpha, m, 0.9)
        #sol = map(lambda x: map(lp.solve, x), tests)
        #sol = map(lambda x: map(lambda y:cons.naive(y,1,0), x), tests)
        #sol = map(lambda x: map(VNS.localSearchZ3, x), sol)
        sol = map(lambda x: map(lambda y: VNS.VNS(y, it), x), tests)
        sol = list(map(list, sol))
#        print(sol)
        #sol[0][0] = VNS.changeNeighbourhood(sol[0][0])
        graph.graphSolutions(sol)
        graph.toLaTeX(sol)
