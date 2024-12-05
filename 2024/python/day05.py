from collections import defaultdict
from graphlib import TopologicalSorter

from utils import get_input_path


def parse_input(
    input: str,
) -> tuple[dict[int, set[int]], dict[int, set[int]], list[list[int]]]:
    """
    Returns children_pages, parent_pages, updates.

    `children_pages: dict[int, set[int]]` - key is a page, value is a set of children pages

    `parent_pages: dict[int, set[int]]` - key is a page, value is a set of parent pages
    """
    rules_s, updates_s = input.split("\n\n")
    rules = [tuple(map(int, r.split("|"))) for r in rules_s.splitlines()]
    children_pages: defaultdict[int, set[int]] = defaultdict(set)
    parent_pages: defaultdict[int, set[int]] = defaultdict(set)
    for first, second in rules:
        children_pages[first].add(second)
        parent_pages[second].add(first)
    updates = [list(map(int, u.split(","))) for u in updates_s.splitlines()]
    return children_pages, parent_pages, updates


def check_update(update: list[int], children_pages: dict[int, set[int]]) -> bool:
    if len(update) == 1:
        return True
    for index, page in enumerate(update[1:], 1):
        for prev_page in update[:index]:
            if prev_page in children_pages[page]:
                return False
    return True


def split_updates(
    children_pages: dict[int, set[int]], updates: list[list[int]]
) -> tuple[list[list[int]], list[list[int]]]:
    """
    Returns good updates and bad updates
    """
    good_updates: list[list[int]] = []
    bad_updates: list[list[int]] = []
    for update in updates:
        if check_update(update, children_pages):
            good_updates.append(update)
        else:
            bad_updates.append(update)
    return good_updates, bad_updates


def find_middle_sum(updates: list[list[int]]) -> int:
    middle_sum = 0
    for update in updates:
        middle_index = len(update) // 2
        middle_sum += update[middle_index]
    return middle_sum


def solve_part_1(children_pages: dict[int, set[int]], updates: list[list[int]]) -> int:
    good_updates, _ = split_updates(children_pages, updates)
    return find_middle_sum(good_updates)


def solve_part_2(
    children_pages: dict[int, set[int]],
    parent_pages: dict[int, set[int]],
    updates: list[list[int]],
) -> int:
    _, bad_updates = split_updates(children_pages, updates)
    ordered_updates: list[list[int]] = []
    for bad_update in bad_updates:
        bad_pages = set(bad_update)
        # filter out nodes from parent pages, otherwise we get cycles
        update_graph = {page: parent_pages[page] for page in bad_pages}
        ts = TopologicalSorter(update_graph)
        ordered_pages = list(ts.static_order())
        new_update: list[int] = []
        for page in ordered_pages:
            if page in bad_pages:
                new_update.append(page)
        ordered_updates.append(new_update)
    return find_middle_sum(ordered_updates)


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
children_pages, parent_pages, updates = parse_input(example)
assert solve_part_1(children_pages, updates) == 143
assert solve_part_2(children_pages, parent_pages, updates) == 123

with open(get_input_path(5)) as f:
    input = f.read()
children_pages, parent_pages, updates = parse_input(input)
assert solve_part_1(children_pages, updates) == 6951
assert solve_part_2(children_pages, parent_pages, updates) == 4121
