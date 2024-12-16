GRID = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        GRID.append([c for c in line])
ROWS, COLS = len(GRID), len(GRID[0])

area_visited = set()
perimiter_visited = set()
perimiter_visiting = set()


def get_area(prev_plant: str | None, r: int, c: int) -> int:
    """easy this is just a DFS/BFS"""
    if (
        r < 0
        or r >= ROWS
        or c < 0
        or c >= COLS
        or (r, c) in area_visited
        or (prev_plant and prev_plant != GRID[r][c])
    ):
        return 0
    area_visited.add((r, c))
    area = (
        1
        + get_area(GRID[r][c], r + 1, c)
        + get_area(GRID[r][c], r - 1, c)
        + get_area(GRID[r][c], r, c + 1)
        + get_area(GRID[r][c], r, c - 1)
    )
    return area


max_perimiter = -1


def get_perimiter(prev_plant: str | None, cur_perimiter: int, r: int, c: int) -> int:
    """this is more complicated
    - initial plot starts with perimiter 4
    - when calling get_perimiter on adjacent plot the current plots
      perimiter must be decremented by 1 and the start_perimiter of
      that adjacent plot must be one less than the current start_perimiter
    """
    if (
        r < 0
        or r >= ROWS
        or c < 0
        or c >= COLS
        or (r, c) in perimiter_visiting
        or (prev_plant and prev_plant != GRID[r][c])
    ):
        return cur_perimiter
    if (r, c) not in perimiter_visited:
        # seeing for the first time
        perimiter_visited.add((r, c))
        if prev_plant:
            # if coming from a previous place:
            cur_perimiter += 4 - 2
        else:
            cur_perimiter += 4
            # don't want to backtrack but want to consider other branches
            # that have been visited that's why we have two sets
        perimiter_visiting.add((r, c))
        cur_perimiter = get_perimiter(GRID[r][c], cur_perimiter, r + 1, c)
        cur_perimiter = get_perimiter(GRID[r][c], cur_perimiter, r - 1, c)
        cur_perimiter = get_perimiter(GRID[r][c], cur_perimiter, r, c + 1)
        cur_perimiter = get_perimiter(GRID[r][c], cur_perimiter, r, c - 1)
        perimiter_visiting.remove((r, c))
    elif (r, c) in perimiter_visited:
        # meaning we've already added the xtra perimiter from this plot
        # but now we found it has another edge that will decrease our perimiter
        cur_perimiter -= 2

    return cur_perimiter


total_area = 0
for r in range(ROWS):
    for c in range(COLS):
        plot_area = get_area(None, r, c)
        if plot_area > 0:
            plot_perimiter = get_perimiter(None, 0, r, c)
            total_area += plot_area * plot_perimiter

print(total_area)
