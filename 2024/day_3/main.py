import re

with open("input.txt", "r") as file:
    lines = file.readlines()
    text = "".join(lines)

# part 1
# mul_pattern = r"(mul\(\d{1,3},\d{1,3}\))"
# matches = re.findall(mul_pattern, text)
# if not matches:
#     raise RuntimeError("pattern not matching")
#
# res = 0
# for mul in matches:
#     args = mul.replace(')', "").split('n')[1]
#     x, y = args.split(",")
#     res += int(x) * int(y)
#
# print(res)

mul_pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))"
matches = re.findall(mul_pattern, text)
if not matches:
    raise RuntimeError("pattern not matching")
res = 0
enabled = True
for m in matches:
    if m == "do()":
        enabled = True
    elif m == "don't()":
        enabled = False
    else:
        if enabled:
            args = m.replace(")", "").split("(")[1]
            x, y = args.split(",")
            res += int(x) * int(y)


print(res)



