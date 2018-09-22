import sys
import parser
import instance as inst
import constructives as cons
import solution as sol

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        nodes = parser.read(arg)
        test = inst.genTest(nodes, 0.75, 3, 14)
        sol = cons.naive(test)
        print(sol.cost())
