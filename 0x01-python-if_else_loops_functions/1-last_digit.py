#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10

if number < 0:
    last_num = - (last_num)

print(f"last digit of {number:d} is {last_num:d} and is", end=" ")
if last_num > 5:
    print("greater than 5")
elif last_num == 0:
    print("0")
elif last_num < 6 and last_num != 0:
    print("less than 6 and not 0")
