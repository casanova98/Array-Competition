import random

array = []
count = {}

n = random.randint(2, 100)
unique = random.randint(0, n-1)

array.append(unique)
for i in range(n):
    number = random.randint(0, n-1)
    
    if number != unique:
        for x in range(2):
            array.append(number)

for item in array:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

for item in count:
    if count[item] == 1:
        print(item)
        break
