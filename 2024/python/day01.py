from collections import Counter
from collections.abc import Iterable

from utils import get_input_path


def parse_input(rows: Iterable[str]) -> tuple[list[int], list[int]]:
    left_lst: list[int] = []
    right_lst: list[int] = []
    for row in rows:
        left, right = row.split("   ", 1)
        left_lst.append(int(left))
        right_lst.append(int(right))
    return left_lst, right_lst


def solve_part_1(left_lst: list[int], right_lst: list[int]) -> int:
    left_lst.sort()
    right_lst.sort()
    total_distance = 0
    for index, left in enumerate(left_lst):
        total_distance += abs(left - right_lst[index])
    return total_distance


def solve_part_2(left_lst: list[int], right_lst: list[int]) -> int:
    right_counter = Counter(right_lst)
    similarity_score = 0
    for number in left_lst:
        similarity_score += number * right_counter[number]
    return similarity_score


example = """3   4
4   3
2   5
1   3
3   9
3   3"""
parsed_example = parse_input(example.split("\n"))
assert solve_part_1(*parsed_example) == 11

with open(get_input_path(1)) as f:
    parsed_input = parse_input(f)
assert solve_part_1(*parsed_input) == 3246517

assert solve_part_2(*parsed_example) == 31
assert solve_part_2(*parsed_input) == 29379307
