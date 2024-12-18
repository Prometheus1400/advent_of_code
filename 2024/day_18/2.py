import re
from collections import deque

nums = list(map(int, re.findall(r"\d+", open("input.txt", "r").read())))
bts = list(zip(nums[::2], nums[1::2]))

grid_size = 70
target = (grid_size, grid_size)
start = (0, 0)
blacklist = set()
for i in range(1024): blacklist.add(bts[i])

def bfs(start: tuple[int, int], end: tuple[int, int]) -> int | None:
    visited = {start}
    q = deque([(0, start)])
    while q:
        cost, cur = q.popleft()
        if cur == end:
            return cost
        r, c = cur
        for delta_r, delta_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r + delta_r, c + delta_c
            if (
                0 <= (new_r) <= grid_size
                and 0 <= (new_c) <= grid_size
                and (new_r, new_c) not in blacklist
                and (new_r, new_c) not in visited
            ):
                visited.add((new_r, new_c))
                q.append((cost + 1, (new_r, new_c)))


# binary search looking for the change point
l, r = 0, len(bts) - 1
while l < r:
    blacklist.clear()
    m = (l + r) // 2
    for i in range(m + 1):
        blacklist.add(bts[i])
    res = bfs(start, target)
    if res:
        l = m + 1
    else:
        r = m - 1
print(bts[l])
