from collections import deque

from utils import get_input_path

with open(get_input_path(12)) as f:
    grid = [list(line.strip()) for line in f]

start = 0, 0
end = 0, 0
potential_starts: list[tuple[int, int]] = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = i, j
            grid[i][j] = "a"
            potential_starts.append(start)
        elif grid[i][j] == "E":
            end = i, j
            grid[i][j] = "z"
        elif grid[i][j] == "a":
            potential_starts.append((i, j))


def get_path(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> list[tuple[int, int]] | None:
    queue: deque[tuple[tuple[int, int], list[tuple[int, int]]]] = deque()
    queue.append((start, []))
    visited: set[tuple[int, int]] = {start}
    while queue:
        (row, col), path = queue.popleft()
        if (row, col) == end:
            return path
        for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_row, new_col = row + i, col + j
            if (
                not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]))
                or (new_row, new_col) in visited
            ):
                continue
            height_diff = ord(grid[new_row][new_col]) - ord(grid[row][col])
            if height_diff < 2:
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
                visited.add((new_row, new_col))
    return None


path = get_path(grid, start, end)
assert path and len(path) == 412

shortest_trail = len(path)
for start in potential_starts:
    path = get_path(grid, start, end)
    if path and len(path) < shortest_trail:
        shortest_trail = len(path)
assert shortest_trail == 402
