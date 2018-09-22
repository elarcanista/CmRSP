#Returns a list with a the x and y coordinates of the ith vertex in a file.
#First and last vertices are the same
def read(filename):
    f = open(filename, "r")
    lines = f.readlines()[6:]
    vertices = []
    for line in lines:
        if(line == "EOF\n"):
            break
        n,x,y = map(int, line.split(" "))
        vertices.append( (n,x,y) )
    f.close()
    return vertices
