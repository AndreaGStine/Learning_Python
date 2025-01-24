'''
Problem statement:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import time
import math
start_time = time.time()


#The naive-naive solution was too slow for my patience, but I'm sure this
#could be further optimized
def solution():
    #This is roughly the same speed for the k given, but is asymptotically a little faster
    #than the naive isprime computation given below
    def isprimefactor(num=0, list=[]):
        for i in list:
            if num % i == 0:
                return False
        return True
    '''
    def isprime(num=0):
        max_check = math.ceil(math.sqrt(num))
        for i in range(2,max_check):
            if num % i == 0:
                return False
        return True
    '''

    factors = []
    k = 600851475143 
    max_factor = k
    max_test = math.ceil(math.sqrt(max_factor))
    n = 2
    while n <= max_test:
        while max_factor % n == 0:
            max_factor /= n
        if isprimefactor(n,factors):
            factors.append(n)
            max_test = math.ceil(math.sqrt(max_factor))
        n += 1
    return max_factor


if __name__ == "__main__":
    print(solution())
    print(time.time() - start_time)