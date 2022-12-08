from utils import get_input_path

with open(get_input_path(8)) as f:
    grid = f.read().splitlines()

visible_count = len(grid) * 2 + len(grid[0]) * 2 - 4
inner_visible: set[tuple[int, int]] = set()


def check_tree(
    grid: list[str],
    row: int,
    col: int,
    visible_count: int,
    inner_visible: set[tuple[int, int]],
    tallest_tree: str,
) -> tuple[int, set[tuple[int, int]], str]:
    if grid[row][col] > tallest_tree:
        if (row, col) not in inner_visible:
            visible_count += 1
            inner_visible.add((row, col))
        tallest_tree = grid[row][col]
    return visible_count, inner_visible, tallest_tree


for row in range(1, len(grid) - 1):
    tallest_tree = grid[row][0]
    for col in range(1, len(grid[row]) - 1):
        visible_count, inner_visible, tallest_tree = check_tree(
            grid, row, col, visible_count, inner_visible, tallest_tree
        )
    tallest_tree = grid[row][-1]
    for col in range(len(grid[row]) - 2, 0, -1):
        visible_count, inner_visible, tallest_tree = check_tree(
            grid, row, col, visible_count, inner_visible, tallest_tree
        )
for col in range(1, len(grid[0]) - 1):
    tallest_tree = grid[0][col]
    for row in range(1, len(grid) - 1):
        visible_count, inner_visible, tallest_tree = check_tree(
            grid, row, col, visible_count, inner_visible, tallest_tree
        )
    tallest_tree = grid[-1][col]
    for row in range(len(grid) - 2, 0, -1):
        visible_count, inner_visible, tallest_tree = check_tree(
            grid, row, col, visible_count, inner_visible, tallest_tree
        )
print(visible_count)
