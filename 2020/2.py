from os.path import join
from typing import List, Tuple


def read_input(path: str) -> List[Tuple[int, int, str, str]]:
    with open(path) as f:
        entries = f.readlines()
        inputs = []
        for e in entries:
            rule, psswd = e.split(': ')
            apps, target = rule.split(' ')
            low, high = [int(x) for x in apps.split('-')]
            inputs.append((low, high, target, psswd))

        return inputs


def part_one(entries: List[Tuple[int, int, str, str]]) -> int:
    valid = list(filter(lambda x: x[0] <= x[3].count(x[2]) <= x[1], entries))
    return len(valid)


def part_two(entries: List[Tuple[int, int, str, str]]) -> int:
    def validate(rule: Tuple[int, int, str], value: str) -> bool:
        f = rule[0] - 1
        s = rule[1] - 1
        t = rule[2]

        valid = (value[f] == t and value[s] != t) or (value[f] != t and value[s] == t)
        return valid

    valid = list(filter(lambda x: validate(x[:3], x[3]), entries))
    return len(valid)


if __name__ == "__main__":
    input_values = read_input(join('inputs', '2.txt'))
    print(part_one(input_values))
    print(part_two(input_values))
