from utils import get_input_path

with open(get_input_path(10)) as f:
    lines = f.readlines()
paren_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
paren_error_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
paren_autocomplete_scores = {"(": 1, "[": 2, "{": 3, "<": 4}
error_score = 0
autocomple_scores = list[int]()
for line in lines:
    line = line.rstrip()
    stack = list[str]()
    for paren in line:
        if paren in paren_pairs:
            stack.append(paren)
        else:
            opening_paren = stack.pop()
            if paren != paren_pairs[opening_paren]:
                error_score += paren_error_scores[paren]
                stack.clear()
                break
    if stack:
        autocomple_score = 0
        while stack:
            paren = stack.pop()
            autocomple_score = autocomple_score * 5 + paren_autocomplete_scores[paren]
        autocomple_scores.append(autocomple_score)
assert error_score == 362271
assert sorted(autocomple_scores)[len(autocomple_scores) // 2] == 1698395182
