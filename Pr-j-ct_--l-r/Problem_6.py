'''
Problem statement:

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
import time
import math
start_time = time.time()

#The cheeky solution is that I remember what the formula is for the sum of squares,
#which makes the computation very fast
def cheeky_solution(k=100):
    sum_of_squares = int(k*(k+1)*(2*k+1)/6)
    square_of_sum = (int(k*(k+1)/2))**2
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    print(cheeky_solution(100))
    print(time.time() - start_time)