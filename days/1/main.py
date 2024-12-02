from collections import Counter

a = []
b = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        x, y = line.split()
        x = int(x.strip())
        y = int(y.strip())
        a.append(x)
        b.append(y)

# part 1
# a.sort()
# b.sort()
# print(sum([abs(x - y) for x,y in zip(a, b)]))

# part 2
b_count = Counter(b)
print(sum([x * b_count[x] for x in a]))
