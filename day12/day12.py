from queue import Queue

file = open('input.txt')
hills = [line.strip() for line in file.readlines()]
file.close()

class HillClimb:
    def __init__(self, pos, prev):
        self.pos = pos
        self.steps = prev.steps + 1 if prev is not None else 0
        self.height = hills[pos[0]][pos[1]]

def valid_step(prev_height, new_height):
    if new_height == 'E':
        return prev_height in 'zy'
    if prev_height == 'S':
        return new_height in 'ab'
    
    return ord(new_height) - ord(prev_height) <= 1

def valid_pos(pos):
    r = pos[0]
    c = pos[1]
    return r >= 0 and r < len(hills) and c >= 0 and c < len(hills[0])

def get_next(prev, visited, part1):
    next = set()
    
    for d_r, d_c in [(1,0), (-1,0), (0,1), (0,-1)]:
        p = prev.pos
        new_pos = (p[0] + d_r, p[1] + d_c)
        if not valid_pos(new_pos):
            continue

        new_height = hills[new_pos[0]][new_pos[1]]
        from_height = prev.height if part1 else new_height
        to_height = new_height if part1 else prev.height
        
        if new_pos not in visited and valid_step(from_height, to_height):
            next_hill = HillClimb(new_pos, prev)
            next.add(next_hill)
            visited.add(new_pos)

    return next

def find_char(c):
    for i, row in enumerate(hills):
        for j, col in enumerate(row):
            if c == col:
                return (i, j)

def bfs(part1):
    visited = set()
    queue = Queue()

    start = find_char('S') if part1 else find_char('E')
    queue.put(HillClimb(start, None))

    goal = 'E' if part1 else 'a'
    while True:
        current = queue.get()

        if current.height == goal:
            print(current.steps)
            return

        for hill_climb in get_next(current, visited, part1):
            queue.put(hill_climb)

bfs(True)
bfs(False)


