from os.path import join
from typing import List


def get_ids(passes: List[str]) -> List[int]:
    ids = []
    for p in passes:
        rows = list(range(128))
        columns = list(range(8))

        for x in p[:7]:
            divider = int(len(rows)/2)
            rows = rows[divider:] if x == 'B' else rows[:divider]

        for x in p[7:]:
            divider = int(len(columns)/2)
            columns = columns[divider:] if x == 'R' else columns[:divider]

        ids.append(rows[0] * 8 + columns[0])

    return ids


def read_input(path: str) -> List[int]:
    with open(path) as f:
        values = [v.strip() for v in f.readlines()]

    return get_ids(values)


if __name__ == "__main__":
    ids = read_input(join('inputs', '5.txt'))
    max_id = max(ids)
    my_id = list(filter(lambda x: x not in ids and x+1 in ids and x-1 in ids, range(max(ids))))[0]
    print(f'part one: {max_id}')
    print(f'part two: {my_id}')
