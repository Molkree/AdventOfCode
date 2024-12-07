from copy import deepcopy
from datetime import UTC, datetime

from utils import get_input_path

DIRECTIONS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
TURNS = {"^": ">", ">": "v", "v": "<", "<": "^"}
OBSTACLE = "#"


def parse_input(input: str) -> list[list[str]]:
    return [list(line) for line in input.splitlines()]


def find_guard_coords(grid: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in "^v<>":
                return x, y
    raise ValueError("No guard found")


def check_coord_within_grid(grid: list[list[str]], x: int, y: int) -> bool:
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def turn(grid: list[list[str]], x: int, y: int) -> tuple[tuple[int, int], str]:
    guard = grid[y][x]
    guard = TURNS[guard]
    direction = DIRECTIONS[guard]
    old_x, old_y = x, y
    x, y = x + direction[0], y + direction[1]
    if not check_coord_within_grid(grid, x, y):
        return (x, y), guard
    # we might have to turn again if there's an obstacle
    if grid[y][x] == OBSTACLE:
        guard = TURNS[guard]
        direction = DIRECTIONS[guard]
        x, y = old_x + direction[0], old_y + direction[1]
    return (x, y), guard


def make_move(grid: list[list[str]], x: int, y: int) -> tuple[int, int]:
    guard = grid[y][x]
    direction = DIRECTIONS[guard]
    old_x, old_y = x, y
    x, y = x + direction[0], y + direction[1]
    if not (check_coord_within_grid(grid, x, y)):
        return x, y
    if grid[y][x] == OBSTACLE:
        (x, y), guard = turn(grid, old_x, old_y)
    if check_coord_within_grid(grid, x, y):
        grid[y][x] = guard
    return x, y


def solve_part_1(grid: list[list[str]]) -> int:
    x, y = find_guard_coords(grid)
    visited = {(x, y)}
    while True:
        x, y = make_move(grid, x, y)
        if not check_coord_within_grid(grid, x, y):
            break
        visited.add((x, y))
    return len(visited)


def detect_loop(grid: list[list[str]], x: int, y: int) -> bool:
    guard = grid[y][x]
    point = (x, y), guard
    visited_points = {point}
    while True:
        x, y = make_move(grid, x, y)
        if not check_coord_within_grid(grid, x, y):
            break
        guard = grid[y][x]
        point = (x, y), guard
        if point in visited_points:
            return True
        visited_points.add(point)
    return False


def solve_part_2(grid: list[list[str]]) -> int:
    x, y = find_guard_coords(grid)
    guard_x, guard_y = x, y
    path = {(x, y)}
    copy_grid = [deepcopy(row) for row in grid]
    while True:
        x, y = make_move(copy_grid, x, y)
        if not check_coord_within_grid(grid, x, y):
            break
        path.add((x, y))
    loops_count = 0
    for x, y in path:
        if (x, y) == (guard_x, guard_y):
            continue
        copy_grid = [deepcopy(row) for row in grid]
        copy_grid[y][x] = OBSTACLE
        if detect_loop(copy_grid, guard_x, guard_y):
            loops_count += 1
    return loops_count


example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
assert solve_part_1(parse_input(example)) == 41
assert solve_part_2(parse_input(example)) == 6

with open(get_input_path(6)) as f:
    input = f.read()
assert solve_part_1(parse_input(input)) == 5177
timer_start = datetime.now(UTC)
assert solve_part_2(parse_input(input)) == 1686
timer_end = datetime.now(UTC)
print("Part 2 took:", timer_end - timer_start)
