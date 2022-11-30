from utils import get_input_path

day = 4
print(f"Day {day:02}")


def is_valid_passport(fields: str) -> bool:
    key_value_pairs = {
        key: value
        for (key, value) in (
            key_value.split(":") for key_value in fields.replace(" ", "\n").split()
        )
    }

    return (
        "byr" in key_value_pairs
        and key_value_pairs["byr"].isdigit()
        and 1920 <= int(key_value_pairs["byr"]) <= 2002
        and "iyr" in key_value_pairs
        and key_value_pairs["iyr"].isdigit()
        and 2010 <= int(key_value_pairs["iyr"]) <= 2020
        and "eyr" in key_value_pairs
        and key_value_pairs["eyr"].isdigit()
        and 2020 <= int(key_value_pairs["eyr"]) <= 2030
        and "hgt" in key_value_pairs
        and (
            key_value_pairs["hgt"].endswith("cm")
            and 150 <= int(key_value_pairs["hgt"][:-2]) <= 193
            or key_value_pairs["hgt"].endswith("in")
            and 59 <= int(key_value_pairs["hgt"][:-2]) <= 76
        )
        and "hcl" in key_value_pairs
        and key_value_pairs["hcl"].startswith("#")
        and len(key_value_pairs["hcl"]) == 7
        and all("0" <= c <= "9" or "a" <= c <= "z" for c in key_value_pairs["hcl"][1:])
        and "ecl" in key_value_pairs
        and key_value_pairs["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        and "pid" in key_value_pairs
        and len(key_value_pairs["pid"]) == 9
        and all("0" <= c <= "9" for c in key_value_pairs["pid"])
    )


with open(get_input_path(day)) as f:
    passports = f.read().split("\n\n")
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports_1 = sum(
        all(field in passport for field in required_fields) for passport in passports
    )
    valid_passports_2 = sum(is_valid_passport(passport) for passport in passports)

print(f"Part 1: {valid_passports_1}")
assert valid_passports_1 == 208
print(f"Part 2: {valid_passports_2}")
assert valid_passports_2 == 167
