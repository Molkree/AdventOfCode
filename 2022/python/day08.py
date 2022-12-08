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
assert visible_count == 1690

highest_scenic_score = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        tree = grid[row][col]
        up = 0
        for up_row in range(row - 1, -1, -1):
            up += 1
            if grid[up_row][col] >= tree:
                break
        down = 0
        for down_row in range(row + 1, len(grid)):
            down += 1
            if grid[down_row][col] >= tree:
                break
        left = 0
        for left_col in range(col - 1, -1, -1):
            left += 1
            if grid[row][left_col] >= tree:
                break
        right = 0
        for right_col in range(col + 1, len(grid[row])):
            right += 1
            if grid[row][right_col] >= tree:
                break
        highest_scenic_score = max(highest_scenic_score, up * down * left * right)
assert highest_scenic_score == 535680
