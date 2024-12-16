with open("input.txt", "r") as file:
    stones = list(map(int, file.read().strip().split(" ")))


def blink(input: list[int]) -> list[int]:
    output = []
    for num in input:
        strnum = str(num)
        if num == 0:
            output.append(1)
        elif len(strnum) % 2 == 0:
            output.append(int(strnum[:len(strnum)//2]))
            output.append(int(strnum[len(strnum)//2:]))
        else:
            output.append(num * 2024)
    return output

for _ in range(25):
    stones = blink(stones)

print(len(stones))
