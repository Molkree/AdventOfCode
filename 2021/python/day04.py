from collections import defaultdict

from utils import get_input_path

with open(get_input_path(4)) as f:
    lines = f.readlines()

    nums = lines[0].split(",")
    num2row: defaultdict[str, set[int]] = defaultdict(set[int])
    num2column: defaultdict[str, set[int]] = defaultdict(set[int])
    rows: defaultdict[int, set[str]] = defaultdict(set[str])
    columns: defaultdict[int, set[str]] = defaultdict(set[str])
    row_ind = 0
    column_ind = 0
    line_ind = 2
    while line_ind < len(lines):
        for i in range(5):
            board_nums = lines[line_ind + i].split()
            for j in range(5):
                num = board_nums[j]
                num2row[num].add(row_ind + i)
                num2column[num].add(column_ind + j)
                rows[row_ind + i].add(num)
                columns[column_ind + j].add(num)
        line_ind += 6
        row_ind += 5
        column_ind += 5

    def get_score(winning_index: int, winning_num: int) -> int:
        start_ind = winning_index // 5 * 5
        winning_sum = 0
        for i in range(5):
            winning_sum += sum(int(num) for num in rows[start_ind + i])
        return winning_sum * winning_num

    boards_count = len(rows) // 5
    winning_boards: set[int] = set()
    first_score = None
    last_score = None
    for num in nums:
        for row in num2row[num]:
            rows[row].remove(num)
            if len(rows[row]) == 0:
                winning_index = row
                winning_num = int(num)
                if first_score is None:
                    first_score = get_score(winning_index, winning_num)
                winning_boards.add(winning_index // 5)
                if boards_count == len(winning_boards) and last_score is None:
                    last_score = get_score(winning_index, winning_num)
        for column in num2column[num]:
            columns[column].remove(num)
            if len(columns[column]) == 0:
                winning_index = column
                winning_num = int(num)
                if first_score is None:
                    first_score = get_score(winning_index, winning_num)
                winning_boards.add(winning_index // 5)
                if boards_count == len(winning_boards) and last_score is None:
                    last_score = get_score(winning_index, winning_num)

    assert first_score == 60368
    assert last_score == 17435
