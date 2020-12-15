from copy import deepcopy
from typing import Dict


def get_nth(start: Dict[int, int], n:int, current: int) -> int:
    values = deepcopy(start)
    for i in range(7, n):
        idx = values.get(current)
        values[current] = i
        if idx:
            current = i - idx
        else:
            current = 0

    return current


if __name__ == "__main__":
    input_values = {0: 1, 13: 2, 1: 3, 8: 4, 6: 5, 15: 6}
    part_one = get_nth(input_values, 2020, 0)
    print(f'part one: {part_one}')

    part_two = get_nth(input_values, 30000000, 0)
    print(f'pat two: {part_two}')
