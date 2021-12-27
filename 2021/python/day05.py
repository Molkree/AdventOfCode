from utils import get_input_path


class VentLine:
    def __init__(self, coords: str) -> None:
        start, end = coords.rstrip().split(" -> ")
        self.x1, self.y1 = map(int, start.split(","))
        self.x2, self.y2 = map(int, end.split(","))


with open(get_input_path(5)) as f:
    lines = f.readlines()

vent_lines = [VentLine(coords) for coords in lines]
max_x, max_y = 0, 0
for vent_line in vent_lines:
    max_x = max(max_x, vent_line.x1, vent_line.x2)
    max_y = max(max_y, vent_line.y1, vent_line.y2)

simple_field = [[0] * (max_x + 1) for _ in range(max_y + 1)]
field = [[0] * (max_x + 1) for _ in range(max_y + 1)]
for vent_line in vent_lines:
    if vent_line.x1 == vent_line.x2:
        start, end = sorted((vent_line.y1, vent_line.y2))
        for row in range(start, end + 1):
            simple_field[row][vent_line.x1] += 1
            field[row][vent_line.x1] += 1
    elif vent_line.y1 == vent_line.y2:
        start, end = sorted((vent_line.x1, vent_line.x2))
        for column in range(start, end + 1):
            simple_field[vent_line.y1][column] += 1
            field[vent_line.y1][column] += 1
    else:
        x1, y1, x2, y2 = vent_line.x1, vent_line.y1, vent_line.x2, vent_line.y2
        if (
            vent_line.x1 > vent_line.x2
            and vent_line.y1 > vent_line.y2
            or vent_line.x1 > vent_line.x2
            and vent_line.y1 < vent_line.y2
        ):
            x1, y1, x2, y2 = vent_line.x2, vent_line.y2, vent_line.x1, vent_line.y1
        for column in range(x1, x2 + 1):
            if y1 < y2:
                field[y1 + column - x1][column] += 1
            else:
                field[y1 - column + x1][column] += 1

simple_count = 0
count = 0
for row_ind, row in enumerate(simple_field):
    for col_ind, point in enumerate(row):
        if point > 1:
            simple_count += 1
        if field[row_ind][col_ind] > 1:
            count += 1

assert simple_count == 4655
assert count == 20500
