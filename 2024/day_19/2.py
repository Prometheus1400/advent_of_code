
import re


patterns, designs = open("input.txt", "r").read().split("\n\n")
patterns = re.findall(r"\w+", patterns)
designs = designs.strip().splitlines()

def num_ways(design: str) -> int:
    """dp"""
    dp = [0] * (len(design) + 1)
    dp[-1] = 1
    for i in range(len(design) - 1, -1, -1):
        for pat in patterns:
            if ((i + len(pat) - 1) < len(design)) and (design[i: i + len(pat)] == pat):
                dp[i] += dp[i + len(pat)]
    return dp[0]

num_possible = 0
for design in designs:
    num_possible += num_ways(design)
print(num_possible)

