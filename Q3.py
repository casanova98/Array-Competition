import random

array = []

n = random.randint(2, 100)

for i in range(n):
    array.append(random.randint(1, n))

def linear(n, target):
    for i in n:
        if i == target:
            return 1
    return -1

x = random.randint(1, n)

result = linear(array, x)
if result == 1:
    print(x, "exists in array.")
else:
    print(x, "does not exist in array.")
