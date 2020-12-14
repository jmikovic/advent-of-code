from os.path import join
from typing import List, Dict


directions = ['N', 'E', 'S', 'W']


def read_input(path: str) -> List[str]:
    with open(path) as f:
        values = f.readlines()

    return values


def move(position: Dict[str, int], d: str, distance: int) -> Dict[str, int]:
    if d == 'N':
        position['y'] += distance
    elif d == 'S':
        position['y'] -= distance
    elif d == 'W':
        position['x'] -= distance
    else:
        position['x'] += distance

    return position


def change_direction(current: str, new: str, angle: int) -> str:
    angle = angle / 90
    current_direction = directions.index(current)
    if new == 'R':
        direction = int((current_direction + angle) % 4)
    else:
        direction = int((current_direction - angle) % 4)

    return directions[direction]


def rotate(current: Dict[str, int], way: str, angle: int) -> Dict[str, int]:
    angle = int(angle / 90)
    if way == 'L':
        angle = int(-angle % 4)

    x = current['x']
    y = current['y']

    for _ in range(angle):
        x, y = y, -x

    return {'x': x, 'y': y}


def part_one(instructions: List[str]) -> int:
    direction = 'E'
    position = {'x': 0, 'y': 0}

    for i in instructions:
        d = i[0]
        distance = int(i[1:])
        if d in directions:
            position = move(position, d, distance)
        elif d == 'F':
            position = move(position, direction, distance)
        else:
            direction = change_direction(direction, d, distance)

    return abs(position['x']) + abs(position['y'])


def part_two(instructions: List[str]) -> int:
    ship_position = {'x': 0, 'y': 0}
    waypoint_position = {'x': 10, 'y': 1}

    for i in instructions:
        d = i[0]
        distance = int(i[1:])
        if d in directions:
            waypoint_position = move(waypoint_position, d, distance)
        elif d == 'F':
            ship_position['x'] += (waypoint_position['x'] * distance)
            ship_position['y'] += (waypoint_position['y'] * distance)
        else:
            waypoint_position = rotate(waypoint_position, d, distance)

    return abs(ship_position['x']) + abs(ship_position['y'])


if __name__ == "__main__":
    input_values = read_input(join('inputs', '12.txt'))
    part_one = part_one(input_values)
    print(f'part one: {part_one}')

    part_two = part_two(input_values)
    print(f'part two: {part_two}')
