from os.path import join
from typing import List, Tuple, Callable


def read_input(path: str) -> List[List[str]]:
    with open(path) as f:
        values = [[y for y in x.strip()] for x in f.readlines()]

    return values


def check_adj(plan: List[List[str]], x: int, y: int) -> int:
    max_x = len(plan[0])
    max_y = len(plan)

    if y > 0 and x > 0:
        if y < max_y and x < max_x:
            new_plan = [p[x-1:x+2] for p in plan[y-1:y+2]]
        elif y < max_y:
            new_plan = [p[x-1:x+1] for p in plan[y-1:y+2]]
        else:
            new_plan = [p[x-1:x+2] for p in plan[y-1:y+1]]
        new_plan[1][1] = '.'
    elif y > 0:
        if y < max_y:
            new_plan = [p[x:x+2] for p in plan[y-1:y+2]]
        else:
            new_plan = [p[x:x+2] for p in plan[y-1:y+1]]
        new_plan[1][0] = '.'
    elif x > 0:
        if x < max_x:
            new_plan = [p[x-1:x+2] for p in plan[y:y+2]]
        else:
            new_plan = [p[x-1:x+1] for p in plan[y:y+2]]
        new_plan[0][1] = '.'
    else:
        new_plan = [p[x:x+2] for p in plan[y:y+2]]
        new_plan[0][0] = '.'

    return sum(new_plan, []).count('#')


def get_num_of_occupied(plan: List[List[str]], check_func: Callable[[List[List[str]], int, int], int], threshold:int)\
     -> int:
    changed = True
    occupied = 0
    max_y = len(plan)
    max_x = len(plan[0])

    while changed:
        changed = False
        new_plan = [[x for x in y] for y in plan]
        for y in range(max_y):
            for x in range(max_x):
                seat = plan[y][x]
                if seat == '.':
                    continue

                filled = check_func(plan, x, y)
                if seat == 'L' and not filled:
                    changed = True
                    new_plan[y][x] = '#'
                elif seat == '#' and filled >= threshold:
                    changed = True
                    new_plan[y][x] = 'L'

        plan = new_plan

    for y in range(max_y):
        for x in range(max_x):
            if plan[y][x] == '#':
                occupied += 1

    return occupied


if __name__ == "__main__":
    input_values = read_input(join('inputs', '11.txt'))
    part_one = get_num_of_occupied(input_values, check_adj, 4)
    print(f'part one: {part_one}')
