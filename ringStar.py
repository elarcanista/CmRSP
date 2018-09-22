import sys
import parser

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        l = parser.read(arg)
        print(l)
