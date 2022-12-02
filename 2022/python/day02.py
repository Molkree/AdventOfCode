from utils import get_input_path

outcomes_1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
outcomes_2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}
with open(get_input_path(2)) as f:
    matches = list(map(str.rstrip, f.readlines()))
score_1 = sum(outcomes_1[match] for match in matches)
score_2 = sum(outcomes_2[match] for match in matches)
assert score_1 == 11449
assert score_2 == 13187
