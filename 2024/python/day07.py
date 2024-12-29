from collections.abc import Callable, Iterable, Sequence
from datetime import UTC, datetime
from itertools import product
from operator import add, mul

from utils import get_input_path


def parse_input(str_equations: Sequence[str]) -> list[tuple[int, list[int]]]:
    equations: list[tuple[int, list[int]]] = []
    for equation in str_equations:
        test_value, numbers = equation.split(": ")
        equations.append((int(test_value), list(map(int, numbers.split()))))
    return equations


def check_equation(
    operations: Iterable[Callable[[int, int], int]], test_value: int, numbers: list[int]
) -> bool:
    combinations = product(operations, repeat=len(numbers) - 1)

    for combination in combinations:
        value = numbers[0]
        for i, operation in enumerate(combination):
            value = operation(value, numbers[i + 1])
            if value > test_value:
                break
        if value == test_value:
            return True
    return False


def solve_part(
    input: Sequence[str], operations: Iterable[Callable[[int, int], int]]
) -> int:
    equations = parse_input(input)
    total_calibration_result = 0
    for test_value, numbers in equations:
        if check_equation(operations, test_value, numbers):
            total_calibration_result += test_value
    return total_calibration_result


def solve_part_1(input: Sequence[str]) -> int:
    operations = [add, mul]
    return solve_part(input, operations)


def solve_part_2(input: Sequence[str]) -> int:
    def concatenation(a: int, b: int) -> int:
        return int(str(a) + str(b))

    operations: list[Callable[[int, int], int]] = [add, mul, concatenation]
    return solve_part(input, operations)


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
