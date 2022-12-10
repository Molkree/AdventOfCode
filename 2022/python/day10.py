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
