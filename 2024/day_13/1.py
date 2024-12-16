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
import sympy as sp
import re

def get_solutions(x_a: int, y_a: int, x_b: int, y_b: int, x_target:int, y_target: int) -> tuple[int, int] | None:
    a_presses, b_presses = sp.symbols("a_presses b_presses")
    eq1 = sp.Eq(a_presses * x_a + b_presses * x_b, x_target)
    eq2 = sp.Eq(a_presses * y_a + b_presses * y_b, y_target)
    soln = sp.solve((eq1, eq2), (a_presses, b_presses))
    a_presses_ans, b_presses_ans = soln[a_presses], soln[b_presses]
    if not isinstance(a_presses_ans, sp.core.numbers.Integer) or not isinstance(b_presses_ans, sp.core.numbers.Integer):
        return None
    return int(a_presses_ans), int(b_presses_ans)


with open("input.txt", "r") as file:
    machines = file.read().strip().split("\n\n")

target = 0
for machine in machines:
    spec = machine.split("\n")
    pattern = r"\d+"
    x_a, y_a = map(int, re.findall(pattern, spec[0]))
    x_b, y_b = map(int, re.findall(pattern, spec[1]))
    x_target, y_target = map(int, re.findall(pattern, spec[2]))
    ans = get_solutions(x_a, y_a, x_b, y_b, x_target, y_target)
    if ans:
        a, b = ans
        target += a * 3 + b * 1
print(target)

