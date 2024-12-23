from collections import defaultdict

adj = defaultdict(set)
for n1, n2 in [
    line.strip().split("-")
    for line in open("input.txt", "r").readlines()
]:
    adj[n1].add(n2)
    adj[n2].add(n1)

"""
build up the clique using dfs and ensuring the dense connection by
making sure every node we've seen so far is also in the adj for
current node
"""
largest_set = set()
def dfs(cur: str, cur_component: set[str]):
    global largest_set
    if not cur_component.issubset(adj[cur]):
        return
    # this is good means we can keep looking for more nodes
    cur_component.add(cur)
    if len(cur_component) > len(largest_set):
        largest_set = cur_component.copy()
    for n in adj[cur]:
        if n not in cur_component:
            dfs(n, cur_component)

for n in adj.keys():
    dfs(n, set())

print(','.join(sorted(largest_set)))
