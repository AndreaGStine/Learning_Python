#User-input variable arguments
import random

#Function prompts user to input a tuple of integers, returns result as a tuple:
def inputnumbers():
    #User inputs a tuple of integers as a string
    print('Input a list of integers, separated by a space: ')
    liststring = input()

    #String is converted to a list
    listlist = list(liststring.split())
    listint = []
    for t in listlist:
        listint = listint + [int(t)]
    listtuple = tuple(listint)

    return listtuple

#Function takes a tuple of integers as input, returns a tuple of the proportion
#of each integer to their sum
def proportions(*args):
    total = 0

    # Sums the integers from the previous function
    for t in args[0]:
        s = int(t)
        total = total + s

    # Computes the portion of each integer
    listportions = []
    for u in args[0]:
        v = int(u)
        listportions = listportions + [v / total]

    return tuple(listportions)

#Function takes a tuple of integers as input and returns one of those integers
#chosen at random, where the probability of choosing such an integer is proportionate
#to the sum of the integers (so proportionately larger integers are more likely
#to be chosen)
def picker(*args):
    #Chooses a uniformly distributed random number from 0 to 1
    #prob = random.random()

    #Computes the proportion of each integer in input to their sum
    portions = proportions(*args)

    #Iterates over each integer, testing to see if that integer's portion exceeds the
    #random number chosen, thus giving a weighed probability to each integer
    #u = 0
    #for s in range(0, len(portions)):
    #    u = u + portions[s]
    #    if prob < u:
    #        return args[0][s]

    #Neater alternative:
    return random.choices(args[0], weights=portions)[0]


def main():
    print(picker(inputnumbers()))

if __name__ == '__main__': main()