from os.path import join
from typing import List, Tuple


def read_input(path: str) -> List[int]:
    with open(path) as f:
        values = [int(x) for x in f.readlines()]

    return values


def check_valid(numbers: [int], target: int) -> bool:
    for n in numbers:
        rem = target - n
        if n == rem:
            continue
        try:
            numbers.index(rem)
        except ValueError:
            continue

        return True
    return False


def get_first_invalid(values: List[int]) -> int:
    for i, v in enumerate(values[25:]):
        valid = check_valid(values[i:i+25], v)
        if not valid:
            return v

    return 0


def get_weakness(numbers: List[int], target: int) -> int:
    for i, n in enumerate(numbers):
        total_set = [n]
        for n2 in numbers[i+1:]:
            total_set.append(n2)
            total = sum(total_set)
            if total > target:
                break
            if total == target:
                return min(total_set) + max(total_set)
    return 0


if __name__ == "__main__":
    input_values = read_input(join('inputs', '9.txt'))
    invalid_number = get_first_invalid(input_values)
    print(f'part one: {invalid_number}')

    part_two = get_weakness(input_values, invalid_number)
    print(f'part two: {part_two}')
