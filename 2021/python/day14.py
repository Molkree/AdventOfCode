from collections import Counter, defaultdict
from itertools import pairwise

from utils import get_input_path

with open(get_input_path(14)) as f:
    lines = f.readlines()

polymer = lines[0].rstrip()
insert_rules = [rule.rstrip().split(" -> ") for rule in lines[2:]]
replace_rules = {
    source: (source[0] + value, value + source[1]) for source, value in insert_rules
}


def grow_polymer(steps: int) -> int:
    counter: dict[str, int] = Counter(map(lambda p: "".join(p), pairwise(polymer)))
    for _ in range(steps):
        new_counter = defaultdict[str, int](int)
        for pair, count in counter.items():
            new_counter[replace_rules[pair][0]] += count
            new_counter[replace_rules[pair][1]] += count
        counter = new_counter
    letters = defaultdict[str, int](int)
    for pair, count in counter.items():
        letters[pair[0]] += count
    letters[polymer[-1]] += 1  # last char never gets replaced
    return max(letters.values()) - min(letters.values())


assert grow_polymer(10) == 2345
assert grow_polymer(40) == 2432786807053
# takes ~0.002s on my laptop for 10+40 steps
# string replacement took 6s for 17 steps
