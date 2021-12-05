from utils import get_input_path

day = 6
print(f"Day {day:02}")
with open(get_input_path(day)) as f:
    groups = f.read().split("\n\n")
    part1 = sum(len(set(group.replace("\n", ""))) for group in groups)
    part2 = sum(
        len(set[str].intersection(*map(set[str], group.split()))) for group in groups
    )

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
