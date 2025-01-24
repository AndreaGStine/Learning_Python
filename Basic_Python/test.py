import math


# Distance function

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Function returns a list of coordinates that lie along the arrow from point (x1,y1) to (x2,y2)
def arrow(x1, y1, x2, y2):
    head = (x1, y1)
    coords = set([])
    for t in range(0, 2000):
        for i in range(0, 100):
            for j in range(0, 100):
                if dist(x1 + (t / 2000)*(x2 - x1), y1 + (t / 2000)*(y2 - y1), i, j) < 0.5:
                    coords.add((i, j))
    return coords