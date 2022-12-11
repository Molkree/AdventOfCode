from collections.abc import Callable

from utils import get_input_path


class Monkey:
    @staticmethod
    def get_bored(item: int) -> int:
        return item // 3

    def __init__(self, note: str) -> None:
        _, items_str, op_str, test_str, true_str, false_str = note.splitlines()

        self.items = list(map(int, items_str.split(": ")[1].split(", ")))

        op_dict: dict[str, Callable[[int, int], int]] = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
        }
        op_words = op_str.split()
        op_type, op_arg = op_dict[op_words[4]], op_words[5]
        if op_arg.isdigit():
            self.operation: Callable[[int], int] = lambda x: op_type(x, int(op_arg))
        else:
            self.operation = lambda x: op_type(x, x)

        self.test: Callable[[int], bool] = lambda x: x % int(test_str.split()[-1]) == 0
        self.true_path = int(true_str.split()[-1])
        self.false_path = int(false_str.split()[-1])
        self.inspection_count = 0

    def next_monkey(self, item: int) -> int:
        self.inspection_count += 1
        if self.test(item):
            return self.true_path
        return self.false_path

    def gen_new_item(self, item: int) -> int:
        return Monkey.get_bored(self.operation(item))


with open(get_input_path(11)) as f:
    monkey_strings = f.read().split("\n\n")

monkeys = [Monkey(monkey_str) for monkey_str in monkey_strings]
for i in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            new_item = monkey.gen_new_item(item)
            monkeys[monkey.next_monkey(new_item)].items.append(new_item)
        monkey.items = []

inspection_counts = sorted(monkey.inspection_count for monkey in monkeys)
monkey_business = inspection_counts[-2] * inspection_counts[-1]
assert monkey_business == 54054
