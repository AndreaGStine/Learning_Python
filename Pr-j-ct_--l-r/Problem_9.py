'''
Problem statement:

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import time
import math
start_time = time.time()

#The naive solution is not totally naive insofar as I write c in terms of a and b
#And I also only test b values up to 1000 - a
def naive_solution():
    for a in range(1,1000):
        for b in range(1,1000-a):
            if a+b+math.sqrt((a**2) + (b**2)) == 1000.0:
                return a*b*math.sqrt((a**2) + (b**2))


#But this is about 50x faster as it makes use of both equations rather than the Pythagorean one
#The trick in this one is that we have 3 variables: a, b, c satisfying 2 equations
#So heuristically there should be one variable of freedom
#That when constrained to integers restricts that variable to a single value
#Since there's only one variable of freedom, we should be able to write both b and c in terms of a
#And then we need only check that all of a, b, and c are integers.
def better_solution(n):
    for a in range(1,n):
        k = n - a
        b = (k ** 2 - a ** 2) / (2 * k)
        c = (k ** 2 + a ** 2) / (2 * k)
        if b == math.floor(b) and c == math.floor(c):
            return a*b*c


if __name__ == "__main__":
    print(naive_solution())
    print(better_solution(1000))
    print(time.time() - start_time)