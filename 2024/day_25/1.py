items = open("input.txt", "r").read().split("\n\n")
locks = []
keys = []
max_size = -1

for item in items:
    lines = item.splitlines()
    count = [0] * len(lines[0])
    max_size = len(lines) - 2

    if lines[0][0] == "#":
        # means it's a lock
        for line in lines[1:]:
            for i, c in enumerate(line):
                if c == "#":
                    count[i] += 1
        locks.append(tuple(count))
    else:
        # it's a key
        for line in lines[:-1]:
            for i, c in enumerate(line):
                if c == "#":
                    count[i] += 1
        keys.append(tuple(count))

unique_pairs = 0

for key in keys:
    for lock in locks:
        fits = True
        for n1, n2 in zip(key, lock):
            if n1 + n2 > max_size:
                fits = False
                break
        if fits:
            unique_pairs += 1

print(unique_pairs)
