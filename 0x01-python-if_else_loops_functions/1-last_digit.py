#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number[-1])
last_d = int(last)
if last_d > 5:
    print(f'The last digit of {number} is {last_d} and is greater than 5')
elif last_d == 0:
    print(f'The last digit of {number} is {last_d} and is 0')
elif last_d < 6 and last_d != 0:
    print(f'The last digit of {number} is {last_d} and is less than 6 and not 0')
