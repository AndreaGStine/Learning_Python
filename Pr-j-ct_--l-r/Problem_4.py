'''
Problem statement:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

'''
import time
import math
start_time = time.time()


def ispalindrome(string=''):
    split = math.floor(len(string) / 2)
    end_char = len(string) - 1
    for i in range(0, split):
        if string[i] != string[end_char - i]:
            return False
    return True

def naive_solution():
    palindromes = []
    for i in range(100,999):
        for j in range(i,999):
            k = i*j
            if ispalindrome(str(k)):
                palindromes.append(k)
    return max(palindromes)


if __name__ == "__main__":
    print(naive_solution())
    print(time.time() - start_time)