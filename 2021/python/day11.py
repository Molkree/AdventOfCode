from copy import deepcopy
from itertools import product

from utils import get_input_path

with open(get_input_path(11)) as f:
    lines = f.readlines()
grid = [[int(octopus) for octopus in line.rstrip()] for line in lines]


def step() -> int:
    revisit = set[tuple[int, int]]()
    flashes = 0

    def transfer_energy(i: int, j: int) -> None:
        def good_neighbor(i: int, j: int) -> bool:
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] > 0

        for shift in product((-1, 0, 1), repeat=2):
            if shift == (0, 0):
                continue
            neighbor_i, neighbor_j = i + shift[0], j + shift[1]
            if good_neighbor(neighbor_i, neighbor_j):
                grid[neighbor_i][neighbor_j] += 1
                revisit.add((neighbor_i, neighbor_j))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                transfer_energy(i, j)
                grid[i][j] = 0
                flashes += 1
    while revisit:
        i, j = revisit.pop()
        if grid[i][j] > 9:
            transfer_energy(i, j)
            grid[i][j] = 0
            flashes += 1
    return flashes


copy_grid = deepcopy(grid)
total_flashes = 0
first_bright_step = 0
octopuses_count = len(grid) * len(grid[0])
for i in range(100):
    flashes = step()
    total_flashes += flashes
    if flashes == octopuses_count:
        first_bright_step = i + 1
assert total_flashes == 1647
steps_count = 100
while first_bright_step == 0:
    steps_count += 1
    if step() == octopuses_count:
        first_bright_step = steps_count
assert first_bright_step == 348
