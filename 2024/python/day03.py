from re import findall

from utils import get_input_path


def find_multiplications(input: str) -> list[tuple[str, str]]:
    """
    Find all instructions like mul(X,Y), where X and Y are each 1-3 digit numbers
    """
    return findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)


def find_total_sum(input: str) -> int:
    return sum(int(x) * int(y) for x, y in find_multiplications(input))


example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
assert find_total_sum(example) == 161

with open(get_input_path(3)) as f:
    input_str = f.read()
assert find_total_sum(input_str) == 178886550
