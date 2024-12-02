import enum

class State(enum.Enum):
    NONE = 0
    INCREASING = 1
    DECREASING = 2

def valid_diff(x: int, y: int) -> bool:
    return 1 <= abs(x - y) <= 3

def get_new_state(prev: int, cur: int) -> State:
    if prev < cur:
        return State.DECREASING
    else:
        return State.INCREASING

def level_safe(level: list[int]) -> bool:
    current_state = State.NONE
    for i in range(1, len(level)):
        prev = level[i - 1]
        cur = level[i]
        if not valid_diff(prev, cur):
            return False

        if current_state == State.NONE:
            new_state = get_new_state(prev, cur)
            current_state = new_state
        else:
            if current_state != get_new_state(prev, cur):
                return False
    return True

    

num_safe_reports = 0
with open("input.txt", "r") as file:
    levels = file.readlines()
    for level in levels:
        level_list = level.strip().split()
        level_list = list(map(int, level_list))
        safe = False
        for i in range(len(level_list)):
            copy = level_list.copy()
            copy.pop(i)
            safe = safe or level_safe(copy)

        if safe:
            num_safe_reports += 1

print(num_safe_reports)


