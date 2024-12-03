from re import findall, search

from utils import get_input_path


def find_multiplications(input: str) -> list[tuple[str, str]]:
    """
    Find all instructions like mul(X,Y), where X and Y are each 1-3 digit numbers
    """
    return findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)


def find_all_instructions(input: str) -> list[str]:
    """
    Find all instructions like mul(X,Y), don't() or do()
    """
    return findall(r"(?:mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\))", input)


def find_total_sum(input: str) -> int:
    return sum(int(x) * int(y) for x, y in find_multiplications(input))


def find_enabled_sum(input: str) -> int:
    instructions = find_all_instructions(input)
    enabled = True
    total = 0
    for instruction in instructions:
        if "do()" in instruction:
            enabled = True
        elif "don't()" in instruction:
            enabled = False
        elif "mul" in instruction:
            if enabled:
                match = search(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)
                if not match:
                    raise ValueError(f"Could not multiplication {instruction}")
                total += int(match.group(1)) * int(match.group(2))
    return total


example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
assert find_total_sum(example) == 161
example_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
assert find_enabled_sum(example_2) == 48

with open(get_input_path(3)) as f:
    input_str = f.read()
assert find_total_sum(input_str) == 178886550
assert find_enabled_sum(input_str) == 87163705
