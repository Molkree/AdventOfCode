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


example_1 = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""
assert count_all_words(example_1.splitlines()) == 4

example_2 = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""
assert count_all_words(example_2.splitlines()) == 18

with open(get_input_path(4)) as f:
    input_str = f.read()

assert count_all_words(input_str.splitlines()) == 2583
