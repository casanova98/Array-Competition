import random

array = []
count = {}
duplicates = []

n = random.randint(2, 100)

for i in range(n):
    array.append(random.randint(0, n-1))
