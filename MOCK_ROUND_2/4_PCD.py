import math
def normalize(angle):
    return angle % 360.0

def perfect_cover_drive(n, r, fielders):
    intervals = []

    for x, y in fielders:
        distance = math.hypot(x, y)
        if distance <= r:
            return 0.000000

        center_angle = math.degrees(math.atan2(y, x))
        angle_offset = math.degrees(math.asin(r / distance))
        start_angle = normalize(center_angle - angle_offset)
        end_angle = normalize(center_angle + angle_offset)

        if start_angle > end_angle:
            intervals.append((start_angle, 360.0))
            intervals.append((0.0, end_angle))
        else:
            intervals.append((start_angle, end_angle))
    intervals.sort()

    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(list(interval))
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    max_gap = 0.0
    for i in range(len(merged)):
        end = merged[i][1]
        next_start = merged[(i + 1) % len(merged)][0]
        gap = (next_start + 360.0 if i == len(merged) - 1 else next_start) - end
        max_gap = max(max_gap, gap)
    return round(max_gap, 6)

n, r = input().split()
n = int(n)
r = float(r)
fielders = [tuple(map(float, input().split())) for _ in range(n)]
result = perfect_cover_drive(n, r, fielders)
print(f"{result:.6f}")
