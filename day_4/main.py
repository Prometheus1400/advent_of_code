target = "XMAS"

with open("sample.txt", "r") as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        row = []
        for c in line:
            if c.strip():
                row.append(c)
        grid.append(row)

ROWS, COLS = len(grid), len(grid[0])
visiting = set()
def dfs(r: int, c: int, cur: int) -> int:
    if ((r, c) in visiting or 
        r < 0 or ROWS <= r or
        c < 0 or COLS <= c or
        cur >= len(target) or
        grid[r][c] != target[cur]):
        return 0

    if cur == len(target) - 1:
        return 1

    visiting.add((r, c))
    val = (
            dfs(r - 1, c, cur + 1) +
            dfs(r, c - 1, cur + 1)+
            dfs(r + 1, c, cur + 1)+
            dfs(r, c + 1, cur + 1)+
            dfs(r - 1, c - 1, cur + 1)+
            dfs(r - 1, c + 1, cur + 1)+
            dfs(r + 1, c - 1, cur + 1)+
            dfs(r + 1, c + 1, cur + 1)
            )

    visiting.remove((r, c))
    return val

total = 0
for r in range(ROWS):
    for c in range(COLS):
        total += dfs(r, c, 0)

print(total)
