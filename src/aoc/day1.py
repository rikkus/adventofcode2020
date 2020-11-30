def helper_needs_testing_too(s: str) -> str:
    return s[::-1]


def part_one(input_data):
    return helper_needs_testing_too(input_data)


def part_two(input_data):
    x = 42
    return len(part_one(input_data))
