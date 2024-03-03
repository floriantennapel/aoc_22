class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False


file = open('input.txt')
grid = [[Tree(int(c)) for c in line.strip()] for line in file.readlines()]
file.close()


def scan_line(row, col, d_row, d_col):
    count_visible = 0
    highest = -1

    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        tree = grid[row][col]

        if tree.height > highest:
            highest = tree.height
            if not tree.visible:
                count_visible += 1
                tree.visible = True

        row += d_row
        col += d_col

    return count_visible


def view_distance(row, col, d_row, d_col):
    count = 0
    height = grid[row][col].height

    row += d_row
    col += d_col
    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        next_height = grid[row][col].height
        count += 1

        if next_height >= height:
            break

        row += d_row
        col += d_col

    return count


def part1():
    sum = 0

    height = len(grid)
    width = len(grid[0])

    for row in range(height):
        sum += scan_line(row, 0, 0, 1)
        sum += scan_line(row, width - 1, 0, -1)

    for col in range(width):
        sum += scan_line(0, col, 1, 0)
        sum += scan_line(height - 1, col, -1, 0)

    return sum


def part2():
    hi_score = -1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            up = view_distance(i, j, -1, 0)
            down = view_distance(i, j, 1, 0)
            left = view_distance(i, j, 0, -1)
            right = view_distance(i, j, 0, 1)

            score = up * down * left * right
            hi_score = max(score, hi_score)

    return hi_score


print(part1())
print(part2())
