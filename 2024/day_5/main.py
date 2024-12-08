from collections import defaultdict

with open("input.txt", "r") as file:
    lines = file.read()

rules, updates = lines.split("\n\n")
rules = rules.split("\n")
updates = updates.split("\n")
updates = [list(map(int, update.split(","))) for update in updates if update.strip()]

no_prev_mapping = defaultdict(list)
dep = defaultdict(list)
for rule in rules:
    pre, cur = rule.split("|")
    pre, cur = int(pre), int(cur)
    no_prev_mapping[pre].append(cur)
    dep[cur].append(pre)

def valid_order(arr: list[int]) -> bool:
    seen = set()
    for num in arr:
        # need to check if no invalid previous pages were here
        if num in no_prev_mapping:
            not_allowed_prevs = no_prev_mapping[num]
            for prev in not_allowed_prevs:
                if prev in seen:
                    return False
        seen.add(num)
    return True

print(rules)
def topological_sort(arr: list[int]) -> list[int]:
    pos = {n: i for i, n in enumerate(arr)}
    dep_copy = dep.copy()
    res = []
    def dfs(i):
        print(i)
        if arr[i] in res:
            return
        for d in dep_copy[arr[i]]:
            if d in pos:
                dfs(pos[d])
        dep_copy[arr[i]] = []
        res.append(arr[i])

    for i in range(len(arr)):
        dfs(i)

    return res

def get_middle(arr: list[int]) -> int:
    if len(arr) % 2 == 0:
        print("invalid even len update")
        return 0

    return arr[len(arr) // 2]

total = 0
for update in updates:
    if not valid_order(update):
        topo = topological_sort(update)
        print(update, "->", topo)
        total += get_middle(topo)

print(total)
