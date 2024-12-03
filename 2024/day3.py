import re

with open('2024/day3-input.txt', 'r') as f:
    memory = f.read()

pattern = re.compile('mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)')
multiplications = pattern.findall(memory)
print(f'Sum of all multiplications: {sum(int(a) * int(b) for a, b in multiplications)}')

groups = memory.split("don't()")
filtered_memory = groups[0] + ''.join(''.join(group.split('do()')[1:]) for group in groups[1:])
multiplications = pattern.findall(filtered_memory)
print(f'Sum of filtered multiplications: {sum(int(a) * int(b) for a, b in multiplications)}')
