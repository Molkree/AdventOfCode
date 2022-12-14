from copy import deepcopy

from utils import get_input_path

AIR = "."
ROCK = "#"
SAND = "o"


def parse_path(str_path: str) -> list[tuple[int, int]]:
    path: list[tuple[int, int]] = []
    for point in str_path.split(" ->"):
        x, y = map(int, point.split(","))
        path.append((x, y))
    return path


with open(get_input_path(14)) as f:
    paths = list(map(parse_path, f.read().splitlines()))


def build_grid(paths: list[list[tuple[int, int]]]) -> tuple[list[list[str]], int]:
    min_left, max_right, bottom = 500, 0, 0
    for path in paths:
        for x, y in path:
            min_left = min(min_left, x)
            max_right = max(max_right, x)
            bottom = max(bottom, y)
    width = max_right - min_left + 1
    height = bottom + 1
    grid = [[AIR for _ in range(width)] for _ in range(height)]
    grid[0][500 - min_left] = "+"
    for path in paths:
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            if x1 == x2:
                y1, y2 = sorted((y1, y2))
                for y in range(y1, y2 + 1):
                    grid[y][x1 - min_left] = ROCK
            else:
                x1, x2 = sorted((x1, x2))
                for x in range(x1, x2 + 1):
                    grid[y1][x - min_left] = ROCK
    return grid, 500 - min_left


def pour_sand(
    grid: list[list[str]], source_x: int, endless_void: bool = True
) -> tuple[list[list[str]], int, bool]:
    x, y = source_x, 0
    while 0 <= y < len(grid) - 1 and 0 <= x < len(grid[0]):
        if grid[y + 1][x] == AIR:
            y += 1
        elif x - 1 < 0:
            if endless_void:
                return grid, source_x, False
            grid = [[AIR] + row for row in grid]
            grid[-1][0] = ROCK
            x += 1
            source_x += 1
        elif grid[y + 1][x - 1] == AIR:
            x -= 1
            y += 1
        elif x + 1 == len(grid[0]):
            if endless_void:
                return grid, source_x, False
            grid = [row + [AIR] for row in grid]
            grid[-1][-1] = ROCK
        elif grid[y + 1][x + 1] == AIR:
            x += 1
            y += 1
        elif grid[y][x] != SAND:
            grid[y][x] = SAND
            return grid, source_x, True
        else:
            return grid, source_x, False
    return grid, source_x, False


grid, source_x = build_grid(paths)
grid_2 = deepcopy(grid)
grains = 0
while True:
    grid, source_x, added_sand = pour_sand(grid, source_x)
    if not added_sand:
        break
    grains += 1
assert grains == 817

grid_2.append([AIR for _ in range(len(grid_2[0]))])
grid_2.append([ROCK for _ in range(len(grid_2[0]))])
grains = 0
while True:
    grid_2, source_x, added_sand = pour_sand(grid_2, source_x, endless_void=False)
    if not added_sand:
        break
    grains += 1
assert grains == 23416
