from collections import defaultdict

from utils import get_input_path


def parse_input(input: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    rules_s, updates_s = input.split("\n\n")
    rules = [tuple(map(int, r.split("|"))) for r in rules_s.splitlines()]
    number_sets: defaultdict[int, set[int]] = defaultdict(set)
    for first, second in rules:
        number_sets[first].add(second)
    updates = [list(map(int, u.split(","))) for u in updates_s.splitlines()]
    return number_sets, updates


def check_update(update: list[int], number_sets: dict[int, set[int]]) -> bool:
    if len(update) == 1:
        return True
    for index, page in enumerate(update[1:], 1):
        for prev_page in update[:index]:
            if prev_page in number_sets[page]:
                return False
    return True


def solve_part_1(number_sets: dict[int, set[int]], updates: list[list[int]]) -> int:
    middle_sum = 0
    for update in updates:
        if check_update(update, number_sets):
            middle_index = len(update) // 2
            middle_sum += update[middle_index]
    return middle_sum


example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
assert solve_part_1(*parse_input(example)) == 143

with open(get_input_path(5)) as f:
    input = f.read()
assert solve_part_1(*parse_input(input)) == 6951
