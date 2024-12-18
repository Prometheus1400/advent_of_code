from collections import namedtuple
import heapq

Reindeer = namedtuple("Reindeer", ["r", "c", "dir"])
def cost_turn(reindeer: Reindeer, new_dir: str) -> int | None:
        """
        returns the cost of the turn
        returns None if turning 180 degrees (not allowed)
        """
        if new_dir == reindeer.dir:
            return 0
        if (
            new_dir == "NORTH"
            and reindeer.dir == "SOUTH"
            or new_dir == "EAST"
            and reindeer.dir == "WEST"
            or new_dir == "SOUTH"
            and reindeer.dir == "NORTH"
            or new_dir == "WEST"
            and reindeer.dir == "EAST"
        ):
            return None
        return 1000

def djikstras(grid: list[list[str]], reindeer: Reindeer) -> int:
    visited = set()
    deltas = {"NORTH": (-1, 0), "EAST": (0, 1), "SOUTH": (1, 0), "WEST": (0, -1)}
    pq = [(0, reindeer)]
    while pq:
        cur_cost, cur_reindeer = heapq.heappop(pq)
        if cur_reindeer in visited:
            continue
        visited.add(cur_reindeer)
        if grid[cur_reindeer.r][cur_reindeer.c] == "E":
            return cur_cost
        for new_dir, (delt_r, delt_c) in deltas.items():
            turn_cost = cost_turn(cur_reindeer, new_dir)
            if turn_cost != None and grid[cur_reindeer.r + delt_r][cur_reindeer.c + delt_c] != "#":
                heapq.heappush(pq, (cur_cost + turn_cost + 1, Reindeer(cur_reindeer.r + delt_r, cur_reindeer.c + delt_c, new_dir)))

    raise RuntimeError()

GRID = []
with open("input.txt", "r") as file:
    for line in file:
        GRID.append([c for c in line.strip()])

ROWS, COLS = len(GRID), len(GRID[0])

for r in range(ROWS):
    for c in range(COLS):
        if GRID[r][c] == "S":
            reindeer = Reindeer(r, c, "EAST")

print(djikstras(GRID, reindeer))
