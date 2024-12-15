import re


def simulate(
    start: tuple[int, int], vel: tuple[int, int], width: int, height: int, seconds: int
) -> tuple[int, int]:

    x, y = start
    vx, vy = vel
    for _ in range(seconds):
        x, y = (x + vx) % width, (y + vy) % height
    return (x, y)


def no_overlaps(robot_pos: list[tuple[int, int]]) -> bool:
    """returns true if no overlaps"""
    return len(set(robot_pos)) == len(robot_pos)


WIDTH, HEIGHT = 101, 103
input = []
with open("input.txt", "r") as file:
    for line in file:
        x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
        input.append((x, y, vx, vy))

for seconds in range(1, 1000000):
    for i, (x, y, vx, vy) in enumerate(input):
        new_x, new_y = simulate((x, y), (vx, vy), WIDTH, HEIGHT, 1)
        input[i] = (new_x, new_y, vx, vy)

    if not no_overlaps([(x, y) for x, y, *_ in input]):
        continue
    print(seconds)
