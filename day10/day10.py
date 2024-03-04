file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()

check_points = [20, 60, 100, 140, 180, 220]
sum = 0
image = ""

cycle = 1
x = 1

for line in lines:
    split = line.split()
    cmd = split[0]

    wait = 1
    add = 0

    if cmd == "addx":
        wait = 2
        add = int(split[1])

    for _ in range(wait):
        # part 1
        if cycle in check_points:
            sum += cycle * x

        # part 2
        if abs((cycle % 40) - 1 - x) <= 1:
            image += "#"
        else:
            image += "."

        cycle += 1

        if cycle % 40 == 1:
            image += "\n"

    x += add

print(sum)
print(image)
