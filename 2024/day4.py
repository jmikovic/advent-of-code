from collections import namedtuple


Direction = namedtuple('Direction', ['x', 'y'])

NEXT_LETTER ={
    'M': 'A',
    'A': 'S',
    'S': None,
}
DIRECTIONS = (
    Direction(-1, -1),
    Direction(-1, 0),
    Direction(-1, 1),
    Direction(1, -1),
    Direction(1, 0),
    Direction(1, 1),
    Direction(0, -1),
    Direction(0, 1),
)
CROSS_VALUES = {'M', 'S'}

table: list[str] = []


def lookup(x: int, y: int, direction: Direction, letter: str) -> bool:
    if (
        x * y < 0
        or x >= len(table[0])
        or y >= len(table)
    ):
        return False
    if table[y][x] == letter:
        return (
            lookup(x + direction.x, y + direction.y, direction, next_letter)
            if (next_letter := NEXT_LETTER[letter])
            else True
        )
    return False


def find_words(x: int, y: int) -> int:
    words = 0
    for direction in DIRECTIONS:
        if lookup(x + direction.x, y + direction.y, direction, 'M'):
            words += 1
    return words


def find_cross(x: int, y: int) -> int:
    if (
        x < 1
        or y < 1
        or x >= len(table[0]) - 1
        or y >= len(table) - 1
    ):
        return 0

    return 1 if (
        {table[y-1][x-1], table[y+1][x+1]} == {table[y-1][x+1], table[y+1][x-1]} == CROSS_VALUES
    ) else 0


if __name__ == '__main__':
    with open('2024/day4-input.txt', 'r') as f:
        table = [line.strip() for line in f.readlines()]

    count_words = 0
    count_crosses = 0
    for y, row in enumerate(table):
        for x, char in enumerate(row):
            if char == 'X':
                count_words += find_words(x, y)
            if char == 'A':
                count_crosses += find_cross(x, y)

    print(f'Part 1: {count_words}')
    print(f'Part 2: {count_crosses}')