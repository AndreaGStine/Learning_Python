import random
from All_Projects.My_Code_Essential_Python import graphs

#For all random walks,
#num is the number of iterations of the random walk
#p is the probability of moving "right"
#increase is the quantity the particle moves to the right
#initial is the initial location
#if an exception is not thrown, then the random walk returns the entire history of the random walk as a list

#1-dimension additive, mean-free random walk
def additive_random_walk(num=10, p=0.5, increase=1, initial=0):
    try:
        #Checks if iterations, probability, and increase quantities are sensible
        if 0 < num and 0 < p < 1 and 0 <= increase:
            decrease = (p * increase) / (1 - p)
            history = [initial]

            for k in range(0,num):
                if random.random() < p:
                    history.append(history[k]+increase)
                else:
                    history.append(history[k]-decrease)
            return(history)
        else:
            print("Random walk unsuccessful. Make sure all quantities are within acceptable parameters.")
            return
    except:
        print("Random walk unsuccessful. Make sure all quantities are within acceptable parameters.")
        return

#1-dimension multiplicative, mean-free random walk
def multiplicative_random_walk(num=10, p=0.5, increase=1.1, initial=100):
    try:
        #Checks if iterations, probability, increase, and initial quantities are reasonable
        if 0 < num and 0 < p < 1 and 1 < increase and 0 < initial:
            decrease = (1 - (p * increase)) / (1 - p)
            history = [initial]

            for k in range(0,num):
                if random.random() < p:
                    history.append(history[k]*increase)
                else:
                    history.append(history[k]*decrease)
            return(history)
        else:
            print("Random walk unsuccessful. Make sure all quantities are within acceptable parameters.")
            return
    except:
        print("Random walk unsuccessful. Make sure all quantities are within acceptable parameters.")
        return

#randomly walking along a directed, weighted graph
#graph is the graph
#w is the weighting given to staying in place
#if you want to do an undirected graph instead, replace the line
#destinations = graph.directed_adjacent_vertices(history[k]) with
#destinations = graph.adjacent_vertices(history[k])
def graph_random_walk(num=10, graph=graphs.Graph(vertices={0},edges=set([])), w=1, initial=0):
    try:
        #Again, sanity-checking the inputs:
        if 0 < num and initial in graph.vertices and 0 <= w:
            history = [initial]

            for k in range(0,num):
                #destinations consists of adjacent vertices and the weight given to each vertex
                #higher weight means more likely to select that vertex
                destinations = graph.directed_adjacent_vertices(history[k])
                destinations.append((history[k],w))
                #establishing the total weight of all edges
                tw = 0
                for m in destinations:
                    tw += m[1]
                #The trick here is to sum over all edge weights one at a time, and once the edge weight exceeds the
                #uniform random quantity btwn 0 and 1, that given edge is chosen to be the one moved to
                r = random.random()*tw
                ts = 0
                b = True
                for m in destinations:
                    ts += m[1]
                    if ts >= r and b == True:
                        history.append(m[0])
                        b = False
            return history

        else:
            print("Random walk unsuccessful. Make sure all arguments are within acceptable parameters.")
            return
    except:
        print("Random walk unsuccessful. Make sure all arguments are within acceptable parameters.")
        return

def main():
    print(additive_random_walk(100, 0.7, 1, 0)[100])
    print(multiplicative_random_walk(100, 0.7, 1.01, 100)[100])
    g0 = graphs.Graph(vertices={0,1,2,3,4,5,6,7,8},edges={(0,1),(0,2),(1,3),(1,4),(2,4),(2,5),(5,6),(6,5),(4,7),(7,8),(8,4)})
    g1 = graphs.random_weighted_graph(15,0.6,3)
    print(g1.edges)
    print(graph_random_walk(30,g1,0.1,0))

if __name__ == '__main__': main()


