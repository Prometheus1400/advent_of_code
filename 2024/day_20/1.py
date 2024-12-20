from collections import deque, Counter

GRID = [[c for c in line.strip()] for line in open("input.txt", "r")]
ROWS, COLS = len(GRID), len(GRID[0])
START = next((r, c) for c in range(COLS) for r in range(ROWS) if GRID[r][c] == "S")
END = next((r, c) for c in range(COLS) for r in range(ROWS) if GRID[r][c] == "E")


def get_costs(start: tuple[int, int]) -> dict[tuple[int, int], int]:
    """
    bfs to get the costs at every point

    figure i can use it when 'cheating' and creating tunnels, if I can connect
    2 different paths I can use the difference in cost to figure out how much
    time the cheat is saving
    """
    costs = {
        (r, c): float("inf")
        for c in range(COLS)
        for r in range(ROWS)
        if GRID[r][c] != "#"
    }
    costs[start] = 0
    q = deque([(0, start)])
    visited = {(start)}
    while q:
        cost, (r, c) = q.popleft()
        for d_r, d_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r + d_r, c + d_c
            new_pos = (new_r, new_c)

            if new_pos in costs and new_pos not in visited:
                visited.add(new_pos)
                costs[new_pos] = cost + 1
                q.append((cost + 1, new_pos))

    return costs


all_cheats = {}


def dfs(
    cur: tuple[int, int],
    start: tuple[int, int],
    costs: dict[tuple[int, int], int],
    i: int = 2,
    cur_cheat: list[tuple[int, int]] | None = None,
):
    """
    length 2 dfs starting from a point in the path, only looking over '#' to try to find another path using the cheat
    """
    r, c = cur
    if r < 0 or r >= ROWS or c < 0 or c >= COLS or i < 0:
        return
    if i == 0 and GRID[r][c] == "#":
        return

    if i == 2:
        # we are at the start, immediately run dfs
        dfs((r + 1, c), start, costs, i - 1, cur_cheat)
        dfs((r - 1, c), start, costs, i - 1, cur_cheat)
        dfs((r, c + 1), start, costs, i - 1, cur_cheat)
        dfs((r, c - 1), start, costs, i - 1, cur_cheat)
    if i == 1:
        if GRID[r][c] != "#":
            return
        dfs((r + 1, c), start, costs, i - 1, [(r, c)])
        dfs((r - 1, c), start, costs, i - 1, [(r, c)])
        dfs((r, c + 1), start, costs, i - 1, [(r, c)])
        dfs((r, c - 1), start, costs, i - 1, [(r, c)])
    if i == 0:
        c1, c2 = costs[start], costs[(r, c)]
        saved = ((c2 - c1) - 1) - 1
        if saved > 0:
            all_cheats[(start, (r, c))] = saved


costs = get_costs(START)
# for r in range(ROWS):
#     for c in range(COLS):
#         if (r, c) not in costs:
#             print(f"{'#':^3}", end="")
#         else:
#             print(f"{costs[(r, c)]:^3}", end="")
#     print()
for r in range(ROWS):
    for c in range(COLS):
        if (r, c) in costs:
            dfs((r, c), (r, c), costs)

print(Counter([v for v in all_cheats.values()]))
print(len([cheat for cheat in all_cheats.values() if cheat >= 100]))
