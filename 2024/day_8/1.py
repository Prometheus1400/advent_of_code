from collections import defaultdict
from aoc_utils.input_helpers import Input, initialize_day, get_lines

"""
row, col
A1 = [5, 6]
A2 = [8, 8]

antinodes:
    slope = [-3, -2]
    AN1 = [2, 4]
    AN2 = [11, 10]
"""

initialize_day(8)
lines = get_lines(8, Input.INPUT)
grid = []
for line in lines:
    grid.append([c for c in line.strip()])
ROWS, COLS = len(grid), len(grid[0])

antennas = defaultdict(list)
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] != ".":
            antennas[grid[row][col]].append((row, col))

unique_antinodes = set()
num_antinodes = 0
for locations in antennas.values():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            r1, c1 = locations[i]
            r2, c2 = locations[j]
            delta_r, delta_c = r1 - r2, c1 - c2
            antinodes = [(r1 + delta_r, c1 + delta_c), (r2 - delta_r, c2 - delta_c)]
            for r, c in antinodes:
                if (
                    (0 <= r < ROWS)
                    and (0 <= c < COLS)
                    and (r, c) not in unique_antinodes
                ):
                    unique_antinodes.add((r, c))
                    num_antinodes += 1

print(num_antinodes)
