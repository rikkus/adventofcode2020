def numbers(input_data):
    return (int(x) for x in input_data.split("\n"))


def part_one(input_data):
    nums = numbers(input_data)
    seen = set()
    for n in nums:
        if 2020 - n in seen:
            return (2020 - n) * n
        seen.add(n)


def part_two(input_data):
    nums = numbers(input_data)
    seen = set()
    for n in nums:
        for s in seen:
            if 2020 - n - s in seen:
                return n * s * (2020 - n - s)
        seen.add(n)
