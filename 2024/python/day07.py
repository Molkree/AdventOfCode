from collections.abc import Sequence
from datetime import UTC, datetime

from utils import get_input_path


def parse_input(str_equations: Sequence[str]) -> list[tuple[int, list[int]]]:
    equations: list[tuple[int, list[int]]] = []
    for equation in str_equations:
        test_value, numbers = equation.split(": ")
        equations.append((int(test_value), list(map(int, numbers.split()))))
    return equations


def check_equation(
    test_value: int, numbers: list[int], check_concatenation: bool = False
) -> bool:
    if len(numbers) == 1:
        return numbers[0] == test_value
    last_number = numbers[-1]
    if last_number > test_value:
        return False
    if test_value % last_number == 0 and check_equation(
        test_value // last_number, numbers[:-1], check_concatenation
    ):
        return True
    if test_value - last_number >= 0 and check_equation(
        test_value - last_number, numbers[:-1], check_concatenation
    ):
        return True
    if check_concatenation:
        if str(test_value).endswith(str(last_number)):
            stripped_value = str(test_value).removesuffix(str(last_number))
            return stripped_value != "" and check_equation(
                int(stripped_value), numbers[:-1], check_concatenation
            )
    return False


def solve_part(input: Sequence[str], check_concatenation: bool = False) -> int:
    equations = parse_input(input)
    total_calibration_result = 0
    for test_value, numbers in equations:
        if check_equation(test_value, numbers, check_concatenation):
            total_calibration_result += test_value
    return total_calibration_result


def solve_part_1(input: Sequence[str]) -> int:
    return solve_part(input)


def solve_part_2(input: Sequence[str]) -> int:
    return solve_part(input, check_concatenation=True)


example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
assert solve_part_1(example.splitlines()) == 3749
assert solve_part_2(example.splitlines()) == 11387

with open(get_input_path(7)) as f:
    input = f.readlines()
assert solve_part_1(input) == 975671981569
timer_start = datetime.now(UTC)
assert solve_part_2(input) == 223472064194845
timer_end = datetime.now(UTC)
print("Part 2 took:", timer_end - timer_start)
