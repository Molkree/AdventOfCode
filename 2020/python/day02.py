import re

from utils import get_input_path

day = 2
print(f"Day {day:02}")
with open(get_input_path(day)) as f:
    valid_passwords_1 = 0
    valid_passwords_2 = 0
    for line in f:
        m = re.match(r"(?P<min>.+)-(?P<max>.+) (?P<char>.+): (?P<password>.+)", line)
        assert m
        min, max, char, password = m.groups()
        min = int(min)
        max = int(max)
        count = 0
        for item in password:
            if item == char:
                count += 1
        if min <= count and count <= max:
            valid_passwords_1 += 1
        if (password[min - 1] == char or password[max - 1] == char) and password[
            min - 1
        ] != password[max - 1]:
            valid_passwords_2 += 1
    print("Part 1:", valid_passwords_1)
    print("Part 2:", valid_passwords_2)
