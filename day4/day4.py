file = open('input.txt')
lines = [l.strip() for l in file.readlines()]
file.close()


def parse_range(range_str):
    splitted = range_str.split('-')
    return (int(splitted[0]), int(splitted[1]))


pairs = []
for line in lines:
    splitted = line.split(',')
    pairs.append((parse_range(splitted[0]), parse_range(splitted[1])))


def one_fully_contains_other(pair):
    lo1 = pair[0][0]
    lo2 = pair[1][0]
    hi1 = pair[0][1]
    hi2 = pair[1][1]

    return (lo1 <= lo2 and hi1 >= hi2) or (lo2 <= lo1 and hi2 >= hi1) 


def has_overlap(pair):
    lo1 = pair[0][0]
    lo2 = pair[1][0]
    hi1 = pair[0][1]
    hi2 = pair[1][1]

    return hi1 >= lo2 and hi2 >= lo1
    

def part1():
    return len([p for p in pairs if one_fully_contains_other(p)])


def part2():
    return len([p for p in pairs if has_overlap(p)])


print(part1())
print(part2())
