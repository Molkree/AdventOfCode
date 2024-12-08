from datetime import UTC, datetime

from utils import get_input_path

DIRECTIONS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
TURNS = {"^": ">", ">": "v", "v": "<", "<": "^"}
OBSTACLE = "#"
EMPTY_SLOT = "."


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


def turn(
    grid: list[list[str]], x: int, y: int, guard: str
) -> tuple[tuple[int, int], str]:
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


def make_move(
    grid: list[list[str]], x: int, y: int, guard: str
) -> tuple[int, int, str]:
    direction = DIRECTIONS[guard]
    old_x, old_y = x, y
    x, y = x + direction[0], y + direction[1]
    if not (check_coord_within_grid(grid, x, y)):
        return x, y, guard
    if grid[y][x] == OBSTACLE:
        (x, y), guard = turn(grid, old_x, old_y, guard)
    return x, y, guard


def solve_part_1(grid: list[list[str]]) -> int:
    x, y = find_guard_coords(grid)
    guard = grid[y][x]
    visited = {(x, y)}
    while True:
        x, y, guard = make_move(grid, x, y, guard)
        if not check_coord_within_grid(grid, x, y):
            break
        visited.add((x, y))
    return len(visited)


def detect_loop(grid: list[list[str]], x: int, y: int) -> bool:
    guard = grid[y][x]
    point = (x, y), guard
    visited_points = {point}
    while True:
        x, y, guard = make_move(grid, x, y, guard)
        if not check_coord_within_grid(grid, x, y):
            break
        point = (x, y), guard
        if point in visited_points:
            return True
        visited_points.add(point)
    return False


def solve_part_2(grid: list[list[str]]) -> int:
    x, y = find_guard_coords(grid)
    guard = grid[y][x]
    guard_x, guard_y = x, y
    prev: dict[tuple[int, int], tuple[int, int, str]] = {}
    while True:
        prev_x, prev_y, prev_guard = x, y, guard
        x, y, guard = make_move(grid, x, y, guard)
        if not check_coord_within_grid(grid, x, y):
            break
        if (x, y) not in prev:
            prev[(x, y)] = prev_x, prev_y, prev_guard
    loops_count = 0
    for (x, y), (prev_x, prev_y, prev_guard) in prev.items():
        if (x, y) == (guard_x, guard_y):
            continue
        grid[y][x] = OBSTACLE
        grid[prev_y][prev_x] = prev_guard
        if detect_loop(grid, prev_x, prev_y):
            loops_count += 1
        grid[prev_y][prev_x] = EMPTY_SLOT
        grid[y][x] = EMPTY_SLOT
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
