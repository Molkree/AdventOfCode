from collections.abc import Iterable
from math import copysign

from utils import get_input_path


def parse_input(rows: Iterable[str]) -> list[list[int]]:
    return [list(map(int, row.split())) for row in rows]


def check_report(report: list[int], strict: bool) -> bool:
    sign = copysign(1, report[1] - report[0])
    for ind, level in enumerate(report[:-1]):
        diff = report[ind + 1] - level
        if abs(diff) not in (1, 2, 3) or copysign(1, diff) != sign:
            if strict:
                return False
            else:
                # remove previous level
                check = check_report(report[0 : ind - 1] + report[ind:], strict=True)
                if check:
                    return True
                # remove current level
                check = check_report(report[0:ind] + report[ind + 1 :], strict=True)
                if check:
                    return True
                # remove next level
                check = check_report(
                    report[0 : ind + 1] + report[ind + 2 :], strict=True
                )
                if check:
                    return True
                return False
    return True


assert check_report([1, 2, 7, 3], strict=False)
assert check_report([1, 2, 7], strict=False)
assert check_report([3, 4, 2, 1], strict=False)
assert check_report([2, 3, 2, 1], strict=False)


def count_safe_reports(reports: list[list[int]], strict: bool) -> int:
    unsafe_count = 0
    for report in reports:
        if not check_report(report, strict=strict):
            unsafe_count += 1
    return len(reports) - unsafe_count


example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
parsed_example = parse_input(example.split("\n"))
assert count_safe_reports(parsed_example, strict=True) == 2
assert count_safe_reports(parsed_example, strict=False) == 4

with open(get_input_path(2)) as f:
    parsed_input = parse_input(f)
assert count_safe_reports(parsed_input, strict=True) == 524
assert count_safe_reports(parsed_input, strict=False) == 569
