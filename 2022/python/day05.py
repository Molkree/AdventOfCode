from utils import get_input_path

with open(get_input_path(5)) as f:
    stacks_str, commands = f.read().split("\n\n")

stacks_split = stacks_str.splitlines()
stacks_count = len(stacks_split[-1].split())
stacks: list[list[str]] = [[] for _ in range(stacks_count)]
for line in stacks_split[:-1]:
    for i in range(stacks_count):
        letter = line[i * 4 + 1]
        if letter != " ":
            stacks[i].append(letter)
stacks = [stack[::-1] for stack in stacks]

stacks_2 = [stack.copy() for stack in stacks]
for _, count_str, _, from_stack_str, _, to_stack_str in map(
    str.split, commands.splitlines()
):
    count = int(count_str)
    from_stack = int(from_stack_str) - 1
    to_stack = int(to_stack_str) - 1
    for _ in range(count):
        stacks[to_stack].append(stacks[from_stack].pop())
    stacks_2[to_stack].extend(stacks_2[from_stack][-count:])
    stacks_2[from_stack] = stacks_2[from_stack][:-count]

top_crates = "".join("".join(crate[-1]) for crate in stacks)
assert top_crates == "JCMHLVGMG"
top_crates_2 = "".join("".join(crate[-1]) for crate in stacks_2)
assert top_crates_2 == "LVMRWSSPZ"
