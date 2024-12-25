import re

inits = list(map(int, re.findall(r"\d+", open("input.txt", "r").read())))

total = 0
for secret in inits:
    for _ in range(2000):
        secret = secret ^ (secret * 64)
        secret = secret % 16777216

        secret = secret ^ (secret // 32)
        secret = secret % 16777216

        secret = secret ^ (secret * 2048)
        secret = secret % 16777216
    total += secret
print(total)

