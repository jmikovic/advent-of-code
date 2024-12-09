def has_possible_combinations(
    target: int,
    current_result: int,
    numbers: list[int],
    with_concat: bool
) -> bool:
    if not numbers:
        return target == current_result

    if current_result > target:
        return False

    next_number = numbers[0]
    if has_possible_combinations(target, current_result + next_number, numbers[1:], with_concat):
        return True

    if has_possible_combinations(target, current_result * next_number, numbers[1:], with_concat):
        return True

    if with_concat:
        if has_possible_combinations(target, int(f'{current_result}{next_number}'), numbers[1:], with_concat):
            return True

    return False


if __name__ == '__main__':
    with open('2024/day7-input.txt', 'r') as f:
        lines = []
        for line in f.readlines():
            result, numbers = line.split(': ')
            numbers = [int(n) for n in numbers.split(' ')]
            lines.append((int(result), numbers))

    final_sum_part_1 = 0
    final_sum_part_2 = 0
    for result, numbers in lines:
        if has_possible_combinations(result, 0, numbers, False):
            final_sum_part_1 += result
            final_sum_part_2 += result
        elif has_possible_combinations(result, 0, numbers, True):
            final_sum_part_2 += result

print(f'2 Operators: {final_sum_part_1}')
print(f'3 Operators: {final_sum_part_2}')
