from utils import get_input_path

with open(get_input_path(4)) as f:
    pairs = [
        [tuple(map(int, elf.split("-"))) for elf in line.split(sep=",")]
        for line in f.readlines()
    ]

fuly_contained = 0
overlapping = 0
for pair in pairs:
    (start_1, end_1), (start_2, end_2) = sorted(pair, key=lambda x: (x[0], -x[1]))
    if start_2 <= end_1:
        overlapping += 1
        if end_2 <= end_1:
            fuly_contained += 1
assert fuly_contained == 644
assert overlapping == 926
