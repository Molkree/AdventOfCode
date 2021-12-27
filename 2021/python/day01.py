from utils import get_input_path

with open(get_input_path(1)) as f:
    lines = f.readlines()

# Part 1
increases = 0
for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i - 1]):
        increases += 1
assert increases == 1475

# Part 2
increases = 0
for i in range(3, len(lines)):
    prev_sum = int(lines[i - 3]) + int(lines[i - 2]) + int(lines[i - 1])
    cur_sum = prev_sum - int(lines[i - 3]) + int(lines[i])
    if prev_sum < cur_sum:
        increases += 1
assert increases == 1516
