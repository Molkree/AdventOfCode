from collections import deque

from utils import get_input_path

with open(get_input_path(12)) as f:
    grid = [list(line.strip()) for line in f]

start = 0, 0
end = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = i, j
            grid[i][j] = "a"
        elif grid[i][j] == "E":
            end = i, j
            grid[i][j] = "z"

queue: deque[tuple[tuple[int, int], list[tuple[int, int]]]] = deque()
queue.append((start, []))
visited: set[tuple[int, int]] = {start}
path: list[tuple[int, int]] = []
while queue:
    (row, col), path = queue.popleft()
    if (row, col) == end:
        print(len(path))
        break
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

assert len(path) == 412
