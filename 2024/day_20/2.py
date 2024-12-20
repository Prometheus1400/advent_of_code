from collections import deque

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

    return costs  # pyright: ignore


all_cheats = {}
visiting = set()
cheat_len = 20

def manhattan_distance(start: tuple[int, int], target:tuple[int, int]):
    (r1,c1) = start
    (r2,c2) = target
    return abs(r1 - r2) + abs(c1 - c2)

costs = get_costs(START)
for r in range(ROWS):
    for c in range(COLS):
        if (r, c) in costs:
            for r2 in range(ROWS):
                for c2 in range(COLS):
                    if (r, c) == (r2, c2) or (r2, c2) not in costs or costs[(r2,c2)] <= costs[(r,c)]:
                        continue
                    dist = manhattan_distance((r,c), (r2,c2))
                    if dist <= cheat_len:
                        all_cheats[((r,c), (r2,c2))] = costs[(r2,c2)] - (costs[(r,c)] + dist)


print(len([cheat for cheat in all_cheats.values() if cheat >= 100]))
