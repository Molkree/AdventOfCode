import functools
from enum import IntEnum
from typing import Union

from utils import get_input_path

with open(get_input_path(13)) as f:
    str_pairs = map(str.splitlines, f.read().split("\n\n"))
Packet = list[Union[int, "Packet"]]


def parse_packet(str_packet: str) -> Packet:
    packet = Packet()
    stack = [packet]
    for index, char in enumerate(str_packet[1:]):
        current = stack[-1]
        if char == "]":
            stack.pop()
        elif char.isdigit():
            if str_packet[index].isdigit():
                current[-1] = current[-1] * 10 + int(char)  # type: ignore # we know that last value is int
            else:
                current.append(int(char))
        elif char == "[":
            current.append(Packet())
            stack.append(current[-1])  # type: ignore # we know that current is a list
    return packet


class PacketOrder(IntEnum):
    LESS = -1
    EQUAL = 0
    GREATER = 1


def get_packet_order(left: Packet, right: Packet) -> PacketOrder:
    for index, left_value in enumerate(left):
        if index >= len(right):
            return PacketOrder.GREATER
        right_value = right[index]
        if isinstance(left_value, int) and isinstance(right_value, int):
            if left_value < right_value:
                return PacketOrder.LESS
            elif left_value > right_value:
                return PacketOrder.GREATER
        elif isinstance(left_value, list) and isinstance(right_value, list):
            order = get_packet_order(left_value, right_value)
            if order != PacketOrder.EQUAL:
                return order
        else:
            if isinstance(left_value, int):
                # both pyright and mypy can't figure out that right_value is a list
                order = get_packet_order([left_value], right_value)  # type: ignore
            else:
                order = get_packet_order(left_value, [right_value])
            if order != PacketOrder.EQUAL:
                return order
    if len(left) < len(right):
        return PacketOrder.LESS
    return PacketOrder.EQUAL


good_pairs: list[int] = []
packets: list[Packet] = []
for index, pair in enumerate(str_pairs):
    left, right = map(parse_packet, pair)
    packets.extend([left, right])
    if get_packet_order(left, right) != PacketOrder.GREATER:
        good_pairs.append(index + 1)
assert sum(good_pairs) == 5208

divider_packet_1, divider_packet_2 = parse_packet("[[2]]"), parse_packet("[[6]]")
packets.extend([divider_packet_1, divider_packet_2])
packets.sort(key=functools.cmp_to_key(get_packet_order))
divider_index_1, divider_index_2 = (
    packets.index(divider_packet_1) + 1,
    packets.index(divider_packet_2) + 1,
)
assert divider_index_1 * divider_index_2 == 25792
