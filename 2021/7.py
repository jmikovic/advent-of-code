from os.path import join
from statistics import fmean, median
from typing import List


def load_inputs(path: str) -> List[int]:
    with open(path) as f:
        inputs = [int(x) for x in f.read().split(',')]
    
    return inputs


def part_one(inputs: List[int]) -> int:
    med = median(inputs)
    return sum([abs(med - i) for i in inputs])


def part_two(inputs: List[int]) -> int:
    avg = int(fmean(inputs))
    return sum([sum(range(abs(avg - i) + 1)) for i in inputs])


if __name__ == '__main__':
    inputs = load_inputs(join('inputs', '7.txt'))
    print(part_one(inputs))
    print(part_two(inputs))
