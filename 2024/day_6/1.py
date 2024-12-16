G = {i+j*1j: c for i,r in enumerate(open('sample.txt'))
               for j,c in enumerate(r.strip())}
print(G)
start = min(p for p in G if G[p] == '^')
print(start)
# GRID = [[c for c in line if c != "\n"] for line in open("sample.txt", "r").readlines()]
# ROWS, COLS = len(GRID), len(GRID[0])
#
# r, c, dir = -1, -1, ""
# for row in range(ROWS):
#     for col in range(COLS):
#         if GRID[row][col] == "^":
#             r, c, dir = row, col, "up"
#         elif GRID[row][col] == ">":
#             r, c, dir = row, col, "right"
#         elif GRID[row][col] == "v":
#             r, c, dir = row, col, "down"
#         elif GRID[row][col] == "<":
#             r, c, dir = row, col, "left"
#
#
#
