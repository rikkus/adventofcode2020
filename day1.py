def part_one():
    with open("input/1.txt") as f:
        return f.read().rstrip()[::-1]


def part_two():
    return len(part_one())


def test_part_one():
    assert part_one() == "hello, world!"


def test_part_two():
    assert part_two() == 13
