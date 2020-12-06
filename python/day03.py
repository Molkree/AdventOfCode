with open('../input/input03.txt') as f:
  lines = f.readlines()
  width = len(lines[0]) - 1
  height = len(lines)

def slide(dy, dx):
  x, y, treesEncountered = 0, 0, 0
  while (y < height - dy):
    y += dy
    x = (x + dx) % width
    if (lines[y][x] == '#'):
      treesEncountered += 1
  return treesEncountered

print('Part 1:', slide(1, 3))
print('Part 2:', slide(1, 1) * slide(1, 3) * slide(1, 5) * slide(1, 7) * slide(2, 1))
