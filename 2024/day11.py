from collections import defaultdict

def calculate_w_cache(numbers: list[int], iterations: int) -> int:
    def calculate_step(stone_map: dict[int, int]) -> dict[int, int]:
        new_map = defaultdict(int)
        for n, count in stone_map.items():
            if n == 0:
                new_map[1] += count
            elif not (len(str_n := str(n))) % 2:
                new_map[int(str_n[:len(str_n)//2])] += count
                new_map[int(str_n[len(str_n)//2:])] += count
            else:
                new_map[n * 2024] += count
        return new_map

    cache = {n: 1 for n in numbers}
    for _ in range(iterations):
        cache = calculate_step(cache)

    return sum(cache.values())

def calculate_stone(number: int, iterations: int) -> int:
    start = [number]
    for _ in range(iterations):
        new_list = []
        for n in start:
            if n == 0:
                new_list.append(1)
            elif not len(str_n := str(n)) % 2:
                new_list.append(int(str_n[:len(str_n)//2]))
                new_list.append(int(str_n[len(str_n)//2:]))
            else:
                new_list.append(n * 2024)

        start = new_list
    return len(start)


if __name__ == '__main__':
    start = [554735, 45401, 8434, 0, 188, 7487525, 77, 7]
    print(f'Part 1: {sum(calculate_stone(n, 25) for n in start)}')
    print(f'Part 2: {calculate_w_cache(start, 75)}')
