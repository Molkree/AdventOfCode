from collections import deque

from utils import get_input_path

with open(get_input_path(5)) as f:
    stacks_str, commands = f.read().split("\n\n")

stacks_split = stacks_str.splitlines()
stacks_count = len(stacks_split[-1].split())
stacks: list[deque[str]] = [deque[str]() for _ in range(stacks_count)]
for line in stacks_split[:-1]:
    for i in range(stacks_count):
        letter = line[i * 4 + 1]
        if letter != " ":
            stacks[i].append(letter)

for _, count, _, from_crate, _, to_crate in map(str.split, commands.splitlines()):
    for _ in range(int(count)):
        stacks[int(to_crate) - 1].appendleft(stacks[int(from_crate) - 1].popleft())
top_crates = "".join("".join(crate[0]) for crate in stacks)
assert top_crates == "JCMHLVGMG"
