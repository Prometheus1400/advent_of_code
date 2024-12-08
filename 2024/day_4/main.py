target = "XMAS"

with open("input.txt", "r") as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        row = []
        for c in line:
            if c.strip():
                row.append(c)
        grid.append(row)

ROWS = len(grid)
COLS = len(grid[0])

def search(r: int, c: int, i_dir:int, j_dir:int, cur: int) -> int:
    if (r < 0 or ROWS <= r or
        c < 0 or COLS <= c or
        cur >= len(target) or
        grid[r][c] != target[cur]):
        return 0

    if cur == len(target) - 1:
        return 1

    return search(r+i_dir, c+j_dir, i_dir, j_dir, cur + 1)

def check_letter(r, c, letter) -> bool:
    if (r < 0 or ROWS <= r or
        c < 0 or COLS <= c or
        grid[r][c] != letter):
        return False
    return True

def check_x(r, c) -> int:
    res = True
    if not (check_letter(r +1, c + 1, "S") and check_letter(r - 1, c - 1, "M") or 
        check_letter(r + 1, c + 1, "M") and check_letter(r - 1, c - 1, "S")):
        res = False
    if not (check_letter(r - 1, c + 1, "S") and check_letter(r + 1, c - 1, "M") or 
        check_letter(r - 1, c + 1, "M") and check_letter(r + 1, c - 1, "S")):
        res = False
    return res

total = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == "A" and check_x(r, c):
            total += 1
print(total)
