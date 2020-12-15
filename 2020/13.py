from math import ceil
from os.path import join
from typing import List, Tuple


def read_input(path: str) -> Tuple[int, List[int]]:
    with open(path) as f:
        values = [l.strip() for l in f.readlines()]

    timestamp = int(values[0])
    buses = values[1].split(',')
    return timestamp, buses


def get_first_bus(time: int, buses: List[int]) -> Tuple[int, int]:
    departures = {}
    for b in buses:
        departures[b] = b * ceil(time / b)

    first_bus = min(departures, key=departures.get)
    wait = departures[first_bus] - time
    return first_bus, wait


def get_earliest_subsequent(buses: List[str]) -> int:
    i = 1
    timestamp = int(buses[0])
    offsets = {}
    for e, b in enumerate(buses):
        if b == 'x':
            continue
        offsets[int(b)] = e

    for b, o in offsets.items():
        while (timestamp + o) % b:
            timestamp += i
        i *= b

    return timestamp


if __name__ == "__main__":
    timestamp, buses = read_input(join('inputs', '13.txt'))
    first, wait = get_first_bus(timestamp, [int(b) for b in buses if b != 'x'])
    part_one = first * wait
    print(f'part one: {part_one}')

    part_two = get_earliest_subsequent(buses)
    print(f'part two: {part_two}')
