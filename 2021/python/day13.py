from utils import get_input_path

with open(get_input_path(13)) as f:
    lines = f.readlines()

dots = list[tuple[int, int]]()
folds = list[tuple[bool, int]]()
for line in lines:
    if "," in line:
        x, y = map(int, line.split(","))
        dots.append((x, y))
    elif any(fold in line for fold in "xy"):
        folds.append(("x" in line, int(line.split("=")[1])))


def fold(is_vertical: bool, line_ind: int) -> list[tuple[int, int]]:
    new_dots = list[tuple[int, int]]()
    if is_vertical:
        for dot in dots:
            if dot[0] > line_ind:
                new_dot = 2 * line_ind - dot[0], dot[1]
                if new_dot not in dots:
                    new_dots.append(new_dot)
            else:
                new_dots.append(dot)
    else:
        for dot in dots:
            if dot[1] > line_ind:
                new_dot = dot[0], 2 * line_ind - dot[1]
                if new_dot not in dots:
                    new_dots.append(new_dot)
            else:
                new_dots.append(dot)
    return new_dots


dots = fold(*folds[0])
assert len(dots) == 743

for fold_instruction in folds[1:]:
    dots = fold(*fold_instruction)
width = max(x for x, _ in dots) + 1
height = max(y for _, y in dots) + 1
paper = [["."] * width for _ in range(height)]
for x, y in dots:
    paper[y][x] = "#"
for line in map("".join, paper):
    print(line)
# It's "RCPLAKHL" :)
