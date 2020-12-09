from os.path import join
from typing import List


def read_input(path: str) -> List[int]:
    with open(path) as f:
        return [int(x.strip()) for x in f.readlines()]


def part_one(entries: List[int]) -> int:
    for e in entries:
        rem = 2020 - e
        if rem in entries:
            return e * rem
    return 0


def part_two(entries: List[int]) -> int:
    for i, e in enumerate(entries):
        for v in entries[i+1:]:
            rem = 2020 - e - v
            if rem in entries:
                return rem * e * v
    return 0


if __name__ == "__main__":
    input_values = read_input(join('inputs', '1.txt'))
    print(part_one(input_values))
    print(part_two(input_values))
