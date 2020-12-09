from os.path import join
from typing import List, Tuple


def read_input(path: str) -> Tuple[List[str], int]:
    with open(path) as f:
        values = f.readlines()
        length = len(values[0])

    return values, length


def calculate(rows: List[str], max_idx: int, right: int, down:int) -> int:
    trees = 0
    idx = right
    for r in rows[down::down]:
        if r[idx] == '#':
            trees += 1
        idx = (idx + right) % max_idx
    return trees


def part_two(rows: List[str], max_idx: int) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for r,d in slopes:
        result *= calculate(rows, max_idx, r, d)

    return result


if __name__ == "__main__":
    input_values, length = read_input(join('inputs', '3.txt'))
    part_one = calculate(input_values, length-1, 3, 1)
    print(f'part one: {part_one}')
    part_two = part_two(input_values, length-1)
    print(f'part two: {part_two}')
