from collections import defaultdict
from aoc_utils.input_helpers import Input, initialize_day, get_text

"""
row, col
A1 = [5, 6]
A2 = [8, 8]

antinodes:
    slope = [-3, -2]
    AN1 = [2, 4]
    AN2 = [11, 10]
"""

initialize_day(9)
input = get_text(9, Input.INPUT)
file_blocks = []
file_id = 0
space = False
for c in input:
    if space:
        file_blocks.extend(["."] * int(c))
    else:
        file_blocks.extend([file_id] * int(c))
        file_id += 1
    space = not space

r = len(file_blocks) - 1
l = 0
while l < r:
    if file_blocks[l] == ".":
        while l < r and file_blocks[r] == ".":
            r -= 1
        if l >= r:
            break
        file_blocks[l], file_blocks[r] = file_blocks[r], file_blocks[l]
    l += 1


total = 0
for i, n in enumerate(file_blocks):
    if n == ".":
        break
    total += i * n
print(total)

