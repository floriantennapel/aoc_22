no_stacks = 9
moves = []


def parse_crates():
    stacks = [[] for _ in range(no_stacks)]

    file = open("crates.txt")

    for line in reversed(file.readlines()):
        for i in range(no_stacks):
            index = 1 + i * 4
            crate = line[index]
            if crate != ' ':
                stacks[i].append(crate)

    file.close()

    return stacks


def parse_moves():
    file = open("moves.txt")

    for line in file.readlines():
        nums = [int(n) for n in line.strip().split(' ') if n.isnumeric()]
        moves.append((nums[0], (nums[1], nums[2])))

    file.close()


def read_top_crates(stacks):
    return ''.join([stack[-1] for stack in stacks if len(stack) != 0])


def part1():
    stacks = parse_crates()

    for move in moves:
        from_index = move[1][0] - 1
        to_index = move[1][1] - 1

        for i in range(move[0]):
            if len(stacks[from_index]) == 0:
                break

            stacks[to_index].append(stacks[from_index].pop())

    return read_top_crates(stacks)


def part2():
    stacks = parse_crates()

    for move in moves:
        from_index = move[1][0] - 1
        to_index = move[1][1] - 1

        no_crates = move[0]

        stacks[to_index] += stacks[from_index][-no_crates:]
        stacks[from_index] = stacks[from_index][:-no_crates]

    return read_top_crates(stacks)


parse_moves()
print(part1())
print(part2())
