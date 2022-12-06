from utils import get_input_path

with open(get_input_path(6)) as f:
    datastream = f.readline().rstrip()
start_packet_len = 4
start_message_len = 14
start_packet_pos = 0
for i in range(len(datastream) - start_packet_len + 1):
    start_packet = datastream[i : i + start_packet_len]
    if not start_packet_pos and len(set(start_packet)) == start_packet_len:
        start_packet_pos = i + start_packet_len
        assert start_packet_pos == 1531
    # no index error cause we are guaranteed to have message marker after packet marker
    start_message = datastream[i : i + start_message_len]
    if len(set(start_message)) == start_message_len:
        start_message_pos = i + start_message_len
        assert start_message_pos == 2518
        break
