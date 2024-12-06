from copy import deepcopy

NEXT_SHAPE: dict[str, tuple[str, int, int]] = {
    '^': ('>', 1, 0),
    '>': ('v', 0, 1),
    'v': ('<', -1, 0),
    '<': ('^', 0, -1),
}

def find_starting_position(area: list[str]) -> tuple[int, int]:
    for y, row in enumerate(area):
        for x, field in enumerate(row):
            if field == '^':
                return x, y


def part_1(area: list[str], x: int, y: int) -> int:
    visited_positions = []
    guard = '^'
    x_mov = 0
    y_mov = -1
    while True:
        if area[y][x] != 'X':
            visited_positions.append((x, y))
        try:
            if area[y + y_mov][x + x_mov] == '#':
                guard, x_mov, y_mov = NEXT_SHAPE[guard]
        except IndexError:
            return visited_positions
        area[y][x] = 'X'
        x, y = x + x_mov, y + y_mov


def forms_loop(new_area: list[str | int], x: int, y: int) -> int:
    def next_step(_guard: str, _x_mov: int, _y_mov: int, turned: bool = False) -> tuple[str, int, int, bool, bool]:
        if new_area[y + _y_mov][x + _x_mov] == '#':
            if new_area[y][x]:
                return _guard, _x_mov, _y_mov, True, True
            _guard, _x_mov, _y_mov, _, turned = next_step(*NEXT_SHAPE[_guard], True)

        return _guard, _x_mov, _y_mov, False, turned

    guard = '^'
    x_mov = 0
    y_mov = -1
    while True:
        if new_area[y][x] in ['.', '^']:
            new_area[y][x] = 0
        try:
            guard, x_mov, y_mov, loop, turned = next_step(guard, x_mov, y_mov)
            if loop:
                return 1
            if ((x + x_mov) * (y + y_mov)) < 0:
                return 0
        except IndexError:
            return 0
        if turned:
            new_area[y][x] = new_area[y][x] + 1
        x, y = x + x_mov, y + y_mov


def part_2(positions: list[tuple[int, int]], area: list[str], x: int, y: int) -> int:
    loops = 0
    for _x, _y in positions:
        area_copy = deepcopy(area)
        area_copy[_y][_x] = '#'
        loops += forms_loop(area_copy, x, y)

    return loops


if __name__ == '__main__':
    with open('2024/day6-input.txt', 'r') as f:
        area = [[x for x in line.strip()] for line in f.readlines()]
        x, y = find_starting_position(area)
        visited_positions = part_1(deepcopy(area), x, y)
        print(f'Visited positions: {len(visited_positions)}')
        print(f'Positions for obstruction: {part_2(visited_positions[1:], area, x, y)}')  # excluding starting position
