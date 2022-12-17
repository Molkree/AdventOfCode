import re

from utils import get_input_path


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


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
            radiuses.append(manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y))

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

# The only place distress beacon can be is where the acute and obtuse outer border
# diagonals of different sensors intersect.
# Linear equation: y = mx + b
# y = -x + sensor_x + sensor_y + radius + 1; acute diagonal
# y = -x + sensor_x + sensor_y - radius - 1; acute diagonal
# y = x - sensor_x + sensor_y + radius + 1; obtuse diagonal
# y = x - sensor_x + sensor_y - radius - 1; obtuse diagonal
# Let's find the intersection of the two lines.
# Let obtuse equation be y = x + a and acute equation be y = -x + b.
# Then intersection is (b - a) // 2, (b + a) // 2.
acute_coefs: set[int] = set()
obtuse_coefs: set[int] = set()
for (x, y), radius in zip(sensors, radiuses):
    acute_coefs.add(x + y + radius + 1)
    acute_coefs.add(x + y - radius - 1)
    obtuse_coefs.add(y - x + radius + 1)
    obtuse_coefs.add(y - x - radius - 1)
FLOOR = 0
CEIL = 4000000
distress_x, distress_y = 0, 0
for obtuse_coef in obtuse_coefs:
    for acute_coef in acute_coefs:
        intersection = (acute_coef - obtuse_coef) // 2, (acute_coef + obtuse_coef) // 2
        if (
            FLOOR <= intersection[0] <= CEIL
            and FLOOR <= intersection[1] <= CEIL
            and all(
                manhattan_distance(*intersection, *sensor) > radius
                for sensor, radius in zip(sensors, radiuses)
            )
        ):
            distress_x, distress_y = intersection
            break

tuning_frequency = distress_x * 4000000 + distress_y
assert tuning_frequency == 13673971349056
