from collections import defaultdict

adj = defaultdict(set)
for n1, n2 in [
    line.strip().split("-")
    for line in open("input.txt", "r").readlines()
]:
    adj[n1].add(n2)
    adj[n2].add(n1)

"""
for each pair of nodes we can find the intersection of their
adjacency lists which will give us the 3rd node in the inter-
connected component

handle duplicates by ensuring a specific order of nodes
pretty sure it could be optimized by modifying adj
to actually eliminate the repeated work
"""

def valid(triple: tuple[str, str, str]) -> bool:
    for n in triple:
        if n[0] == "t":
            return True
    return False

interconnected = set()
for n1, neighs in adj.items():
    for n2 in neighs:
        if n2 < n1: continue
        for n3 in adj[n1].intersection(adj[n2]):
            if n3 < n2: continue
            interconnected.add((n1, n2, n3))

total = 0
for triple in interconnected:
    if valid(triple):
        total += 1
print(total)
