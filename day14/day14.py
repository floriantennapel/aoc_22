file = open('input.txt')
pairs = [line.strip().split(' -> ') for line in file.readlines()]
file.close()

rock_paths = []
for line in pairs:
    rock_paths.append([(int(split[0]), int(split[1])) for split in [pair.split(',') for pair in line]])

 
# the size of the grid does not really matter, as long as it is big enough
width = 1000 
height = 1000 
start_col = 500 - width // 2 

lowest_rock = 0
grid = [[False for _ in range(width)] for _ in range(height)]


##############################
# Adding rock positions
##############################

def get_delta_move(current, next):
    """Returns a tuple of direction to move, and how many times to move, for example: ((d_y, d_x), n)"""
    row, col = current
    next_row, next_col = (next[1], next[0] - start_col) 

    if row - next_row != 0:
        diff = abs(row - next_row)
        if row < next_row:
            return ((1,0), diff)
        else:
            return ((-1,0), diff)
    else:
        diff = abs(col - next_col)
        if col < next_col:
            return ((0,1), diff)
        else:
            return ((0,-1), diff)


def draw_path(path):
    current = (path[0][1], path[0][0] - start_col)
    grid[current[0]][current[1]] = True
    for next in path[1:]:
        delta, n = get_delta_move(current, next)
        for _ in range(n):
            current = (current[0] + delta[0], current[1] + delta[1])
            grid[current[0]][current[1]] = True

            global lowest_rock
            lowest_rock = max(lowest_rock, current[0])



#############################
# Sand movement
#############################

def next_pos(pos):
    row, col = pos
    for d_col in [0, -1, 1]:
        new_row, new_col = row + 1, col + d_col
        if not grid[new_row][new_col - start_col]:
            return (new_row, new_col)
    # nowhere to move
    return pos


def drop_sand(part2=False):
    row, col = 0, 500
    cond = lambda r: part2 or r <= lowest_rock

    while cond(row):
        next = next_pos((row, col))
        if part2 and next[0] == 0:
            return False
        elif next[0] == row:
            grid[row][col - start_col] = True
            return True
        else:
            row, col = next

    return False



##########################
# Program start
##########################


# draw rocks on grid
for path in rock_paths:
    draw_path(path)

sand_count = 0
while drop_sand():
    sand_count += 1

# part 1
print(sand_count)


# add cave_floor
grid[lowest_rock + 2] = [True for _ in range(width)]

while drop_sand(part2=True):
    sand_count += 1
#last grain is not added
sand_count += 1

# part 2
print(sand_count)



