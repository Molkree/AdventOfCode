from utils import get_input_path

with open(get_input_path(16)) as f:
    hex = f.readline().rstrip()

bin_str = ""
for hex_digit in hex:
    bin_str += bin(int(hex_digit, 16))[2:].zfill(4)
version_sum = 0


def parse_packet(bin_str: str) -> int:
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
        # dec_literal = int(bin_literal, 2)
        return groups_ind + 5
    else:
        length_type_id = bin_str[6]
        subpackets_start = 7
        if length_type_id == "0":
            subpackets_start += 15
            total_bit_length = int(bin_str[7:subpackets_start], 2)
            next_packet_start = subpackets_start
            while subpackets_start + total_bit_length > next_packet_start:
                next_packet_start += parse_packet(bin_str[next_packet_start:])
        else:
            subpackets_start += 11
            subpackets_count = int(bin_str[7:subpackets_start], 2)
            next_packet_start = subpackets_start
            for _ in range(subpackets_count):
                next_packet_start += parse_packet(bin_str[next_packet_start:])
        return next_packet_start


packet_len = parse_packet(bin_str)
assert version_sum == 1007
