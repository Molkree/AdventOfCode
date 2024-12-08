from concurrent.futures import ProcessPoolExecutor
from datetime import UTC, datetime

from utils import get_input_path

DIRECTIONS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
TURNS = {"^": ">", ">": "v", "v": "<", "<": "^"}
OBSTACLE = "#"
EMPTY_SLOT = "."


Grid = list[list[str]]
Coord = tuple[int, int]


def parse_input(input: str) -> Grid:
    return [list(line) for line in input.splitlines()]


def find_guard_coords(grid: Grid) -> Coord:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in "^v<>":
                return x, y
    raise ValueError("No guard found")


def check_coord_within_grid(grid: Grid, x: int, y: int) -> bool:
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def turn(grid: Grid, x: int, y: int, guard: str) -> tuple[Coord, str]:
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


Move = tuple[int, int, str]


def make_move(grid: Grid, x: int, y: int, guard: str) -> Move | None:
    direction = DIRECTIONS[guard]
    old_x, old_y = x, y
    x, y = x + direction[0], y + direction[1]
    if not (check_coord_within_grid(grid, x, y)):
        return None
    if grid[y][x] == OBSTACLE:
        (x, y), guard = turn(grid, old_x, old_y, guard)
    return x, y, guard


def solve_part_1(grid: Grid) -> int:
    x, y = find_guard_coords(grid)
    guard = grid[y][x]
    visited = {(x, y)}
    while True:
        move = make_move(grid, x, y, guard)
        if not move:
            break
        x, y, guard = move
        visited.add((x, y))
    return len(visited)


def detect_loop(grid: Grid, x: int, y: int) -> bool:
    guard = grid[y][x]
    point = (x, y), guard
    visited_points = {point}
    while True:
        move = make_move(grid, x, y, guard)
        if not move:
            break
        x, y, guard = move
        point = (x, y), guard
        if point in visited_points:
            return True
        visited_points.add(point)
    return False


def check_loop(grid: Grid, item: tuple[Coord, Move]) -> bool:
    (x, y), (prev_x, prev_y, prev_guard) = item
    grid[y][x] = OBSTACLE
    grid[prev_y][prev_x] = prev_guard
    return detect_loop(grid, prev_x, prev_y)


def solve_part_2(grid: Grid) -> int:
    x, y = find_guard_coords(grid)
    guard = grid[y][x]
    guard_x, guard_y = x, y
    prev: dict[Coord, Move] = {}
    while True:
        prev_x, prev_y, prev_guard = x, y, guard
        move = make_move(grid, x, y, guard)
        if not move:
            break
        x, y, guard = move
        if (x, y) not in prev and (x, y) != (guard_x, guard_y):
            prev[(x, y)] = prev_x, prev_y, prev_guard
    with ProcessPoolExecutor() as executor:
        results = executor.map(check_loop, [grid] * len(prev), prev.items())
    return sum(results)


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
