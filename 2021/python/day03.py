from utils import get_input_path

with open(get_input_path(3)) as f:
    lines = f.readlines()

# Part 1
count_ones = [int(bit) for bit in lines[0].rstrip()]
for num in lines[1:]:
    for i in range(len(num.rstrip())):
        count_ones[i] += int(num[i])
gamma = "".join("1" if bit >= len(lines) // 2 else "0" for bit in count_ones)
epsilon = "".join("1" if bit == "0" else "0" for bit in gamma)
gamma = "0b" + gamma
epsilon = "0b" + epsilon
assert int(gamma, 2) * int(epsilon, 2) == 2583164


# Part 2
def get_rating(starting_bit: str, oxygen: bool = True) -> int:
    bit = starting_bit
    bit_ind = 0
    candidates = [num for num in lines if num[bit_ind] == bit]
    while len(candidates) > 1:
        count = 0
        bit_ind += 1
        for candidate in candidates:
            count += int(candidate[bit_ind])
        bit = "1" if count >= len(candidates) / 2 else "0"
        if not oxygen:
            bit = "0" if bit == "1" else "1"
        candidates = [num for num in candidates if num[bit_ind] == bit]
    return int("0b" + candidates[0], 2)


oxygen = get_rating(gamma[2])
co2 = get_rating(epsilon[2], oxygen=False)
assert oxygen * co2 == 2784375
