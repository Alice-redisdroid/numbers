import random

numbers = []

for i in range(3, 21):
    numbers.append(i)

random_number = random.choice(numbers)

for first in range(1,random_number):
    for second in range(first+1, random_number):
         if random_number % (first + second) == 0:
             print(first, second, sep='', end='')


