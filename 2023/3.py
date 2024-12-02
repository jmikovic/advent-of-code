with open('../adjust/input.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

result = 0


def check_surroundings(x: int, y: int, start: int) -> bool:
    for ly in range(max(0, y-1), min(y + 2, 140)):
        for lx in range(max(0, start-1), min(x + 1, 140)):
            lchar = lines[ly][lx]
            if not lchar.isdigit() and lchar != '.':
                return True
    return False


start = None
for y, line in enumerate(lines):
    if start:
        if check_surroundings(139, y - 1, start):
            result += int(lines[y-1][start:])
        start = None
    for x, char in enumerate(line):
        if char.isdigit() and start is None:
            start = x
        elif not char.isdigit() and start is not None:
            if check_surroundings(x, y, start):
                result += int(line[start:x])
            start = None

print(result)
