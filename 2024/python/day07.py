from collections.abc import Sequence
from itertools import product
from operator import add, mul

from utils import get_input_path


def parse_input(str_equations: Sequence[str]) -> list[tuple[int, list[int]]]:
    equations: list[tuple[int, list[int]]] = []
    for equation in str_equations:
        test_value, numbers = equation.split(": ")
        equations.append((int(test_value), list(map(int, numbers.split()))))
    return equations


def check_equation(test_value: int, numbers: list[int]) -> bool:
    operations = [add, mul]
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


def solve_part_1(input: Sequence[str]) -> int:
    equations = parse_input(input)
    total_calibration_result = 0
    for test_value, numbers in equations:
        if check_equation(test_value, numbers):
            total_calibration_result += test_value
    return total_calibration_result


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

with open(get_input_path(7)) as f:
    input = f.readlines()
assert solve_part_1(input) == 975671981569
