from utils import get_input_path


def get_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1


with open(get_input_path(3)) as f:
    rucksacks = list(map(str.rstrip, f.readlines()))

sum_priorities = 0
for rucksack in rucksacks:
    half_capacity = len(rucksack) // 2
    comp_1, comp_2 = rucksack[:half_capacity], rucksack[half_capacity:]
    bad_item = (set(comp_1) & set(comp_2)).pop()
    sum_priorities += get_priority(bad_item)
assert sum_priorities == 8139

sum_priorities = 0
for i in range(0, len(rucksacks), 3):
    common_item = (
        set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])
    ).pop()
    sum_priorities += get_priority(common_item)
assert sum_priorities == 2668
