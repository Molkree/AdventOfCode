from utils import get_input_path


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


def make_move(grid: list[list[str]], x: int, y: int) -> tuple[int, int]:
    directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    guard = grid[y][x]
    direction = directions[guard]
    old_x, old_y = x, y
    x += direction[0]
    y += direction[1]
    if not (check_coord_within_grid(grid, x, y)):
        return x, y
    if grid[y][x] == "#":
        turns = {"^": ">", ">": "v", "v": "<", "<": "^"}
        guard = turns[guard]
        direction = directions[guard]
        x, y = old_x, old_y
        x += direction[0]
        y += direction[1]
    if check_coord_within_grid(grid, x, y):
        grid[y][x] = guard
    return x, y


def solve_part_1(grid: list[list[str]]) -> int:
    x, y = find_guard_coords(grid)
    visited = {(x, y)}
    while check_coord_within_grid(grid, x, y):
        x, y = make_move(grid, x, y)
        visited.add((x, y))
    return len(visited) - 1


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

with open(get_input_path(6)) as f:
    input = f.read()
assert solve_part_1(parse_input(input)) == 5177
