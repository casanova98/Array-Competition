import random

array = []
remove = []

n = random.randint(2, 100)

for i in range(n):
    array.append(random.randint(1, n))

for item in array:
    if item not in remove:
        remove.append(item)

def quick_sort(n):
    if n == []:
        return []
    else:
        pivot = n[0]
        
        big = []
        small = []
        
        for i in n[1:]:
            if i > pivot:
                big.append(i)
            else:
                small.append(i)
        
        return quick_sort(small) + [pivot] + quick_sort(big)

print(quick_sort(remove))
