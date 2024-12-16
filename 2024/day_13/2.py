"""
example:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

create a system of equations like:
    a_presses * 94 + b_presses * 22 = 8400
    a_presses * 34 + b_presses * 67 = 5400

solve for a_presses and b_presses (if solutions exist)
iterate over possible solutions to find the cheapest one
"""

import re

import sympy as sp
from sympy.core.numbers import Integer


def get_solutions(
    x_a: int, y_a: int, x_b: int, y_b: int, x_target: int, y_target: int
) -> tuple[int, int]:
    a, b = sp.symbols("a b")
    soln = sp.solve(
        (sp.Eq(a * x_a + b * x_b, x_target), sp.Eq(a * y_a + b * y_b, y_target)), (a, b)
    )
    a_ans, b_ans = soln[a], soln[b]
    if not isinstance(a_ans, Integer) or not isinstance(b_ans, Integer):
        return 0, 0
    return int(a_ans), int(b_ans)


with open("input.txt", "r") as file:
    machines = file.read().strip().split("\n\n")

target = 0
for machine in machines:
    spec = machine.split("\n")
    pattern = r"\d+"
    x_a, y_a = map(int, re.findall(pattern, spec[0]))
    x_b, y_b = map(int, re.findall(pattern, spec[1]))
    x_target, y_target = map(
        lambda x: int(x) + 10000000000000, re.findall(pattern, spec[2])
    )
    a, b = get_solutions(x_a, y_a, x_b, y_b, x_target, y_target)
    target += a * 3 + b * 1
print(target)
