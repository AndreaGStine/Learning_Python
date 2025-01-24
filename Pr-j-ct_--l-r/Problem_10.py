'''
Problem statement:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import time
import math


#Unsurprisingly, I can just recycle code from previous problems to solve this one
#But that turns out to be very slow, so I used a couple tricks seen in previous problems to speed it up...
def relativelyprime(n=1,l=[]):
    for k in l:
        if n % k == 0:
            return False
        elif k > math.sqrt(n):
            return True
    return True

def primes_below(j = 2):
    start_time = time.time()
    primeslist = [2,3]
    n = 6
    while n < j:
        if relativelyprime(n-1, primeslist):
            primeslist.append(n-1)
        if relativelyprime(n+1, primeslist):
            primeslist.append(n+1)
        n += 6
    return (sum(primeslist),time.time() - start_time)

#Hey, under 8 seconds isn't too bad. To do any faster I'd need the sieve of Eratosthenes
#given in the solution pdf.
#It's good practice to turn pseudocode into actual code, so here's my rendition:
def sieve_solution(j=2):
    start_time = time.time()

    sieve_bound = math.ceil((j - 1)/2)
    crosslimit = math.ceil((math.sqrt(j) - 1)/2)
    sieve = [False]*sieve_bound
    for n in range(1,crosslimit):
        if not sieve[n]:
            for m in range(2*n*(n+1),sieve_bound,(2*n)+1):
                sieve[m] = True
    s = 2
    for n in range(1,sieve_bound):
        if not sieve[n]:
            s += 2*n + 1
    return (s,time.time() - start_time)

if __name__ == "__main__":
    print(primes_below(2*(10**6)))
    print(sieve_solution(2*(10**6)))