print('Day 06')
with open('../input/input06.txt') as f:
  groups = f.read().split('\n\n')
  part1 = sum([len(set(group.replace('\n', ''))) for group in groups])
  part2 = sum([len(set.intersection(*map(set, group.split()))) for group in groups])

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
