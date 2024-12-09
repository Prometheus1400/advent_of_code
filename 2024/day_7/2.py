from operator import add, mul
from re import findall

with open("sample.txt", "r") as f:
    lines = f.readlines()

def cat(a: int, b:int) -> int:
    return int(str(a) + str(b))

total = 0
for line in lines:
    target, x, *args = map(int, findall(r"\d+", line))
    intermediaries = [x]
    for y in args:
        intermediaries = [op(x,y) for x in intermediaries for op in (add, mul, cat)]

    # at this point intermediaries contains the final possibilities
    if target in intermediaries:
        total += target

print(total)
