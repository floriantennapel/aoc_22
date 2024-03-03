file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


def add_pos(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def should_move(tail, head):
    return abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1


def move(tail, head):
    """Should only be called after checking a move is needed"""

    d_y = 0
    d_x = 0

    if tail[0] < head[0]:
        d_y = 1
    elif tail[0] > head[0]:
        d_y = -1

    if tail[1] < head[1]:
        d_x = 1
    elif tail[1] > head[1]:
        d_x = -1

    return add_pos(tail, (d_y, d_x))


def get_delta_dir(direction):
    match direction:
        case "U":
            return (-1, 0)
        case "D":
            return (1, 0)
        case "L":
            return (0, -1)
        case "R":
            return (0, 1)
        case _:
            print("Invalid input")
            return (0, 0)


def part1():
    visited = {(0, 0)}

    head = (0, 0)
    tail = (0, 0)

    for line in lines:
        delta = get_delta_dir(line[0])
        n = int(line[2:])

        for _ in range(n):
            head = add_pos(head, delta)
            if should_move(tail, head):
                tail = move(tail, head)
                visited.add(tail)

    return len(visited)


def part2():
    visited = {(0, 0)}
    head = (0, 0)
    knots = [(0, 0) for _ in range(9)]

    for line in lines:
        delta = get_delta_dir(line[0])
        n = int(line[2:])

        for _ in range(n):
            head = add_pos(head, delta)

            for i in range(len(knots)):
                tail = knots[i]
                in_front = head if i == 0 else knots[i - 1]

                if should_move(tail, in_front):
                    knots[i] = move(tail, in_front)

            visited.add(knots[-1])

    return len(visited)


print(part1())
print(part2())
