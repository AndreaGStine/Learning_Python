import time
import random

def memory_arithmetic_problem(t):
    current_time = time.time()
    score = 0
    r2 = r2 = random.randint(2, 100)
    print('The first term is: ', r2)
    while time.time() - current_time < t:
        answer = 1
        result = -300
        while answer != result:
            r1 = random.random()
            try:
                if r1 < 0.25:
                    r3 = random.randint(2, 100)
                    print('... +', r3)
                    answer = r2 + r3
                elif r1 < 0.5:
                    r3 = random.randint(2, 10)
                    print('... *', r3)
                    answer = r2 * r3
                elif r1 < 0.75:
                    r3 = random.randint(2, 100)
                    print('... -', r3)
                    answer = r2 - r3
                else:
                    r3 = random.randint(2, 10)
                    print('... //', r3)
                    answer = r2//r3
                while result != answer:
                    result = int(input('Input answer: '))
                score += 1
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                print('Right')
                r2 = answer
            except:
                break
    print('Score:', score)
    return score

if __name__ == "__main__":
    while True:
        t = int(input('Set time for the round, in seconds.'))
        memory_arithmetic_problem(t)
        cont = input('Do you want to try again?')
        if cont != 'Yes' and cont != 'Y' and cont != 'y' and cont != 'yes' and cont != '':
            break
