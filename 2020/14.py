from os.path import join
from re import match
from typing import List, Tuple


def read_input(path: str) -> List[str]:
    with open(path) as f:
        full_input = f.readlines()

    return full_input


def part_one(program: List[str]) -> int:
    memory = {}
    mask = ''
    for i in program:
        if i.startswith('mask'):
            mask = i.split(' = ')[1].strip()
        else:
            mem, num = match(r'\w+\[([0-9]+)\]\s=\s([0-9]+)', i).groups()
            num = int(num)
            bin_num = [n for n in f'{num:036b}']
            for e, x in enumerate(mask):
                if x != 'X':
                    bin_num[e] = x
            memory[mem] = int(''.join(bin_num), 2)

    return sum(memory.values())


if __name__ == "__main__":
    program = read_input(join('inputs', '14.txt'))
    part_one = part_one(program)
    print(f'part one: {part_one}')

