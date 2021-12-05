from utils import get_input_path

day = 1
print(f"Day {day:02}")
numbers: list[int] = []
with open(get_input_path(day)) as f:
    for line in f:
        numbers.append(int(line.strip("\n")))
for i, first in enumerate(numbers):
    for j, second in enumerate(numbers[i:]):
        if first + second == 2020:
            print("Part 1:", first * second)
        for k, third in enumerate(numbers[j:]):
            if first + second + third == 2020:
                print("Part 2:", first * second * third)
