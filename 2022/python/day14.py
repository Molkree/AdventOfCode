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
    return grid, min_left


def pour_sand(grid: list[list[str]], source_x: int) -> bool:
    x, y = source_x, 0
    while 0 <= y < len(grid) - 1 and 0 <= x < len(grid[0]):
        if grid[y + 1][x] == AIR:
            y += 1
        elif x - 1 < 0:
            return False
        elif grid[y + 1][x - 1] == AIR:
            x -= 1
            y += 1
        elif x + 1 == len(grid[0]):
            return False
        elif grid[y + 1][x + 1] == AIR:
            x += 1
            y += 1
        elif grid[y][x] != SAND:
            grid[y][x] = SAND
            return True
        else:
            return False
    return False


grid, min_left = build_grid(paths)
grains = 0
while True:
    if not pour_sand(grid, 500 - min_left):
        break
    grains += 1
for row in grid:
    print("".join(row))
assert grains == 817
