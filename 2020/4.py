from os.path import join
from re import match
from typing import List


fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def read_input(path: str) -> List[str]:
    with open(path) as f:
        values = f.read().split('\n\n')

    values = [x.replace('\n', ' ').strip() for x in values]
    return values


def valid_fields(passport: str) -> bool:
    return all([f in passport for f in fields])


def validate_field_values(field: str, value: str) -> bool:
    def valid_hgt(value: str) -> bool:
        if value.endswith('cm'):
            if 150 <= int(value.strip('cm')) <= 193:
                return True

        if value.endswith('in'):
            if 59 <= int(value.strip('in')) <= 76:
                return True

        return False

    def valid_pid(value: str) -> bool:
        if len(value) != 9:
            return False

        try:
            int(value)
        except ValueError:
            return False

        return True

    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    validator = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': valid_hgt,
        'hcl': lambda x: match(r'#[0-9a-f]{6}', x) is not None,
        'ecl': lambda x: x in valid_ecl,
        'pid': valid_pid,
        'cid': lambda x: True
    }

    return validator.get(field, False)(value)


def get_valid_passports(passports: List[str]) -> List[str]:
    return list(filter(lambda x: valid_fields(x), passports))


def part_one(passports: List[str]) -> int:
    return len(get_valid_passports(passports))


def part_two(passports: List[str]) -> int:
    valid = 0
    for p in get_valid_passports(passports):
        p_fields = p.split(' ')
        for f in p_fields:
            k, v = f.split(':')
            if not validate_field_values(k, v):
                break
        else:
            valid += 1

    return valid


if __name__ == "__main__":
    input_values = read_input(join('inputs', '4.txt'))
    print(part_one(input_values))
    print(part_two(input_values))
