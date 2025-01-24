'''
Problem statement:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import time
start_time = time.time()

#Naive solution:
def naive_solution():
    sum = 0
    for n in range(1,1000):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

if __name__ == "__main__":
    print(naive_solution())
    print((time.time() - start_time))
#Seeing as the naive solution takes an amount of time that rounds to 0, I'll stick with it.