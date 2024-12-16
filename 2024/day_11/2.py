import time

start = time.time()

with open("input.txt", "r") as file:
    stones = list(map(int, file.read().strip().split(" ")))

cache = {}
def num_stones_from_cur(stone: int, blinks: int) -> int:
    if blinks <= 0:
        return 1 
    if (stone, blinks) in cache:
        return cache[(stone, blinks)]

    strstone = str(stone)
    res = None
    if stone == 0:
        res = num_stones_from_cur(1, blinks - 1)
    elif len(strstone) % 2 == 0:
        res = num_stones_from_cur(int(strstone[:len(strstone) // 2]), blinks - 1) + num_stones_from_cur(int(strstone[len(strstone) // 2:]), blinks - 1)
    else:
        res = num_stones_from_cur(stone * 2024, blinks - 1)

    cache[(stone, blinks)] = res
    return res
        

num_stones = 0
for stone in stones:
    num_stones += num_stones_from_cur(stone, 75)

end = time.time()
print(num_stones)
print(f"took {end - start} s")
