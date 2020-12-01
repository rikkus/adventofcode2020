import pytest
import importlib
import src.aoc.common as helper

all_days_both_parts : [(int, int)] = [
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
]

days_and_parts_to_test_now = [(1, 1), (1, 2)]


@pytest.mark.parametrize('day,part', days_and_parts_to_test_now)
def test_part(day, part):
    module = importlib.import_module(f"src.aoc.day{day}")
    data = helper.data(day, part)
    answer = helper.answer(day, part)
    if part == 1:
        assert module.part_one(data) == answer
    elif part == 2:
        assert module.part_two(data) == answer

