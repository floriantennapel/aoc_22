input = open('input.txt')
lines = input.readlines()
input.close()


def get_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def part1():
    sum = 0
    for line in lines:
        halfway = int(len(line) / 2)
        fst_half = line[:halfway]
        snd_half = line[halfway:-1]  # excluding newline

        for c in fst_half:
            if c in snd_half:
                sum += get_priority(c)
                break

    return sum


def part2():
    sum = 0

    group_index = 0
    while group_index < len(lines):
        fst = lines[group_index]
        snd = lines[group_index + 1]
        trd = lines[group_index + 2]

        matches = []
        for c in fst:
            if c in snd:
                matches.append(c)

        for c in matches:
            if c in trd:
                sum += get_priority(c)
                break

        group_index += 3

    return sum


print(part1())
print(part2())
