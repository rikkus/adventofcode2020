def helper_needs_testing_too(s: str) -> str:
    return s[::-1]


def part_one(input_data):
    floor = 0
    for c in input_data:
        if c == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def part_two(input_data):
    floor = 0
    pos = 0
    for c in input_data:
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return pos + 1
        pos += 1

