import inspect

from utils import get_input_path

with open(get_input_path(10)) as f:
    instructions = f.read().splitlines()

register = 1
history = [1]
for instruction in instructions:
    if instruction.startswith("addx"):
        history.append(register)
        register += int(instruction.split()[1])
    history.append(register)
signal_strengths: list[int] = []
for i in range(19, 221, 40):
    signal_strengths.append(history[i] * (i + 1))
assert sum(signal_strengths) == 13220

lines: list[str] = []
for row in range(6):
    line: list[str] = []
    for col in range(40):
        pixel = row * 40 + col
        if history[pixel] - 1 <= col <= history[pixel] + 1:
            line.append("#")
        else:
            line.append(".")
    lines.append("".join(line))
answer = inspect.cleandoc("""
###..#..#..##..#..#.#..#.###..####.#..#.
#..#.#..#.#..#.#.#..#..#.#..#.#....#.#..
#..#.#..#.#..#.##...####.###..###..##...
###..#..#.####.#.#..#..#.#..#.#....#.#..
#.#..#..#.#..#.#.#..#..#.#..#.#....#.#..
#..#..##..#..#.#..#.#..#.###..####.#..#.""")  # RUAKHBEK
assert "\n".join(lines) == answer
