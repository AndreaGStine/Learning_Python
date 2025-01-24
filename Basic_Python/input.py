#Testing user input

import math

#Input a user's name:
def confirm_name():
    #Placeholder name with check to confirm name
    tempname = ""
    done = False
    #Loop until user has confirmed name
    while done == False:
        tempname = input('Please input your name: ' )
        print('Are you sure you would like to be called ', tempname, '?')
        confirmation = input('(Y/N) ' )
        if confirmation == 'Y' or confirmation == 'y':
            done = True
        else:
            print('Okay, we\'ll try again.')
    print('Welcome, ', tempname)
    return tempname

name = confirm_name()

#Calling the name outside of the function:
print("Aha, I see your name is:", name)

#User inputs for doing a bisection method approximation of a 0
def inputbisection():
    #As above; placeholder range, variable, and test for done-ness
    testingrange = []
    testingfunction = lambda x: x
    testingiterates = 0
    tempiterates = ''
    tempfunction = ''
    temprange = ''
    done = False

    #Loop until user has given a correct function and range
    while not done:
        tempfunction = input('Please input a nondecreasing function of a single variable x:' )
        temprange = input('Please input the range you\'d like to search for a 0 within in the exact format [a, b]:' )
        tempiterates = input('Please input how many iterations you would like to perform, as an integer:' )
        confirmation = input('Is the function and its range written as desired? (Y/N) ')
        if confirmation == 'Y' or confirmation == 'y':
            try:
                #Attemps to convert to a function, list, and integer
                testingfunction = eval(f'lambda x: {tempfunction}')
                testingrange = eval(temprange)
                testingiterates = eval(tempiterates)
            except:
                print('Your range and/or function and/or iterates are in the wrong format. We\'ll try again.')
            else:
                done = True
                #Returns a list  of a function, a list, and an integer
                return [testingfunction, testingrange, testingiterates]
        else:
            print('Okay, we\'ll try again.')

#Approximating fixed points of a user-inputted function in a user-inputted range using the bisection method:
def bisection():
    testingvalues = inputbisection()
    a = testingvalues[1][0]
    b = testingvalues[1][1]
    for i in range(1,testingvalues[2]):
        c = (a + b)/2
        if testingvalues[0](c) == 0:
            print(f'Zero found at x = {c}')
            return c
        elif testingvalues[0](c) > 0:
            b = c
        else:
            a = c
    #Returns the estimate for a zero found and its error
    return [c, testingvalues[0](c)]

print(bisection())



