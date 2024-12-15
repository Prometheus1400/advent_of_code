from dataclasses import dataclass


@dataclass
class Robot:
    r: int
    c: int

    def __simple_case_move(self, grid: list[list[str]], dir_r: int, dir_c: int) -> bool:
        new_r, new_c = self.r + dir_r, self.c + dir_c
        if grid[new_r][new_c] == "#":
            return True
        if grid[new_r][new_c] == ".":
            grid[self.r][self.c] = "."
            self.r, self.c = new_r, new_c
            grid[self.r][self.c] = "@"
            return True
        return False

    def __move_boxes_vertically(self, grid: list[list[str]], dir: int):
        """
        Do a BFS until
         - we find a row with at least 1 '#' which means we cannot
        move the boxes up
         - or until we find a row with all '.' which means we can break and move
        the boxes up level by level.

        We should store each row as we go as well as the indices of items in
        the row so we can easily reverse-traverse it and shift items up
        """

        def get_match(box_half: tuple[int, int]) -> tuple[int, int] | None:
            r, c = box_half
            if grid[r][c] == "[":
                return (r, c + 1)
            if grid[r][c] == "]":
                return (r, c - 1)
            raise RuntimeError("can't get match for non box type")

        r = self.r
        levels = [[(self.r, self.c)]]
        level = levels[0]
        while True:
            next_level = set()
            moveable = True
            for r, c in level:
                if grid[r + dir][c] in "[]":
                    next_level.add((r + dir, c))
                    next_level.add(get_match((r + dir, c)))
                if grid[r + dir][c] == "#":
                    moveable = False

            if not moveable:
                # do nothing
                return

            if len(next_level) == 0:
                # the current level is moveable and no boxes above
                # aka: 'next_level' is all '.'
                for lvl in levels[::-1]:
                    for item in lvl:
                        r, c = item
                        grid[r + dir][c] = grid[r][c]
                        grid[r][c] = "."
                self.r += dir
                return

            level = list(next_level)
            levels.append(level)
            r += dir

    def __move_boxes_horizontally(self, grid: list[list[str]], dir: int):
        c_start = self.c
        c = self.c + dir
        while grid[self.r][c] != "#":
            if grid[self.r][c] == ".":
                for i in range(c - dir, c_start - dir, -dir):
                    grid[self.r][i + dir] = grid[self.r][i]
                grid[self.r][c_start] = "."
                self.c += dir
                break
            c += dir

    def move(self, dir: str, grid: list[list[str]]) -> None:
        """
        modified the grid as side effect also updates position

        can assume the new position is always in bounds - since we will
        never move to an actual edge
        """
        match dir:
            case ">":
                if self.__simple_case_move(grid, 0, 1):
                    return
                self.__move_boxes_horizontally(grid, 1)
            case "v":
                if self.__simple_case_move(grid, 1, 0):
                    return
                self.__move_boxes_vertically(grid, 1)
            case "<":
                if self.__simple_case_move(grid, 0, -1):
                    return
                self.__move_boxes_horizontally(grid, -1)
            case "^":
                if self.__simple_case_move(grid, -1, 0):
                    return
                self.__move_boxes_vertically(grid, -1)


GRID = []
robot = None
with open("input.txt", "r") as file:
    map, movements = file.read().split("\n\n")
    map, movements = map.strip(), movements.strip()
    r = 0
    for line in map.splitlines():
        row = []
        c = 0
        for char in line:
            if char in "#.":
                row.extend([char, char])
            elif char == "@":
                robot = Robot(r, c)
                row.extend([char, "."])
            elif char == "O":
                row.extend(["[", "]"])
            c += 2
        GRID.append(row)
        r += 1
if not robot:
    raise RuntimeError("didn't get robot start pos")
ROWS, COLS = len(GRID), len(GRID[0])

for movement in movements:
    robot.move(movement, GRID)

total = 0
for r in range(ROWS):
    for c in range(COLS):
        if GRID[r][c] == "[":
            total += 100 * r + c
print(total)
