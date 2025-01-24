# Playing around with classes
import random
import math
import numpy

class Graph:
    # Initializing what a (weighted) graph is, where weights are the third coordinate of edges if they exist
    # Weights are assumed to be 1 if not specified otherwise
    def __init__(self, vertices=set([]), edges=set([])):
        self._vertices = vertices
        self._edges = edges

    # Defining a new property of the graph: Its adjacency matrix
    # Note the adjacency matrix gets majorly screwed up if you don't index your vertices as 0, 1, 2, ..., n
    def adjacency(self):

        # Since I'm not using numpy, I'm making the matrix with nested lists
        adjacency_matrix = []
        row = []
        for i in range(0, len(self._vertices)):
            row.append(0)
        for j in range(0, len(self._vertices)):
            adjacency_matrix.append(row[:])
        # One must put row[:] to create a separate instance of "row" that is unique
        # Else, changing one entry in the matrix changes that entry in every row,
        # As the matrix's rows would then be the same object.

        for edge in self._edges:
            v1 = edge[0]
            v2 = edge[1]
            try:
                adjacency_matrix[v1][v2] = edge[2]
                adjacency_matrix[v2][v1] = edge[2]
            except:
                adjacency_matrix[v1][v2] = 1
                adjacency_matrix[v2][v1] = 1
        # This sets entries to 1 where the entry corresponds to an edge between the row index and column index

        return adjacency_matrix

    #Identical to the above, but treats an edge (i,j) as an arrow i -> j instead:
    def directed_adjacency(self):
        # Since I'm not using numpy, I'm making the matrix with nested lists
        adjacency_matrix = []
        row = []
        for i in range(0, len(self._vertices)):
            row.append(0)
        for j in range(0, len(self._vertices)):
            adjacency_matrix.append(row[:])
        # One must put row[:] to create a separate instance of "row" that is unique
        # Else, changing one entry in the matrix changes that entry in every row,
        # As the matrix's rows would then be the same object.

        for edge in self._edges:
            v1 = edge[0]
            v2 = edge[1]
            try:
                adjacency_matrix[v1][v2] = edge[2]
            except:
                adjacency_matrix[v1][v2] = 1
        # This sets entries to 1 where the entry corresponds to an edge between the row index and column index

        return adjacency_matrix

    # Defining a new property of each vertex of the graph: Its adjacent edges
    def adjacent_vertices(self, vertex):
        if vertex in self._vertices:
            adjacentlist = []
            for edge in self._edges:
                if edge[0] == vertex:
                    try:
                        adjacentlist.append((edge[1],edge[2]))
                    except:
                        adjacentlist.append((edge[1],1))
                elif edge[1] == vertex:
                    try:
                        adjacentlist.append((edge[0],edge[2]))
                    except:
                        adjacentlist.append((edge[0],1))

            return adjacentlist
        else:
            print("That is not a vertex")
            return

    #Identical to the above, but treats the edge (i,j) as an arrow i -> j instead:
    def directed_adjacent_vertices(self, vertex):
        if vertex in self._vertices:
            adjacentlist = []
            for edge in self._edges:
                if edge[0] == vertex:
                    try:
                        adjacentlist.append((edge[1], edge[2]))
                    except:
                        adjacentlist.append((edge[1],1))
            return adjacentlist
        else:
            print("That is not a vertex")
            return



    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges
