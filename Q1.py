import random

array = []
count = {}
duplicates = []

n = random.randint(2, 100)

for i in range(n):
    array.append(random.randint(0, n-1))

for item in array:
    if item in count:
        if item not in duplicates:
            duplicates.append(item)
    else:
        count[item] = 1

print("Number of duplicates:", len(duplicates))
