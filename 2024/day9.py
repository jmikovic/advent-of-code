def part_1(disk: list[int]) -> int:
    checksum = 0
    index = 0
    queue = []
    for i, number in enumerate(disk):
        if not i % 2:  # even index -> file
            for _ in range(number):
                checksum += ((i // 2) * index)
                index += 1
        else:  # odd index -> free space
            while len(queue) < number:
                last_file_id = (len(disk) - 1) // 2
                last_file = disk.pop()
                queue += [last_file_id] * last_file
                disk.pop()  # remove empty space from the end
            for _ in range(number):
                checksum += (queue.pop(0) * index)
                index += 1
    for n in queue:  # add leftover file blocks at the end
        checksum += n * index
        index += 1
    return checksum


if __name__ == '__main__':
    with open('2024/day9-input.txt', 'r') as f:
        disk = [int(n) for n in f.read().strip()]

    print(f'Checksum: {part_1(disk)}')
