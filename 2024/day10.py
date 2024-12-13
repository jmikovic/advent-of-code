from collections import namedtuple


Direction = namedtuple('Direction', ['x', 'y'])

DIRECTIONS = (
    Direction(-1, 0),
    Direction(1, 0),
    Direction(0, -1),
    Direction(0, 1),
)

topomap: list[list[int]] = []


def get_trail_score(x: int, y: int) -> int:
    ends = []

    def lookup(x: int, y: int, value: int) -> None:
        if (
            x * y < 0
            or x >= len(topomap[0])
            or y >= len(topomap)
        ):
            return

        if topomap[y][x] == value:
            if value == 9:
                ends.append((x, y))
            else:
                for direction in DIRECTIONS:
                    lookup(x + direction.x, y + direction.y, value + 1)

    for direction in DIRECTIONS:
        lookup(x + direction.x, y + direction.y, 1)

    return len(set(ends)), len(ends)


if __name__ == '__main__':
    with open('2024/day10-input.txt', 'r') as f:
        topomap = [[int(p) for p in line.strip()] for line in f.readlines()]

    final_score = 0
    final_rating = 0
    for y, row in enumerate(topomap):
        for x, value in enumerate(row):
            if value == 0:  # start of the trail
                score, rating = get_trail_score(x, y)
                final_score += score
                final_rating += rating

    print(f'Sum of scores: {final_score}')
    print(f'Sum of ratings: {final_rating}')
