import re


def simulate(
    start: tuple[int, int], vel: tuple[int, int], width: int, height: int, seconds: int
) -> tuple[int, int]:

    x, y = start
    vx, vy = vel
    for _ in range(seconds):
        x, y = (x + vx) % width, (y + vy) % height
    return (x, y)


robot_pos_final = []
WIDTH, HEIGHT = 101, 103
SECONDS = 100
with open("input.txt", "r") as file:
    for line in file:
        x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
        robot_pos_final.append(simulate((x, y), (vx, vy), WIDTH, HEIGHT, SECONDS))

quadrants = {x: 0 for x in range(4)}
for robot_pos in robot_pos_final:
    x, y = robot_pos
    x_mid, y_mid = WIDTH // 2, HEIGHT // 2
    if x < x_mid and y < y_mid:
        quadrants[0] += 1
    if x < x_mid and y > y_mid:
        quadrants[2] += 1
    if x > x_mid and y < y_mid:
        quadrants[1] += 1
    if x > x_mid and y > y_mid:
        quadrants[3] += 1

sf = 1
for num_robots in quadrants.values():
    sf *= num_robots
print(sf)
    
