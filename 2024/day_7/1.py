from operator import add, mul
from re import findall

with open("sample.txt", "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    target, x, *args = map(int, findall(r"\d+", line))
    intermediaries = [x]
    for y in args:
        print(intermediaries)
        intermediaries = [op(x,y) for x in intermediaries for op in (add, mul)]
    print(intermediaries)

    # at this point intermediaries contains the final possibilities
    if target in intermediaries:
        total += target

print(total)
