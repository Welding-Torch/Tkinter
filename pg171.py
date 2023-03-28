# Generating Random Numbers

from random import random, sample

num = random()
print("Random Float 0.0-1.0:", num)
num = int(num * 10)
print("Random Integer 0-9:", num)

nums = []
i = 0
while i < 6:
    nums.append(int(random() * 10) + 1)
    i += 1
print('Random Multiple Intgers 1-10:', nums)
nums = sample(range(1,49), 6)
print('Random Integer Sample 1-49:', nums)