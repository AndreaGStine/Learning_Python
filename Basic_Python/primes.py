#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#adapted from Essential Python LinkedIn Course code to be slightly more efficient
import math

#Empty list to be called for find_primes, but defined outside of the function for convenience
primes = []

#The og isprime code but sped up a little bit:
#This function will test if a number is divisible by any other number less than its square root. If so, it returns
#false, else it returns true.
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, math.ceil(n**0.5)):
        if n % x == 0:
            return False
    else:
        return True

#Instead of testing against every number in the range, why not just test against primes already found up to that range?
#This seems to run slower for a given n since it's recursively testing every prime up to the appropriate
# ceiling rather than over the whole range, but I would imagine this is more "useful" for most contexts.
#This function returns the updated list of primes in the range from 2 up to n.
def find_primes(n):
    primes = []
    for x in range(2, n):
        yesprime = True
        for y in primes:
            if y > (x**0.5):
                break
            if x % y == 0:
                yesprime = False
                break
        if yesprime:
            primes.append(x)
    return primes

#I'm not a number theorist so I might be wrong, but it seems like every mersenne prime is to a prime power;
#(2023 Update: I checked; they are all prime!)
#61 seems to be the farthest that my computer will get to for n before getting upset
#This function will test for every mersenne prime from 2^p - 1 up to 2^p - 1, and return each value on a new line
def mersenne(p):

    for x in find_primes(p+1):
        if isprime(2**x - 1):
            print(2**x - 1, '(or 2 to the ', x, ' minus 1)')

#You may call a function as you'd like here at the end:
def main():
    mersenne(31)
    print(find_primes(100))

if __name__ == '__main__': main()