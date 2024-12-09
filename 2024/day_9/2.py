import heapq

with open("input.txt", "r") as f:
    input = f.read().strip()

files = {}
spaces = {i: [] for i in range(10)}
file_id = 0
pos = 0
for i, c in enumerate(input):
    x = int(c)
    if i % 2 == 0:
        files[file_id] = (pos, x)
        file_id += 1
    else:
        heapq.heappush(spaces[x], (pos, x))
    pos += x

def get_space(min_size: int, max_pos: int) -> tuple[int, int] | None:
    """
    gets the earliest space that can fit the file_id
      - initially made the mistake of preferencing the smaller spaces
        but we need ANY size large enough just the earliest one
    """
    global spaces
    candidates = [spaces[i][0] for i in range(min_size, 10) if (spaces[i] and spaces[i][0][0] < max_pos)]
    heapq.heapify(candidates)
    if not candidates: return None
    space = heapq.heappop(candidates)
    heapq.heappop(spaces[space[1]])
    return space

def insert_space(space: tuple[int, int]) -> None:
    global spaces
    heapq.heappush(spaces[space[1]], space)


for i in range(file_id - 1, -1, -1):
    fpos, fsize = files[i]
    space = get_space(fsize, fpos)
    if not space:
        continue
    # create a new space representing the file getting moved
    insert_space((fpos, fsize))
    spos, ssize = space
    diff = ssize - fsize
    # if remaining space need to reinsert a modified space
    if diff > 0:
        insert_space((spos + fsize, diff))
    files[i] = (spos, fsize)


total = 0
for fid, (pos, size) in files.items():
    for i in range(pos, pos + size):
        total += i * fid
print(total)

# # right answer: 6488291456470
