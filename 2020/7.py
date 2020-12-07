from os.path import join
from typing import List, Dict


def read_input(path: str) -> Dict[str, str]:
    with open(path) as f:
        lines = f.readlines()

    rules = dict(x.strip('.\n').split(' bags contain ') for x in lines)
    return rules


def get_colours(target: str, rules: Dict[str, str]) -> List[str]:
    colours = [k for k,v in rules.items() if target in v]
    additional = [get_colours(c, rules) for c in colours]

    additional = sum(additional, [])
    return colours + additional


def get_bags(target: str, rules: Dict[str, str]) -> int:
    count = 0
    rule = rules.get(target)
    if 'no other' in rule:
        return 0

    for bag in rule.split(', '):
        c, b = ' '.join(bag.split(' ')[:-1]).split(' ', 1)
        c = int(c)
        count += c + (c * get_bags(b, rules))

    return count


if __name__ == "__main__":
    input_values = read_input(join('inputs', '7.txt'))
    part_one = len(set(get_colours('shiny gold', input_values)))
    print(f'part one: {part_one}')

    part_two = get_bags('shiny gold', input_values)
    print(f'part two: {part_two}')
