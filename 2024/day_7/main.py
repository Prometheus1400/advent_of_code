# with open("input.txt", "r") as f:
#     lines = f.readlines()
#
# eqs = []
# for line in lines:
#     target, args = line.strip().split(":")
#     target = int(target)
#     args = args.strip().split(" ")
#     args = [int(x) for x in args]
#     eqs.append((target, args))
#
# def solveable(args: list[int], target: int, i: int, cur: int | None = None) -> bool:
#     if cur and cur == target:
#         return True
#     if (cur and cur > target) or i >= len(args):
#         return False
#
#     if not cur:
#         return solveable(args, target, i + 1, args[i])
#
#     return solveable(args, target, i + 1, cur * args[i]) or solveable(args, target, i + 1, cur + args[i])
#
# res = []
# for eq in eqs:
#     if solveable(eq[1], eq[0], 1, eq[1][0]):
#         print(eq, "->", True)
#         res.append(eq[0])
#     # print(solveable(eq[1], eq[0], 0))
#
# print(sum(res))
from re import findall
from operator import add, mul

cat = lambda x,y: int(str(x) + str(y))

ans = 0
for line in open('input.txt'):
    tgt, x, *Y = map(int, findall(r'\d+', line))

    X = [x]
    for y in Y:
        X = [op(x,y) for x in X for op in (add,mul)]

    if tgt in X: ans += tgt

print(ans)
