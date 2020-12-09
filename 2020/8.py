from copy import deepcopy
from os.path import join
from typing import List, Tuple


def read_input(path: str) -> List[str]:
    with open(path) as f:
        values = [v.strip() for v in f.readlines()]

    return values


def process_instructions(instructions: List[str]) -> Tuple[bool, int]:
    i = 0
    acc = 0
    processed = []

    while i < len(instructions):
        if i in processed:
            return False, acc

        processed.append(i)
        op, val = instructions[i].split(' ')
        if op == 'acc':
            acc += int(val)
            i += 1
        elif op == 'jmp':
            i += int(val)
        else:
            i += 1

    return True, acc


def find_finite(instructions: List[str]) -> int:
    def switch(op: str, val: str):
        return f'jmp {val}' if op == 'nop' else f'nop {val}'

    options = [i for i, o in enumerate(instructions) if o != 'acc']
    for o in options:
        new_instr = deepcopy(instructions)
        new_instr[o] = switch(*new_instr[o].split(' '))
        finite, acc = process_instructions(new_instr)
        if finite:
            return acc
    return 0


if __name__ == "__main__":
    input_values = read_input(join('inputs', '8.txt'))
    _, part_one = process_instructions(input_values)
    print(f'part_one: {part_one}')

    part_two = find_finite(input_values)
    print(f'part two: {part_two}')
