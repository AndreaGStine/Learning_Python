import time
import random

def arithmetic_problem():
    current_time = time.time()
    score = 0
    while time.time() - current_time < 120:
        answer = 1
        result = 0
        while answer != result:
            r1 = random.random()
            try:
                if r1 < 0.25:
                    r2 = random.randint(2, 1000)
                    r3 = random.randint(2, 1000)
                    print(r2, '+', r3)
                    answer = r2 + r3
                    result = int(input())
                elif r1 < 0.5:
                    r2 = random.randint(2, 100)
                    r3 = random.randint(2, 100)
                    print(r2, '*', r3)
                    answer = r2 * r3
                    result = int(input())
                elif r1 < 0.75:
                    r2 = random.randint(2, 1000)
                    r3 = random.randint(2, 1000)
                    print(r2 + r3, '-', r3)
                    answer = r2
                    result = int(input())
                else:
                    r2 = random.randint(2, 100)
                    r3 = random.randint(2, 100)
                    print(r2*r3, '/', r3)
                    answer = r2
                    result = int(input())

                if result == answer:
                    score += 1
                    print('Right')
                    break
                else:
                    print('Wrong')
                    pass
            except:
                break

        else:
            print('Wrong')
    print('Score:', score)
    return score

if __name__ == "__main__":
    while True:
        arithmetic_problem()
        cont = input('Do you want to try again?')
        if cont != 'Yes' and cont != 'Y' and cont != 'y' and cont != 'yes' and cont != '':
            break
