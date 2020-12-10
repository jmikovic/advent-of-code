from math import prod
from os.path import join
from typing import List


def read_input(path: str) -> List[int]:
    with open(path) as f:
        values = [int(x) for x in f.readlines()]

    values.sort()
    return values


def get_differences(adapters: List[int]) -> int:
    diff_3 = 1
    diff_1 = 1

    for i, a in enumerate(adapters[1:]):
        if a - adapters[i] == 1:
            diff_1 += 1
        elif a - adapters[i] == 3:
            diff_3 += 1

    return diff_1 * diff_3


def f(x: int) -> int:
    if x < 3:
        return 1
    elif x == 3:
        return 2
    return f(x-1) + f(x-2) + f(x-3)


def get_groups(adapters: List[int]) -> List[int]:
    groups = []
    count = 1
    prev = adapters[0]
    for a in adapters[1:]:
        if a - prev == 1:
            count += 1
        else:
            groups.append(count)
            count = 1
        prev = a

    groups.append(count)
    return groups


if __name__ == "__main__":
    input_values = read_input(join('inputs', '10.txt'))
    part_one = get_differences(input_values)
    print(f'part one: {part_one}')

    part_two = prod(list(map(f, get_groups([0] + input_values))))
    print(f'part two: {part_two}')
