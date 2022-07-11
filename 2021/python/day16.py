import operator
from collections.abc import Callable
from functools import partial
from math import prod
from typing import Literal

from utils import get_input_path

with open(get_input_path(16)) as f:
    hex = f.readline().rstrip()

bin_str = ""
for hex_digit in hex:
    bin_str += bin(int(hex_digit, 16))[2:].zfill(4)
version_sum = 0

comp: Callable[[Callable[[int, int], bool], list[int]], Literal[0, 1]] = (
    lambda op, p: 1 if op(*p) else 0
)
ops = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: partial(comp, operator.gt),
    6: partial(comp, operator.lt),
    7: partial(comp, operator.eq),
}


def parse_packet(bin_str: str) -> tuple[int, int]:
    global version_sum
    version = int(bin_str[:3], 2)
    version_sum += version
    type_id = int(bin_str[3:6], 2)

    if type_id == 4:
        groups_ind = 6
        bin_literal = ""
        while bin_str[groups_ind] == "1":
            bin_literal += bin_str[groups_ind + 1 : groups_ind + 5]
            groups_ind += 5
        bin_literal += bin_str[groups_ind + 1 : groups_ind + 5]
        value = int(bin_literal, 2)
        return groups_ind + 5, value
    else:
        length_type_id = bin_str[6]
        subpackets_start = 7
        sub_values = list[int]()
        if length_type_id == "0":
            subpackets_start += 15
            total_bit_length = int(bin_str[7:subpackets_start], 2)
            next_packet_start = subpackets_start
            while subpackets_start + total_bit_length > next_packet_start:
                next_len, next_value = parse_packet(bin_str[next_packet_start:])
                next_packet_start += next_len
                sub_values.append(next_value)
        else:
            subpackets_start += 11
            subpackets_count = int(bin_str[7:subpackets_start], 2)
            next_packet_start = subpackets_start
            for _ in range(subpackets_count):
                next_len, next_value = parse_packet(bin_str[next_packet_start:])
                next_packet_start += next_len
                sub_values.append(next_value)
        return next_packet_start, ops[type_id](sub_values)


_, value = parse_packet(bin_str)
assert version_sum == 1007
assert value == 834151779165
