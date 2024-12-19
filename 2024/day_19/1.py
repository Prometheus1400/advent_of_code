import re


patterns, designs = open("input.txt", "r").read().split("\n\n")
patterns = re.findall(r"\w+", patterns)
designs = designs.strip().splitlines()

def possible(design: str) -> bool:
    """dp"""
    dp = [False] * (len(design) + 1)
    dp[-1] = True
    for i in range(len(design) - 1, -1, -1):
        for pat in patterns:
            if ((i + len(pat) - 1) < len(design)) and (design[i: i + len(pat)] == pat):
                dp[i] = dp[i] or dp[i + len(pat)]
    return dp[0]

num_possible = 0
for design in designs:
    if possible(design):
        num_possible += 1
print(num_possible)

