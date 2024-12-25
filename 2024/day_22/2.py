import re
from collections import defaultdict, deque

inits = list(map(int, re.findall(r"\d+", open("input.txt", "r").read())))

def get_next_secret(secret:int)->int:
    secret = secret ^ (secret * 64)
    secret = secret % 16777216
    secret = secret ^ (secret // 32)
    secret = secret % 16777216
    secret = secret ^ (secret * 2048)
    secret = secret % 16777216
    return secret

def get_first_digit(num: int) -> int:
    return num % 10

seqs = defaultdict(int)
for i, secret in enumerate(inits):
    prevs = deque()
    seen = set()
    prev = get_first_digit(secret)
    for _ in range(2000):
        secret = get_next_secret(secret)
        price = get_first_digit(secret)

        while len(prevs) >= 4:
            prevs.popleft()
        if prev != None: prevs.append(price - prev)

        prev_tuple = tuple(prevs)
        if len(prev_tuple) >= 4 and prev_tuple not in seen:
            seqs[prev_tuple] += price
            seen.add(prev_tuple)
        prev = price

best_seq = None
most_bananas = -1

for seq, bananas in seqs.items():
    if bananas > most_bananas:
        most_bananas = bananas
        best_seq = seq

print(best_seq, most_bananas)
