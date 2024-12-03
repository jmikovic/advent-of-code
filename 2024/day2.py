def check_increase(first: int, second: int) -> bool:
    return first < second and abs(first - second) <= 3


def check_decrease(first: int, second: int) -> bool:
    return second < first and abs(first - second) <= 3


def check_report(report: list[int]) -> int:
    first_number: int = report[0]
    prev_number: int = report[1]
    if abs(prev_number - first_number) > 3 or prev_number == first_number:
        return 0
    direction: str = 'dec' if first_number > prev_number else 'inc'
    for num in report[2:]:
        if direction == 'dec' and not check_decrease(prev_number, num):
            break
        elif direction == 'inc' and not check_increase(prev_number, num):
            break
        prev_number = num
    else:
        return 1
    return 0


def part_1(reports: list[list[int]]) -> int:
    safe_count: int = 0
    for report in reports:
        safe_count += check_report(report)
    return safe_count


def part_2(reports:list[list[int]]) -> int:
    safe_count: int = 0
    for report in reports:
        if check_report(report[1:]) or check_report([report[0], *report[2:]]):
            safe_count += 1
            continue
        already_skipped: bool = False
        first_number: int = report[0]
        prev_number: int = report[1]
        direction: str = 'dec' if first_number > prev_number else 'inc'
        if (
            abs(prev_number - first_number) > 3
            or prev_number == first_number
        ):
            if check_decrease(first_number, report[2]):
                direction = 'dec'
                prev_number = first_number
                already_skipped = True
            elif check_increase(first_number, report[2]):
                direction == 'inc'
                prev_number = first_number
                already_skipped = True
            else:
                continue
        for i, num in enumerate(report[2:], 2):
            if direction == 'dec' and not check_decrease(prev_number, num):
                if already_skipped:
                    break
                if (
                    i + 1 == len(report)
                    or (i + 1 < len(report) and check_decrease(prev_number, report[i + 1]))
                ):
                    already_skipped = True
                    continue
                break
            elif direction == 'inc' and not check_increase(prev_number, num):
                if already_skipped:
                    break
                if (
                    i + 1 == len(report)
                    or (i + 1 < len(report) and check_increase(prev_number, report[i + 1]))
                ):
                    already_skipped = True
                    continue
                break
            prev_number = num
        else:
            safe_count += 1

    return safe_count


if __name__ == '__main__':
    with open('2024/day2-input.txt', 'r') as f:
        reports = [[int(num) for num in line.split(' ') if num] for line in f.readlines()]

    print(f'Safe reports: {part_1(reports)}')
    print(f'Safe reports with correction: {part_2(reports)}')
