from utils import get_input_path

with open(get_input_path(6)) as f:
    datastream = f.readline().rstrip()
start_marker_len = 4
for i in range(len(datastream) - start_marker_len + 1):
    start_marker = datastream[i : i + start_marker_len]
    if len(set(start_marker)) == start_marker_len:
        start_marker_pos = i + start_marker_len
        assert start_marker_pos == 1531
        break
