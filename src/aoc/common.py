from os import path
from rtoml import load as toml_load


def read_file(file_path) -> str:
    with open(file_path) as f:
        return f.read().rstrip()


answers: dict = toml_load(read_file('answers.toml'))


def answer(day: int, part: int) -> str:
    return answers[str(day)][str(part)]


def data(day_number, part_number) -> str:
    filename = f"test_input_day{day_number}.txt"
    if path.isfile(filename):
        return read_file(filename)
    else:
        return read_file(f"test_input_day{day_number}_{part_number}.txt")
