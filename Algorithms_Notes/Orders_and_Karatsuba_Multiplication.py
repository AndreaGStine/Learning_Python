'''
Big-O Notation:
f(x) = O(g(x)) iff there is an n0 > 0, c > 0 st for all n > n0, f(n) <= cg(x)
(f is bounded above by g)

f(x) = o(g(x)) iff for any e > 0, there is an n0 > 0 st for all n > n0, f(n) <= eg(x)
(f is dominated by g asymptotically)

f(x) = Omega(g(x)) iff g(x) = O(f(x))
(f is bounded below by g)

f(x) = Theta(g(x)) iff f(x) = Omega(g(x)) and f(x) = O(g(x))
(f is of the same order as g)
'''

import time
import math
import sys

sys.set_int_max_str_digits(10**9)

def slow_multiply(x,y):
    m = [int(i) for i in str(x)]
    n = [int(j) for j in str(y)]
    z = 0
    for i in range(0,len(m)):
        for j in range(0,len(n)):
            z += (10**(len(m) + len(n) - i - j - 2))*m[i]*n[j]
    return z

def karatsuba_multiply(x,y):
    a = [int(i) for i in str(x)]
    b = [int(j) for j in str(y)]
    if (x < 10 or y < 10):
        return slow_multiply(x,y)
    else:
        m = max(len(a),len(b))
        m2 = math.floor(m/2)

        high1, low1 = math.floor(x / (10**m2)), x % (10**m2)
        high2, low2 = math.floor(y / (10**m2)), y % (10**m2)

        z0 = karatsuba_multiply(low1,low2)
        z1 = karatsuba_multiply(low1 + high1,low2 + high2)
        z2 = karatsuba_multiply(high1,high2)

        return (z2*(10**(m2*2))) + ((z1 - z2 - z0)*(10**(m2))) + z0

def mult_runtime(n,m):
    print('The product is: ', n*m)
    start_time = time.time()
    for i in range(0,20):
        slow_multiply(n, m)
    print('Slow multiplication runtime over 20 trials is: %s seconds' % (time.time() - start_time))
    start_time = time.time()
    for i in range(0,20):
        karatsuba_multiply(n, m)
    print('Karatsuba multiplication runtime over 20 trials is: %s seconds' % (time.time() - start_time))
    start_time = time.time()
    for i in range(0,20000):
        n*m
    print('Pythons built-in multiplication runtime over 20000 trials is: %s seconds' % (time.time() - start_time))

def time_complexity(n,m):
    def very_slow_sum(a,b):
        s = a
        for i in range(0,b):
            s += 1
        return s

    def very_slow_prod(a,b):
        p = 0
        for i in range(0,b):
           p = very_slow_sum(p,a)
        return p

    # O(a^b) complexity for computing a^b:
    def very_slow_exp(a,b):
        e = int(a)
        for i in range(0,b-1):
            e = very_slow_prod(e,a)
        return e

    # O(n^3) complexity for computing a^b:
    def mid_exp(a,b):
        e = int(a)
        for i in range(0,b-1):
            e = slow_multiply(e,a)
        return e
    '''
    start_time = time.time()
    x = slow_exp(n,m)

    print((x,time.time() - start_time))
    
    start_time = time.time()
    y = mid_exp(n,m)
    print((y,time.time() - start_time))
    '''
    start_time = time.time()
    z = n**m
    print(time.time() - start_time)
    #Observationally, exponentiation in python seems to be roughly O(log(n))

    def fast_exp(a,b):
        if b == 0:
            return 1

        out = fast_exp(a,b//2)
        out = out * out

        if b < 0:
            a = 1 / a
            b = -b

        if b % 2 != 0:
            out = out * a
        return out
    start_time = time.time()
    w = fast_exp(n,m)
    print(time.time() - start_time)
    #Well how about that! It looks like binary expansion is what Python uses. Runtimes are nearly identical.


if __name__ == "__main__":
    mult_runtime(math.floor(math.pi * (10**(300))),math.floor(math.pi ** 600))

    #time_complexity(13,40000)