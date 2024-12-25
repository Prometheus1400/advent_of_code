inits, desc = open("input.txt", "r").read().split("\n\n")

vals: dict[str, bool] = {
    k: bool(int(v)) for line in inits.splitlines() for k, v in [line.split(": ")]
}
deps: dict[str, tuple[str, list[str]]] = {}

for line in desc.splitlines():
    dep1, op, dep2, _, cur = line.strip().split()
    deps[cur] = (op, [dep1, dep2])

"""
we can just iterate over all the nodes and do a memoized DFS
"""


def dfs(cur: str) -> bool:
    if cur in vals:
        return vals[cur]

    op, (dep1, dep2) = deps[cur]
    val = None
    match op:
        case "AND":
            val = dfs(dep1) and dfs(dep2)
        case "XOR":
            val = dfs(dep1) != dfs(dep2)
        case "OR":
            val = dfs(dep1) or dfs(dep2)

    assert val != None
    vals[cur] = val
    return val


z_wires = {}
for node in deps.keys():
    res = dfs(node)
    if node[0] == "z":
        z_wires[node] = res

res = 0
for k, v in z_wires.items():
    if not v:
        continue

    power = int(k[1:])
    res = res | (2**power)
print(res)
