from All_Projects.My_Code_Essential_Python import graphs
from Ex_Files_Python_Data_Structures.Exercise_Files.begin_03_03 import read_maze


#Purpose: Convert maze in matrix data type to graph data type
def mazematrixconverter(matrix):
    try:

        #Initializing sets of vertices and edges
        v = set([])
        e = set([])

        #Iterating over entries in the matrix
        for i in range(0,len(matrix)):
           for j in range(0,len(matrix[i])):
                #Add each entry of the matrix to the set of vertices
                v.add((i,j))

                #The below checks if the entries above and to the left of a given entry are obstacles
                #Note an obstacle is represented by '*'
                #If the adjacent entry is not an obstacle, and edge is added between the two entries
                #The below only checks up and left of a given entry so as not to repeat edges
                #Yay even though this is O(n^2) because it just manually searches thru matrix entries the constant term is
                #slightly smaller because it only has to iterate thru half the number of cases!
                if i != 0 and matrix[i-1][j] != '*':
                        e.add(((i,j),(i-1,j)))
                if j != 0 and matrix[i][j-1] != '*':
                        e.add(((i,j),(i,j-1)))

        #To do: Since edges are only going to be between adjacent matrix entries, I'm sure there's a more efficient
        #Way to represent this data, right? I should figure that out
        #I also should find a more efficient way to go thru matrix entries than this... algorithms pls

        g = graphs.Graph(vertices=v, edges=e)

        return g
    except:
        print("Maze matrix-to-graph converter unsuccessful.")
        return

#Purpose: Convert an adjacency matrix to an undirected graph
#In an undirected graph, the edge (i,j) is the same as the edge (j,i), so only one is included
#Note that the output may not appear identical to the original undirected graph as order of (from,to) for edges
#Might be permuted
#(but this is fine because in an undirected graph, the direction doesn't matter!)
def undirected_adjacency_matrix_converter(matrix):
    try:
        v = set([])
        e = set([])

        for i in range(0, len(matrix)):
            v.add(i)
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 1:
                    if (j,i) not in e:
                        e.add((i,j))

        g = graphs.Graph(vertices=v, edges=e)
        return g

    except:
        print("Adjacency matrix-to-graph conversion unsuccessful.")
        return


# Purpose: Convert an adjacency matrix to a directed graph
def directed_adjacency_matrix_converter(matrix):
    try:
        v = set([])
        e = set([])

        for i in range(0, len(matrix)):
            v.add(i)
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 1:
                    if (j, i) not in e:
                        e.add((i, j))

        g = graphs.Graph(vertices=v, edges=e)
        return g

    except:
        print("Adjacency matrix-to-graph conversion unsuccessful.")
        return


def main():
    print(mazematrixconverter(read_maze.read_maze(r"C:\Users\Andrea\Desktop\Programming\Ex_Files_Python_Data_Structures\Exercise_Files\begin_03_03\mazes\modest_maze.txt")).edges)

    g0 = graphs.random_graph()
    print(g0.vertices)
    print(g0.edges)

    g1 = undirected_adjacency_matrix_converter(g0.adjacency())
    print(g1.vertices)
    print(g1.edges)

if __name__ == '__main__': main()
