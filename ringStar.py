import sys

def parse(filename):
    f = open(filename, "r")
    lines = f.readlines()[6:]
    vertices = []
    for line in lines:
        if(line == "EOF\n"):
            break
        n,x,y = map(int, line.split(" "))
        vertices.append((x,y))
    return vertices

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        l = parse(arg)
        print(l)
