from utils import get_input_path

day = 3
print(f"Day {day:02}")
with open(get_input_path(day)) as f:
    lines = f.readlines()
    width = len(lines[0]) - 1
    height = len(lines)


def slide(dy: int, dx: int) -> int:
    x, y, trees_encountered = 0, 0, 0
    while y < height - dy:
        y += dy
        x = (x + dx) % width
        if lines[y][x] == "#":
            trees_encountered += 1
    return trees_encountered


print("Part 1:", slide(1, 3))
print("Part 2:", slide(1, 1) * slide(1, 3) * slide(1, 5) * slide(1, 7) * slide(2, 1))
