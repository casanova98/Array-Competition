import random
highest = 0
lowest = 100000000
array = []

n = random.randint(2, 100)

for i in range(n):
    array.append(random.randint(1, n))

for i in array:
    if i < lowest:
        lowest = i
    elif i > highest:
        highest = i

print("Lowest", lowest)
print("Highest:", highest)
