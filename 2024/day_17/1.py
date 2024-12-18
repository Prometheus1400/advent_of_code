import re


registers, program = open("input.txt", "r").read().split("\n\n")
a, b, c = map(int, re.findall(r"\d+", registers))
ip_table = {i: int(n) for i, n in enumerate(re.findall(r"\d", program))}

def execute(a:int, b:int, c:int):
    ip = 0
    stdout = []
    while ip <= max(ip_table.keys()):
        combo = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}
        opcode, operand = ip_table[ip], ip_table[ip + 1]
        match opcode:
            case 0: a = a // 2 ** combo[operand]
            case 1: b = b ^ operand
            case 2: b = combo[operand] % 8
            case 3: ip = operand - 2 if a else ip
            case 4: b = b ^ c
            case 5: stdout.append(combo[operand] % 8) 
            case 6: b = a // 2 ** combo[operand]
            case 7: c = a // 2 ** combo[operand]
        ip += 2
    return stdout

print(",".join(map(str, execute(a,b,c))))
