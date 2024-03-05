def compare(v1, v2):
    """Returns -1, 0 or 1 if v1 is less than, equal to or more than v2"""

    # if one is list and other is not, put other value into list
    if not isinstance(v1, list):
        if isinstance(v2, list):
            v1 = [v1]
        else:  # both are int
            if v1 < v2:
                return -1
            elif v1 == v2:
                return 0
            else:
                return 1
    elif not isinstance(v2, list):
        v2 = [v2]

    # check if one of the lists is empty
    if len(v1) == 0:
        if len(v2) == 0:
            return 0
        else:
            return -1
    elif len(v2) == 0:
        return 1

    # both are now known to be non-empty lists
    for i in range(max(len(v1), len(v2))):
        if i >= len(v1):
            return -1
        elif i >= len(v2):
            return 1

        val1 = v1[i]
        val2 = v2[i]

        comparison = compare(val1, val2)
        if comparison != 0:
            return comparison

    return 0


def parse_input(file_path):
    file = open(file_path)
    lines = [line.strip() for line in file.readlines()]
    file.close()

    pairs = []
    row = 0
    while row < len(lines):
        pairs.append((eval(lines[row]), eval(lines[row + 1])))
        row += 3

    return pairs


def quicksort(signals):
    if len(signals) == 0:
        return []

    pivot = signals.pop(len(signals) // 2)
    lt = quicksort([s for s in signals if compare(s, pivot) <= 0])
    gt = quicksort([s for s in signals if compare(s, pivot) == 1])

    return lt + [pivot] + gt


####################
# program start
####################

pairs = parse_input("input.txt")


def part1():
    sum = 0
    for i, pair in enumerate(pairs):
        if compare(pair[0], pair[1]) < 0:
            sum += i + 1

    return sum


def part2():
    signals = [signal for pair in pairs for signal in pair] + [[[2]], [[6]]]
    sorted = quicksort(signals)

    key = 1
    for i, signal in enumerate(sorted):
        if signal == [[2]] or signal == [[6]]:
            key *= i + 1

    return key


print(part1())
print(part2())
