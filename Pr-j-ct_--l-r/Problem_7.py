'''
Problem statement:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
import time
import math
start_time = time.time()

#Recycling code from Problem 5
def relativelyprime(n=1,l=[]):
    for k in l:
        if n % k == 0:
            return False
    return True

#I would call this a naive solution, but I think it's faster than the solution given in the pdf
def solution():
    primeslist = []
    n = 1
    i = 0
    while i < 10001:
        n += 1
        if relativelyprime(n,primeslist):
            primeslist.append(n)
            i += 1
    return n



if __name__ == "__main__":
    print(solution())
    print(time.time() - start_time)