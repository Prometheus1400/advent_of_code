#TODO: fix this
from collections import deque
from dataclasses import dataclass, field
import heapq


@dataclass
class DirectedPoint:
    score: float
    r: int
    c: int
    dir: "str"

    def get_tuple(self) -> tuple[int, int]:
        return (self.r, self.c)

    def turn_cost(self, new_dir: str) -> float:
        if new_dir == self.dir:
            return 0
        if (
            new_dir == "NORTH"
            and self.dir == "SOUTH"
            or new_dir == "EAST"
            and self.dir == "WEST"
            or new_dir == "SOUTH"
            and self.dir == "NORTH"
            or new_dir == "WEST"
            and self.dir == "EAST"
        ):
            return float("inf")
        return 1000

    def __lt__(self, other: "DirectedPoint") -> bool:
        return (self.score, self.r, self.c) < (other.score, other.r, other.c)

@dataclass
class State:
    mincost_seen: float = float("inf")
    prev: list[tuple[int, int]] = field(default_factory=list)

def backtrack(node_states: dict[tuple[int,int], State], end_pos: tuple[int, int]) -> int:
    seen = set()
    q = deque([end_pos])
    while q:
        pos = q.popleft()
        seen.add(pos)
        q.extend(node_states[pos].prev)
    return len(seen)


def djikstras(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> tuple[float, int]:
    node_states = {(r, c): State() for c in range(len(grid[0])) for r in range(len(grid))} 
    deltas = {"NORTH": (-1, 0), "EAST": (0, 1), "SOUTH": (1, 0), "WEST": (0, -1)}
    pq = [DirectedPoint(0, *start, "EAST")]
    while pq:
        cur = heapq.heappop(pq)
        print(pq)
        score, r, c, _ = cur.score, cur.r, cur.c, cur.dir
        for new_dir, (delta_r, delta_c) in deltas.items():
            new_pos = (r + delta_r, c + delta_c)
            new_score = score + cur.turn_cost(new_dir) + 1
            state = node_states[new_pos]
            if grid[new_pos[0]][new_pos[1]] == "#" or new_score > state.mincost_seen or new_score == float("inf"):
                continue
            if new_score < state.mincost_seen:
                state.mincost_seen = new_score
                state.prev = [cur.get_tuple()]
            elif new_score == state.mincost_seen:
                state.prev.append(cur.get_tuple())
            heapq.heappush(pq, DirectedPoint(new_score, *new_pos, new_dir))
    
    for k, v in node_states.items():
        if v.mincost_seen != float("inf") and k == (7, 5): print(k, v)
    node_states[end].prev = []
    return (node_states[end].mincost_seen, backtrack(node_states, end))


GRID = [[c for c in line] for line in open("sample.txt", "r")]
start = [(r, c) for c in range(len(GRID[0])) for r in range(len(GRID)) if GRID[r][c] == "S"][0]
end = [(r, c) for c in range(len(GRID[0])) for r in range(len(GRID)) if GRID[r][c] == "E"][0]
print(djikstras(GRID, start, end))
