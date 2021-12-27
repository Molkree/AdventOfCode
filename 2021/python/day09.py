import operator
from functools import reduce

from utils import get_input_path

with open(get_input_path(9)) as f:
    lines = f.readlines()
heightmap = [[10] + [int(height) for height in line.rstrip()] + [10] for line in lines]
heightmap_width = len(heightmap[0])
heightmap = [[10] * heightmap_width] + heightmap + [[10] * heightmap_width]
heightmap_height = len(heightmap)
risk_level = 0
low_points = list[tuple[int, int]]()
for i in range(1, heightmap_height - 1):
    for j in range(1, heightmap_width - 1):
        if all(
            height > heightmap[i][j]
            for height in (
                heightmap[i - 1][j],
                heightmap[i + 1][j],
                heightmap[i][j - 1],
                heightmap[i][j + 1],
            )
        ):
            risk_level += 1 + heightmap[i][j]
            low_points.append((i, j))
assert risk_level == 530

areas = list[int]()
for i, j in low_points:
    stack = list[tuple[int, int]]()
    visited = {(i, j)}

    def add_neighbors(i: int, j: int) -> None:
        def good_neighbor(i: int, j: int) -> bool:
            return (
                0 < i < heightmap_height - 1
                and 0 < j < heightmap_width - 1
                and (i, j) not in visited
                and heightmap[i][j] < 9
            )

        neighbor_i = i - 1
        neighbor_j = j
        if good_neighbor(neighbor_i, neighbor_j):
            stack.append((neighbor_i, neighbor_j))
            visited.add((neighbor_i, neighbor_j))
        neighbor_i = i + 1
        if good_neighbor(neighbor_i, neighbor_j):
            stack.append((neighbor_i, neighbor_j))
            visited.add((neighbor_i, neighbor_j))
        neighbor_i = i
        neighbor_j = j - 1
        if good_neighbor(neighbor_i, neighbor_j):
            stack.append((neighbor_i, neighbor_j))
            visited.add((neighbor_i, neighbor_j))
        neighbor_j = j + 1
        if good_neighbor(neighbor_i, neighbor_j):
            stack.append((neighbor_i, neighbor_j))
            visited.add((neighbor_i, neighbor_j))

    add_neighbors(i, j)
    area = 1
    while stack:
        i, j = stack.pop()
        area += 1
        add_neighbors(i, j)
    areas.append(area)
assert reduce(operator.mul, sorted(areas)[-3:]) == 1019494
