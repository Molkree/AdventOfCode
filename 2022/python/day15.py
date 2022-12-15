import re

from utils import get_input_path

TARGET_ROW = 2000000

beacons: list[tuple[int, int]] = []
scanned_columns: set[int] = set()
with open(get_input_path(15)) as f:
    for line in f:
        match = re.search(
            "Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line
        )
        if match:
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, match.groups())
            radius = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            distance = abs(TARGET_ROW - sensor_y)
            if distance > radius:
                continue
            beacons.append((beacon_x, beacon_y))
            margin = radius - distance
            for x in range(sensor_x - margin, sensor_x + margin + 1):
                scanned_columns.add(x)
scanned_columns -= {x for x, y in beacons if y == TARGET_ROW}
assert len(scanned_columns) == 5335787
