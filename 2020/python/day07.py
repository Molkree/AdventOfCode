from collections import deque

from utils import get_input_path

day = 7
print(f"Day {day:02}")


class Bag:
    def __init__(self, bag_string: str) -> None:
        self.name = bag_string[2:]
        self.required_number = int(bag_string[0])


def build_rules(
    rule_lines: list[str],
) -> tuple[dict[str, set[str]], dict[str, set[Bag]]]:
    bottom_up: dict[str, set[str]] = {}
    top_down: dict[str, set[Bag]] = {}
    for rule in rule_lines:
        key_values = rule.split("s contain ")
        key = key_values[0]
        values = key_values[1][:-2].split(", ")
        values = [
            (value if value[0] == "1" else value[:-1]) if value[0].isdigit() else ""
            for value in values
        ]
        if values[0] == "":
            values = []
        for value in [value[2:] for value in values]:
            if value in bottom_up:
                bottom_up[value].add(key)
            else:
                bottom_up[value] = {key}
        if key in top_down:
            top_down[key] = top_down[key].union([Bag(bag) for bag in values])
        else:
            top_down[key] = {Bag(bag) for bag in values}
    return bottom_up, top_down


def dfs(rules: dict[str, set[Bag]], bag: str) -> int:
    if bag not in rules:
        return 0
    else:
        return sum(
            (1 + dfs(rules, inner_bag.name)) * inner_bag.required_number
            for inner_bag in rules[bag]
        )


with open(get_input_path(day)) as f:
    rule_lines = f.readlines()
bottom_up, top_down = build_rules(rule_lines)
part1 = set(bottom_up["shiny gold bag"])
queue = deque(part1)
while len(queue) > 0:
    bag = queue.pop()
    if bag not in bottom_up:
        continue
    new_result = part1.union(bottom_up[bag])
    difference = new_result.difference(part1)
    for container in difference:
        queue.append(container)
    part1 = new_result

print(f"Part 1: {len(part1)}")
print(f'Part 2: {dfs(top_down, "shiny gold bag")}')
