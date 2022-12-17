import re

from utils import get_input_path


def add_interval(
    intervals: list[tuple[int, int]], start: int, end: int
) -> list[tuple[int, int]]:
    """Add interval to list of intervals, merging overlapping intervals."""
    intervals.append((start, end))
    intervals.sort()
    merged_intervals: list[tuple[int, int]] = []
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = (
                merged_intervals[-1][0],
                max(merged_intervals[-1][1], interval[1]),
            )
            if len(merged_intervals) > 1 and (
                merged_intervals[-2][1] + 1 == merged_intervals[-1][0]
            ):
                merged_intervals[-2] = (
                    merged_intervals[-2][0],
                    merged_intervals[-1][1],
                )
                merged_intervals.pop()
    return merged_intervals


def remove_point(intervals: list[tuple[int, int]], x: int) -> list[tuple[int, int]]:
    """Remove point from list of intervals, splitting intervals if necessary."""
    for i, (start, end) in enumerate(intervals):
        if start <= x <= end:
            if start == end:
                del intervals[i]
            elif start == x:
                intervals[i] = (start + 1, end)
            elif end == x:
                intervals[i] = (start, end - 1)
            else:
                intervals[i] = (start, x - 1)
                intervals.insert(i + 1, (x + 1, end))
            break
    return intervals


sensors: list[tuple[int, int]] = []
beacons: list[tuple[int, int]] = []
radiuses: list[int] = []
with open(get_input_path(15)) as f:
    for line in f:
        match = re.search(
            "Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line
        )
        if match:
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, match.groups())
            beacons.append((beacon_x, beacon_y))
            sensors.append((sensor_x, sensor_y))
            radiuses.append(abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y))

PART_1_TARGET = 2000000
intervals: list[tuple[int, int]] = []
for (sensor_x, sensor_y), (beacon_x, beacon_y), radius in zip(
    sensors, beacons, radiuses
):
    distance = abs(PART_1_TARGET - sensor_y)
    if distance <= radius:
        margin = radius - distance
        intervals = add_interval(intervals, sensor_x - margin, sensor_x + margin)
for beacon_x, beacon_y in beacons:
    if beacon_y == PART_1_TARGET:
        intervals = remove_point(intervals, beacon_x)
bad_positions = sum(end - start + 1 for start, end in intervals)
assert bad_positions == 5335787

FLOOR = 0
CEIL = 4000000
distress_y, distress_x = 0, 0
for y in range(FLOOR, CEIL + 1):
    intervals = []
    for (sensor_x, sensor_y), (beacon_x, beacon_y), radius in zip(
        sensors, beacons, radiuses
    ):
        distance = abs(y - sensor_y)
        if distance <= radius:
            margin = radius - distance
            left, right = sensor_x - margin, sensor_x + margin
            if left > CEIL or right < FLOOR:
                continue
            intervals = add_interval(intervals, max(left, FLOOR), min(right, CEIL))
    bad_positions = sum(end - start + 1 for start, end in intervals)
    if bad_positions < CEIL - FLOOR + 1:
        distress_x = intervals[0][1] + 1
        distress_y = y
        break

tuning_frequency = distress_x * 4000000 + distress_y
assert tuning_frequency == 13673971349056
