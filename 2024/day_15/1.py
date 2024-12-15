from dataclasses import dataclass


@dataclass
class Robot:
    r: int
    c: int

    def __simple_case_move(self, grid: list[list[str]], new_r: int, new_c: int) -> bool:
        if grid[new_r][new_c] == "#":
            return True
        if grid[new_r][new_c] == ".":
            grid[self.r][self.c] = "."
            self.r, self.c = new_r, new_c
            grid[self.r][self.c] = "@"
            return True
        return False

    def move(self, dir: str, grid: list[list[str]]) -> None:
        """
        modified the grid as side effect also updates position

        can assume the new position is always in bounds - since we will
        never move to an actual edge
        """
        match dir:
            case ">":
                if self.__simple_case_move(grid, self.r, self.c + 1):
                    return
                # means it's a '0' need to check if there is an empty space in this direction to compress
                c_start = self.c
                c = self.c + 1
                while grid[self.r][c] != "#":
                    if grid[self.r][c] == ".":
                        for i in range(c - 1, c_start - 1, -1):
                            grid[self.r][i + 1] = grid[self.r][i]
                        grid[self.r][c_start] = "."
                        self.c += 1
                        break
                    c += 1
            case "v":
                if self.__simple_case_move(grid, self.r + 1, self.c):
                    return
                r_start = self.r
                r = self.r + 1
                while grid[r][self.c] != "#":
                    if grid[r][self.c] == ".":
                        for i in range(r - 1, r_start - 1, -1):
                            grid[i + 1][self.c] = grid[i][self.c]
                        grid[r_start][self.c] = "."
                        self.r += 1
                        break
                    r += 1
            case "<":
                if self.__simple_case_move(grid, self.r, self.c - 1):
                    return
                c_start = self.c
                c = self.c - 1
                while grid[self.r][c] != "#":
                    if grid[self.r][c] == ".":
                        for i in range(c + 1, c_start + 1):
                            grid[self.r][i - 1] = grid[self.r][i]
                        grid[self.r][c_start] = "."
                        self.c -= 1
                        break
                    c -= 1
            case "^":
                if self.__simple_case_move(grid, self.r - 1, self.c):
                    return
                r_start = self.r
                r = self.r - 1
                while grid[r][self.c] != "#":
                    if grid[r][self.c] == ".":
                        for i in range(r + 1, r_start + 1):
                            grid[i - 1][self.c] = grid[i][self.c]
                        grid[r_start][self.c] = "."
                        self.r -= 1
                        break
                    r -= 1


GRID = []
with open("input.txt", "r") as file:
    map, movements = file.read().split("\n\n")
    map, movements = map.strip(), movements.strip()
    for line in map.splitlines():
        GRID.append([c for c in line])

ROWS, COLS = len(GRID), len(GRID[0])
# for row in GRID:
#     print(row)
for r in range(ROWS):
    for c in range(COLS):
        if GRID[r][c] == "@":
            robot = Robot(r, c)
            break

for movement in movements:
    robot.move(movement, GRID)
    # print()
    # for row in GRID:
    #     print(row)

total = 0
for r in range(ROWS):
    for c in range(COLS):
        if GRID[r][c] == "O":
            total += 100 * r + c
print(total)
