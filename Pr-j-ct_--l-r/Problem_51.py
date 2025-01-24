
#I might return to 11-50 but the first 10 were very easy and I didn't learn a lot, so here's
#a bigger challenge
'''
Problem statement:

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

'''
import time
import math
import itertools

'''This worked for a solution, but it wasn't terribly robust. I made two big assumptions
which turned out to be correct, but they were big assumptions nonetheless:
1. As noted in my commentary above primes_is_eligible, I deduced that a number of digits 
divisible by 3 had to be the same digit getting replaced, and then wrote code based on the 
assumption that it would be exactly 3 digits getting replaced, rather than 3 or 6 or 9, et cetera.
2. In what I wrote for checkable_strings, I assumed that all of the eligible primes
had only one collection of 3+ identical digits, when in reality a prime might have had
multiple collections of 3+ identical digits.

I think this is the last Project Euler problem I'll do for the moment. I learned a lot
doing this problem, and it's good practice for implementing algorithms, but I'd like to move on
to something else.
'''

#This outputs a list of all primes less than the input, and also a boolean list saying whether or
#not a given number is prime.
'''
Let's use the sieve solution from Problem 10 to get a nice, big list of primes,
Except I'm using the 'worse' sieve because I don't want to think that hard about indexing
'''
def sieve_solution(j=2):
    crosslimit = math.ceil(math.sqrt(j))
    sieve = [True]*j
    for n in range(4,j,2):
        sieve[n] = False
    for n in range(3,crosslimit,2):
        if sieve[n]:
            for m in range(n**2,j,2*n):
                sieve[m] = False

    l = [2]
    for n in range(3,j):
        if sieve[n]:
            l.append(n)

    return (sieve,l)

#This outputs whether or not a given number is a prime that could be one of the eight primes
#that I'm looking for, taking in that given number as an input
'''
It'd make sense that we'd need to replace multiple digits since
there's 10 total numbers with a given replaced digit, and if we replace only one digit,
at least 3 of them will be divisible by 3, meaning we could only have at most 7 primes!
A little cleverness checking with modular arithmetic verifies that if we replace only 2 digits,
the same is true: If we replace 2 digits, we're incrementing a number by 10^n + 10^k
 = 10^(n-k) * 10^k + 10^k = (10^(n-k) + 1) * 10^k. 10^k = 1 mod 3, so we must be incrementing by
2 mod 3, meaning at least 3 will be divisible by 3.
A little further cleverness demonstrates that we need to replace a number of digits divisible by 3
in order to have an eligible candidate. Which eliminates a lot of our options!
'''
def prime_is_eligible(n = 56004,s=[]):
    try:
        if s[n] == False:
            return False
        if n < 56003:
            return False

        converted = list(str(n))
        for i in range(0, len(converted) - 1):
            t = 1
            for j in range(i + 1, len(converted) - 1):
                if converted[i] == converted[j]:
                    t += 1
            if t >= 3:
                return True
        return False
    except:
        return False

#This determines all of the identical digits of a given prime number
def locations_finder(l = []):
    try:
        for i in range(0,len(l) - 1):
            locations = [i]
            for j in range(i+1, len(l) - 1):
                if l[i] == l[j]:
                    locations.append(j)
            if len(locations) >= 3:
                return locations
        return []
    except:
        return []

#This outputs a list of all combinations where 3 identical digits of a number have
# been replaced by "None" where the number is written as a list
def checkable_strings(n = 56663):
    converted = tuple(str(n))
    interchangeable_locations = locations_finder(converted)

    list_of_replaceables = itertools.combinations(interchangeable_locations,3)

    output = []
    for t in list_of_replaceables:
        x = list(converted)
        l = list(t)
        for p in l:
            x[p] = None
        output.append(x)

    return output


#This takes as input one of the lists in the list outputted by checkable_strings
#and a digit i from 0 to 9 and outputs the number where the missing digits have been replaced
#by i
def list_to_int(l = [],i=0):
    x = 0
    for j in range(0, len(l)):
        if l[j] == None:
            x += i * (10 ** (len(l) - j - 1))
        else:
            x += int(l[j]) * (10 ** (len(l) - j - 1))
    return x

#This takes as input one of the lists in the list outputted by checkable_strings
#and the boolean list outputted by sieve_solution and checks whether each of the
#replacements of 3 digits of a given number is prime
def checker(n = [], s = []):
    primes_with_digits = []
    number = n
    for i in range(0,10):
        x = list_to_int(number,i)
        if s[x]:
            primes_with_digits.append(x)
    return primes_with_digits


def solution():

    start_time = time.time()
    s = sieve_solution(10**6)

    #This iterates through every prime, checks if it's a candidate for this replacing business,
    #if it is, then it runs thru all of the numbers that are that prime with 3 digits replaced
    #and sees if at least 8 of them are prime
    for i in s[1]:
        if prime_is_eligible(i,s[0]):
            for j in checkable_strings(i):
                primesfound = checker(j,s[0])
                if len(primesfound) >= 8:
                    #This extra if is needed in case the first digit of a prime has been replaced
                    #with a 0
                    if len(str(primesfound[0])) == len(str(primesfound[1])):
                        return (primesfound[0], time.time() - start_time)




if __name__ == "__main__":
    print(solution())