import re
"""
program: 2,4, 1,3, 7,5, 0,3, 4,1, 1,5, 5,5, 3,0

decompiled:
    1: b <- a mod 8
    2: b <- b xor 3
    3: c <- a bitshift right b times
    4: a <- a bitshift right 3 times
    5: b <- b xor c
    6: b <- b xor 5
    7: print b mod 8
    8: if a != 0 goto 1

observations:
    - b and c are functions of a which means the output is entirely a function of a
    - lowest value is a multiple of 8 + i where i in [0 - 7] meaning we can potentially
      decrease problem space by only checking 8x + offset instead of every value
        * how to find the offset though?

    - at step 2 b is AT MOST 7 (111) and AT LEAST 0
    - a then gets bitshifted 3 times meaning it loses bottom 3 bits
"""

registers, program = open("input.txt", "r").read().split("\n\n")
a, b, c = map(int, re.findall(r"\d+", registers))
ip_table = {i: int(n) for i, n in enumerate(re.findall(r"\d", program))}
target = list(map(int, re.findall(r"\d", program)))

def execute(a:int, b:int, c:int, ip_table: dict[int, int]) -> list[int]:
    ip = 0
    stdout = []
    while ip <= max(ip_table.keys()):
        combo = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}
        opcode, operand = ip_table[ip], ip_table[ip + 1]
        match opcode:
            case 0: a = a >> combo[operand]
            case 1: b = b ^ operand
            case 2: b = combo[operand] % 8
            case 3: ip = operand - 2 if a else ip
            case 4: b = b ^ c
            case 5: stdout.append(combo[operand] % 8) 
            case 6: b = a >> combo[operand]
            case 7: c = a >> combo[operand]
        ip += 2
    return stdout

def solve(a: int, i: int):
    if i < 0:
        return
    for d in range(8):
        new_a = (a << 3) | d
        res = execute(new_a, 0, 0, ip_table)
        if res == target[i:]:
            if i == 0:
                print(new_a)
                exit(0)
            else:
                solve(new_a, i - 1)
    
solve(0, len(target) - 1)
