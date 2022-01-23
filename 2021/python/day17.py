import re

from utils import get_input_path

with open(get_input_path(17)) as f:
    coords = f.readline()

x1, x2, y1, y2 = map(
    int, re.search("target area: x=(\\d+)..(\\d+), y=(-\\d+)..(-\\d+)", coords).groups()  # type: ignore
)

y_velocity = -y1 - 1
max_height = y_velocity * (y_velocity + 1) // 2  # sum of arithmetic progression
assert max_height == 4095
