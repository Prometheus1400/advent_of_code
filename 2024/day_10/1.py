with open("input.txt", "r") as f:
    lines = f.readlines()

GRID = [[int(num) for num in line if num != "\n"] for line in lines]
ROWS, COLS = len(GRID), len(GRID[0])

visited = set()


def dfs(r: int, c: int, cur: int = 0) -> int:
    """returns num of reachable 9's from this point"""
    if (
        r < 0
        or r >= ROWS
        or c < 0
        or c >= COLS
        # or (r, c) in visited
        or GRID[r][c] != (cur + 1)
    ):
        return 0
    visited.add((r, c))

    if GRID[r][c] == 9:
        return 1

    return (
        dfs(r + 1, c, GRID[r][c])
        + dfs(r, c + 1, GRID[r][c])
        + dfs(r - 1, c, GRID[r][c])
        + dfs(r, c - 1, GRID[r][c])
    )


total = 0
for r in range(ROWS):
    for c in range(COLS):
        if GRID[r][c] == 0:
            visited.clear()
            rating = dfs(r, c, -1)
            print(f"rating ({r}, {c}) = {rating}")
            total += rating
print(total)
