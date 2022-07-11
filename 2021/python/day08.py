from utils import get_input_path

with open(get_input_path(8)) as f:
    lines = f.readlines()

# Part 1
all_outputs = [line.split(" | ")[1].split() for line in lines]
flat_outputs = [output for outputs in all_outputs for output in outputs]
unique_numbers = sum(len(output) in (2, 3, 4, 7) for output in flat_outputs)
assert unique_numbers == 397


# Part 2
def get_output_value(entry: str) -> int:
    signals, outputs = map(str.split, entry.split(" | "))

    def deduce_numbers() -> dict[str, int]:
        one = four = seven = eight = set[str]()
        for signal in signals:
            match len(signal):
                case 2:
                    one = set(signal)
                case 3:
                    seven = set(signal)
                case 4:
                    four = set(signal)
                case 7:
                    eight = set(signal)
                case _:
                    pass
        six = set[str]()
        for signal in signals:
            if len(signal) == 6 and eight - seven < set(signal):
                six = set(signal)
                break
        c_line = eight - six
        five = set[str]()
        for signal in signals:
            if len(signal) == 5 and c_line.isdisjoint(signal):
                five = set(signal)
                break
        e_line = six - five
        zero = two = three = nine = set[str]()
        for signal in signals:
            if len(signal) == 6 and set(signal) != six:
                if e_line < set(signal):
                    zero = set(signal)
                else:
                    nine = set(signal)
            elif len(signal) == 5:
                if e_line < set(signal):
                    two = set(signal)
                elif set(signal) != five:
                    three = set(signal)
        return {
            "".join(sorted(set_num)): int_num
            for int_num, set_num in enumerate(
                (zero, one, two, three, four, five, six, seven, eight, nine)
            )
        }

    str2int = deduce_numbers()
    output_value = str2int["".join(sorted(outputs[0]))]
    for output in outputs[1:]:
        output_value = output_value * 10 + str2int["".join(sorted(output))]
    return output_value


assert sum(get_output_value(entry) for entry in lines) == 1027422
