from collections.abc import Sequence
from typing import Literal

from utils import get_input_path


def count_word(
    grid: Sequence[str],
    row: int,
    col: int,
    word: str,
    direction: tuple[Literal[-1, 0, 1], Literal[-1, 0, 1]] | None = None,
) -> int:
    height = len(grid)
    width = len(grid[0])
    if grid[row][col] != word[0]:
        return 0
    if len(word) == 1:
        return 1
    if direction is not None:
        row += direction[0]
        col += direction[1]
        if row < 0 or row >= height or col < 0 or col >= width:
            return 0
        return count_word(grid, row, col, word[1:], direction)
    count = 0
    if row > 0:
        count += count_word(grid, row - 1, col, word[1:], direction=(-1, 0))
        if col > 0:
            count += count_word(grid, row - 1, col - 1, word[1:], direction=(-1, -1))
        if col < width - 1:
            count += count_word(grid, row - 1, col + 1, word[1:], direction=(-1, 1))
    if row < height - 1:
        count += count_word(grid, row + 1, col, word[1:], direction=(1, 0))
        if col > 0:
            count += count_word(grid, row + 1, col - 1, word[1:], direction=(1, -1))
        if col < width - 1:
            count += count_word(grid, row + 1, col + 1, word[1:], direction=(1, 1))
    if col > 0:
        count += count_word(grid, row, col - 1, word[1:], direction=(0, -1))
    if col < width - 1:
        count += count_word(grid, row, col + 1, word[1:], direction=(0, 1))
    return count


def count_all_words(grid: Sequence[str]) -> int:
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            count += count_word(grid, row, col, "XMAS")
    return count


def check_x_mas(grid: Sequence[str], row: int, col: int) -> bool:
    return grid[row][col] == "A" and (
        # M.M
        # .A.
        # S.S
        grid[row - 1][col - 1] == "M"
        and grid[row - 1][col + 1] == "M"
        and grid[row + 1][col - 1] == "S"
        and grid[row + 1][col + 1] == "S"
        # S.S
        # .A.
        # M.M
        or grid[row - 1][col - 1] == "S"
        and grid[row - 1][col + 1] == "S"
        and grid[row + 1][col - 1] == "M"
        and grid[row + 1][col + 1] == "M"
        # M.S
        # .A.
        # M.S
        or grid[row - 1][col - 1] == "M"
        and grid[row - 1][col + 1] == "S"
        and grid[row + 1][col - 1] == "M"
        and grid[row + 1][col + 1] == "S"
        # S.M
        # .A.
        # S.M
        or grid[row - 1][col - 1] == "S"
        and grid[row - 1][col + 1] == "M"
        and grid[row + 1][col - 1] == "S"
        and grid[row + 1][col + 1] == "M"
    )


def count_x_mases(grid: Sequence[str]) -> int:
    count = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            count += int(check_x_mas(grid, row, col))
    return count


example_1 = """..X...
.SAMX.
.A..A.
XMAS.S
.X....""".splitlines()
assert count_all_words(example_1) == 4

example_2 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()
assert count_all_words(example_2) == 18
assert count_x_mases(example_2) == 9

with open(get_input_path(4)) as f:
    input = f.read().splitlines()

assert count_all_words(input) == 2583
assert count_x_mases(input) == 1978
