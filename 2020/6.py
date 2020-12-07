from os.path import join
from typing import List


def read_input(path: str) -> List[str]:
    with open(path) as f:
        values = f.read().split('\n\n')

    values = [x.replace('\n', ' ').strip() for x in values]
    return values


def part_one(values: List[str]) -> int:
    values = [x.replace(' ', '').strip() for x in values]
    return sum([len(set(q)) for q in values])


def part_two(values: List[str]) -> int:
    values = [x.split(' ') for x in values]
    sum = 0
    for v in values:
        for q in v[0]:
            if all([q in a for a in v]):
                sum += 1

    return sum


if __name__ == "__main__":
    input_values = read_input(join('inputs', '6.txt'))
    part_one = part_one(input_values)
    print(f'part one: {part_one}')

    part_two = part_two(input_values)
    print(f'part two: {part_two}')
