from collections.abc import Iterable
from math import copysign

from utils import get_input_path


def parse_input(rows: Iterable[str]) -> list[list[int]]:
    return [list(map(int, row.split())) for row in rows]


def count_safe_reports(reports: list[list[int]]) -> int:
    unsafe_count = 0
    for report in reports:
        sign = copysign(1, report[1] - report[0])
        for ind, level in enumerate(report[1:], start=1):
            diff = level - report[ind - 1]
            if not diff or abs(diff) > 3 or copysign(1, diff) != sign:
                unsafe_count += 1
                break
    return len(reports) - unsafe_count


example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
parsed_example = parse_input(example.split("\n"))
assert count_safe_reports(parsed_example) == 2

parsed_input = parse_input(open(get_input_path(2)))
assert count_safe_reports(parsed_input) == 524
