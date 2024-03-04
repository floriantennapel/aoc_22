file = open("input.txt")
map = [
    [ord(c) - ord("a") if c not in "SE" else c for c in line.strip()]
    for line in file.readlines()
]
file.close()


class Node:
    def __init__(self, pos, prev):
        self.pos = pos
        self.prev = prev
        self.height = map[pos[0]][pos[1]]
        self.dist = 0 if prev is None else prev.dist + 1

    def __eq__(self, other):
        if other is self:
            return True
        elif isinstance(other, Node):
            return self.pos == other.pos

        return False

    def __hash__(self):
        return hash(self.pos)


def valid_step(from_node, to_node, part1):
    from_height = from_node.height
    to_height = to_node.height

    # moving backwards in part2
    if not part1:
        temp = from_height
        from_height = to_height
        to_height = temp

    if not isinstance(from_height, int):  # start
        return to_height <= 1
    elif not isinstance(to_height, int):
        return from_height >= 24
    else:
        return to_height <= from_height + 1


def valid_moves(node, visited, part1):
    row = node.pos[0]
    col = node.pos[1]

    next = []

    if row > 0:
        next.append(Node((row - 1, col), node))
    if row < len(map) - 1:
        next.append(Node((row + 1, col), node))
    if col > 0:
        next.append(Node((row, col - 1), node))
    if col < len(map[0]) - 1:
        next.append(Node((row, col + 1), node))

    return [n for n in next if (n not in visited) and valid_step(node, n, part1)]


def dijkstra(part1=True):
    start_point = "S" if part1 else "E"
    end_point = "E" if part1 else 0

    # find starting point
    start: Node = None
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == start_point:
                start = Node((i, j), None)

    queue = [start]
    visited = set()
    while True:
        current = queue.pop(0)
        visited.add(current)
        queue = [n for n in queue if n not in visited]

        if current.height == end_point:
            return current

        queue += valid_moves(current, visited, part1)
        queue.sort(key=(lambda n: n.dist))


def print_path(end_point):
    """simple visualization of path taken"""
    pretty = [["." for _ in range(len(map[0]))] for _ in range(len(map))]

    current = end_point
    while current is not None:
        pretty[current.pos[0]][current.pos[1]] = "#"
        current = current.prev

    for line in pretty:
        print("".join(line))


print(dijkstra().dist)
print(dijkstra(part1=False).dist)
# print_path(dijkstra())