"""
    # Ignore everything below in quotes. It's an abandoned project.
    # Distance function
    def dist(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Function returns a list of coordinates that lie along the arrow from point (x1,y1) to (x2,y2)
    def arrow(self, x1, y1, x2, y2, r):
        head = (x1, y1)
        coords = set([])
        for t in range(0, 400 * r):
            for i in range(0, math.ceil(20 * r) - 1):
                for j in range(0, math.ceil(20 * r) - 1):
                    if self.dist(x1 + (t / (400 * r)) * (x2 - x1), y1 + (t / (400 * r)) * (y2 - y1), i, j) < 0.5:
                        coords.add((i, j))
        return coords

    # Drawing the graph
    def draw(self):
        # Constructing a finite plane as a matrix
        r = math.ceil(len(self._vertices) / (2 * math.pi))
        visual_matrix = []
        row = []
        for i in range(0, math.ceil(20 * r)):
            row.append(' ')
        for j in range(0, math.ceil(20 * r)):
            visual_matrix.append(row[:])

        # Placing each vertex around a circle in the plane
        k = 0
        t = 0
        p = 0
        while k < len(visual_matrix):
            k1 = 0
            while k1 < len(visual_matrix[k]):
                if math.floor(self.dist(k1, k, 4 * r + 1, 4 * r + 1)) == 4 * r + 1:
                    if t < len(self._vertices):
                        if p % 4 == 0:
                            visual_matrix[k][k1] = list(self._vertices)[t]
                            t = t + 1
                            p = p + 1
                        else:
                            p = p + 1

                k1 = k1 + 1
            k = k + 1

        # Identifying coordinates in the plane where an edge should be passing through
        for i in self._vertices:
            for x1 in range(0, len(visual_matrix)):
                for y1 in range(0, len(visual_matrix[x1])):
                    for x2 in range(0, len(visual_matrix)):
                        for y2 in range(0, len(visual_matrix[x2])):
                            if (visual_matrix[x1][y1], visual_matrix[x2][y2]) in self._edges:
                                for c in self.arrow(x1, y1, x2, y2, r):
                                    if visual_matrix[c[0]][c[1]] not in range(0, 400, 1):
                                        visual_matrix[c[0]][c[1]] = 'y'

        # Printing the plane in a somewhat nice, clean way
        for x in range(0, len(visual_matrix)):
            for y in range(0, len(visual_matrix[x])):
                if visual_matrix[x][y] in range(0, 400, 1):
                    print(visual_matrix[x][y], end="")
                elif visual_matrix[x][y] == 'y':
                    print('.', end="")
                else:
                    print(' ', end="")
            print('')
"""

#n: Max number of vertices
#r2: Probability of a given arrow existing (remember there's roughly n^2 edges in a complete graph!)
def random_graph(n,r2):
    try:
        # Uniformly distributed random number of vertices between 1 and n
        r = random.randint(1, n)
        v = set([])
        for i in range(0, r):
            v.add(i)

        # Randomly picking edge
        e = set([])
        for j in v:
            for k in v:
                if random.random() < r2 and k != j:
                    e.add((j, k))

        g = Graph(vertices=v, edges=e)
        return g
    except:
        return

#Identical to the above, but checks if an edge already exist so there's no duplicates
def random_undirected_graph(n,r2):
    try:
        # Uniformly distributed random number of vertices between 1 and n
        r = random.randint(1, n)
        v = set([])
        for i in range(0, r):
            v.add(i)

        # Randomly picking edge
        e = set([])
        for j in v:
            for k in v:
                if random.random() < r2 and k != j and (j,k) not in e:
                    e.add((j, k))

        g = Graph(vertices=v, edges=e)
        return g
    except:
        return

#Identical to above, but for a weighted graph. w is a weight constant: each arrow is given a weight
#with average weight w.
#If w is an integer, weights are Poisson-distributed.
#If w is a float, weights are "Normally-distributed with mean w, st dev sqrt(w)"...
#...except that wouldn't work because weights need to be positive!
#Turns out (thanks Wikipedia) that the sum of uniform distributions nicely approximates the normal distribution
#Not only by CLT but also because it's a spline approximation! How neat! Irwin-Hall is the distribution.
#Not only that, but it's supposedly computationally efficient to approximate the normal distribution in such a fashion
#Not only that, but it also has cutoffs the way I'd like it to!
def random_weighted_graph(n,r2,w):
    try:

        rw = False
        if type(w) != int:
            rw = True

        # Uniformly distributed random number of vertices between 1 and n
        r = random.randint(1, n)
        v = set([])
        for i in range(0, r):
            v.add(i)

        # Randomly picking edge
        e = set([])
        for j in v:
            for k in v:
                if random.random() < r2 and k != j:
                    if rw == False:
                        #Randomly assigning weights, poisson distributed with mean w in the int case (Z-valued)
                        e.add((j,k,numpy.random.poisson(w)))
                    else:
                        #Randomly assigning weights, Irwin-Hall distributed with mean w in the float case (R-valued)
                        r1 = 0
                        for i in range(0,math.ceil(2*w)):
                            r1 += random.random()
                        e.add((j,k,r1))


        g = Graph(vertices=v, edges=e)
        return g
    except:
        return


def main():
    g0 = random_weighted_graph(20,0.3,3)

    print(g0.vertices)
    print(g0.edges)


if __name__ == '__main__': main()
