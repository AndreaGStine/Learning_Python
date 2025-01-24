'''
Problem statement:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


'''
import time
import math
start_time = time.time()

#Calculate gcd using euclidean algorithm
def gcd(a = 2, b = 2):
    r1 = min(a,b)
    r2 = max(a,b)
    while r2 % r1 != 0:
        newr1 = abs(r2 - (math.floor(r2 / r1)*r1))
        r2 = r1
        r1 = newr1
    return r1

#Calculate lcm in terms of gcd
def lcm(a = 2, b = 2):
    return int((a * b) / gcd(a,b))

#The naive solution fails for k=43 or greater
#I honestly don't understand why
#Naive approach: Calculate the lcm of all numbers from 2 to 20
def naive_solution(k=20):
    #The smallest number evenly divisible by all of 1-k is the lcm of all of them,
    #so just compute the lcm...
    #To further speed up the computation, ignore 1 as all numbers are evenly divisible by 1
    #and start at k and descend
    n = 1
    for i in range(0,k-2):
        n = lcm(n,k-i)
    return n

def relativelyprime(n=1,l=[]):
    for k in l:
        if n % k == 0:
            return False
    return True

def listprimes(n):
    primeslist = []
    for i in range(2,n):
        if relativelyprime(i,primeslist):
            primeslist.append(i)
    return primeslist

#Better approach: Determine all primes from 2 to 20,
#Determine highest power of each prime that's less than 20,
#Output the product of the highest powers of all primes
def better_solution(k=20):
    primes = listprimes(k)
    n = 1
    for p in primes:
        i = 1
        while p**i <= k:
            n *= p
            i += 1
    return n


if __name__ == "__main__":
    print(better_solution(20))
    print(time.time() - start_time)