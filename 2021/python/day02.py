from utils import get_input_path

with open(get_input_path(2)) as f:
    lines = f.readlines()

# Part 1
horizontal = 0
depth = 0
for command in lines:
    match command.split():
        case "forward", x:
            horizontal += int(x)
        case "up", x:
            depth -= int(x)
        case "down", x:
            depth += int(x)
assert horizontal * depth == 1636725

# Part 2
horizontal = 0
depth = 0
aim = 0
for command in lines:
    match command.split():
        case "forward", x:
            horizontal += int(x)
            depth += aim * int(x)
        case "up", x:
            aim -= int(x)
        case "down", x:
            aim += int(x)
assert horizontal * depth == 1872757425
