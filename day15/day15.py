from tqdm import tqdm

sensors = dict()

file = open('input.txt')
for line in file:
    just_nums = [xy[2:] for xy in line.split() if 'x' in xy or 'y' in xy] 
    for i in range(3):
        just_nums[i] = int(just_nums[i][:-1])
    sx = just_nums[0]
    sy = just_nums[1]
    bx = just_nums[2]
    by = int(just_nums[3])

    sensors[(sx, sy)] = (bx, by)
file.close()    


def line_coverage(sensor, beacon, line_no):
    dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    dist_to_line = abs(line_no - sensor[1])
    dist_left = dist - dist_to_line

    if (dist_left) > 0:
        lo = sensor[0] - dist_left
        hi = sensor[0] + 1 + dist_left 

        return (lo, hi)
    else:
        return None


def part1(row):
    coverages = []

    for s, b in sensors.items():
        coverage = line_coverage(s, b, row)
        if coverage is not None:
            coverages.append(coverage)

    coverages.sort()

    sum = coverages[0][1] - coverages[0][0]
    prev_hi = coverages[0][1]
    for lo, hi in coverages[1:]:
        if lo < prev_hi:
            lo = prev_hi
            if (hi < prev_hi):
                continue
        sum += hi - lo 
        prev_hi = hi

    return sum - 1



def part2(limit):
    limit += 1

    for row in tqdm(range(limit)):
        coverages = []
        for s, b in sensors.items():
            coverage = line_coverage(s, b, row)
            if coverage is not None:
                coverages.append(coverage)

        coverages.sort()

        prev_hi = coverages[0][1]
        for lo, hi in coverages[1:]:
            if lo < 0:
                if hi <= 0:
                    continue
                else:
                    lo = 0
            if hi > limit:
                if lo >= limit:
                    continue
                else:
                    hi = limit

            if lo < prev_hi:
                lo = prev_hi
                if (hi < prev_hi):
                    continue
            elif lo >= prev_hi:
                return prev_hi * 4000000 + row

            prev_hi = hi


print(part1(2000000))
print(part2(4000000))
