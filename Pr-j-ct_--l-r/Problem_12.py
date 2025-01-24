'''

Problem Statement:
A triangular number is of the form 1 + 2 + ... + n.

What is the value of the first triangle number to have over five hundred divisors?

'''

import time
import math
import numpy as np
import itertools as it

def sieve_of_eratosthenes(j=2):
    sieve_bound = math.ceil((j - 1)/2)
    crosslimit = math.ceil((math.sqrt(j) - 1)/2)
    sieve = [False]*sieve_bound
    for n in range(1,crosslimit):
        if not sieve[n]:
            for m in range(2*n*(n+1),sieve_bound,(2*n)+1):
                sieve[m] = True

    fullsieve = [False, False, True]
    for i in range(3,j):
        if i % 2 == 0 or sieve[(i-1)//2]:
            fullsieve.append(False)
        else:
            fullsieve.append(True)

    return fullsieve

# Garbage I decided against:
# # Input: An integer n and a list of primes (not a boolean list)
# # Output: A list of pairs [p,k] where p is a prime factor of n
# # and k is the maximum power of p dividing n
# def find_prime_factors(n,compressedprimeslist):
#     if compressedprimeslist[-1] < n**2:
#         print('Warning: Some prime factors may not be found.')
#
#     length = len(compressedprimeslist)
#     primefactors = []
#     k=0
#     while compressedprimeslist[k] <= n and k < length:
#         j = 0
#         while n % compressedprimeslist[k] == 0:
#             j += 1
#             n // compressedprimeslist[k]
#         primefactors.append([compressedprimeslist[k]],j)
#         k+=1
#     return primefactors
#
#
# primefactorization[n] = find_prime_factors(n, compressedprimeslist)
# # Then determine the number of divisors of n:
# for i in range(0, len(primefactorization[n])):
#     divisorscount[n] *= (primefactorization[n][i][1] + 1)
# # Then compute the prime factors and number of divisors of n times its
# for i in range(0, len(primefactorization[n])):
#     p = primefactorization[n][i][0]
#     k = 1
#     while n * (p ** k) < sieve_bound:
#         primefactorization[n * (p ** k)] = primefactorization[n]
#         primefactorization[n * (p ** k)][i][1] += k

# Since the product of the first 9 primes is under 10**9 (~228mil), know n satisfying n(n+1)
# has > 501 prime factors is < 10**9
# Total runtime in worst case: O(sieve_bound log(sieve_bound)).
def solution(value=500,sieve_bound=10**5):
    # First, note that any triangular number 1 + 2 + ... + n = n(n+1)/2.
    # So we are looking for an integer n such that n(n+1)/2 has over 500 divisors.
    # That means n(n+1) should have over 501 divisors
    # (since k/2 has one less divisor than k, which is k itself)

    # Most naive algorithm: Iterate through every triangular
    # number until one with >500 divisors is found.
    # n = 7
    # count = 0
    # while True:
    #     count = 0
    #     triang = n*(n+1)
    #     for j in range(1,n):
    #         if j % triang == 0:
    #             count += 1
    #     if count > 501:
    #         break
    #     else:
    #         n += 1

    # Issue: This algorithm is very, very slow. Something more time-efficient:
    # We can remember the count of every integer found thus far.
    # Then for every new value, we can simply compare it to other values in the count!
    # Better yet: We can save ourselves a little time by computing a bunch of primes first,
    # and checking to see if n is in the list.
    # As a rough guess, n is probably less than 10^9; we can always raise bound if needed

    # Additional thought: The total # of divisors of a number should be
    # equal to the product of the powers+1 of the prime factors of that number.
    # For instance: 12 = 2^2 * 3^1, so we'd expect 3*2=6 divisors, and we have:
    # 1, 2, 3, 4, 6, 12: 6 divisors
    # Another instance: 140 = 2^2 * 5 * 7, so we'd expect 3*2*2=12 divisors, and we have:
    # 1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140: 12 divisors.

    # So to speed up computation, instead find the prime factorization of each number
    # And compute product of powers of prime factors
    # Lastly, since we're looking for a triangular number, the number of divisors of
    # n and n+1 should be multiplied together and tested vs 501.


    # Boolean list of locations of primes:

    # Takes O(sieve_bound log(sieve_bound)) to find all primes up to sieve_bound:
    primeslist = sieve_of_eratosthenes(sieve_bound)
    compressedprimeslist = list(it.compress(range(sieve_bound),primeslist))
    print('Primes found and compressed')
    # Number of divisors of n:
    divisorscount = [1]*sieve_bound
    n = 2
    # Loop over every number within the sieve bound until a value is found:
    # Worst case: No value found; loops over entire sieve_bound, and complexity is:
    # O(sieve_bound log(sieve_bound)).
    while (n < sieve_bound) and ((n % 2 == 1 and divisorscount[(n-1)//2]*divisorscount[n-2] < value+1) or (n % 2 == 0 and divisorscount[n-1]*divisorscount[n//2 - 1] < value+1)):
        # Check first to see if the divisor count of n has been computed:
        if divisorscount[n] == 1:
            # If n's prime factorization hasn't been computed, next check to see if n is prime:
            if primeslist[n]:
                # O(log(n)) time to find powers of prime n:
                # If it is, compute the prime factorization and divisors of all powers of n:
                k = 1
                while n**k < sieve_bound:
                    divisorscount[n**k] = k+1
                    k += 1
            # If n is not prime, find its first prime factor
            # noting that since the list is (mostly) computed in order,
            # every new non-prime value will be a prime multiple of something already found:
            else:
                # O(log(n)) time to find new prime divisor of n, O(log(n)) time to
                # find largest power of divisor that divides n:
                for p in compressedprimeslist:
                    if n % p == 0:
                        # Find the largest power of p that divides n
                        j = 1
                        while n % p**(j+1) == 0:
                            j += 1
                        # Then find the divisors of n // p**j and multiply it by j+1
                        # (since there's 1 more factor of p than there was before!)
                        divisorscount[n] = divisorscount[n//(p**j)] * (j+1)
                        break
        n += 1
    print(n-1, n-2, (n-1)*(n-2)//2, divisorscount[n-1], divisorscount[n-2])
    return (n-1)*(n-2)//2, divisorscount[n-1]*divisorscount[n-2]


if __name__ == "__main__":
    start_time = time.time()
    print(solution(value=500,sieve_bound=3*(10**6)))
    print(time.time() - start_time)


